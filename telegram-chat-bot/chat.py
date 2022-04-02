import random
import json
import torch
from model import NeuralNet
from nltk_utils import bag_of_words,tokenize
from config import INTENTS_URL,FILE,TELEGRAM_BOT_API_KEY
from telegram import *

import telebot

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open(INTENTS_URL) as f:
    intents = json.load(f)

data = torch.load(FILE)

input_size = data['input_size']
hidden_size = data['hidden_size']
output_size = data['output_size']
all_words = data['all_words']
tags = data['tags']
model_state = data['model_state']

model = NeuralNet(input_size,hidden_size,output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = 'Multi_bot'
bot = telebot.TeleBot(TELEGRAM_BOT_API_KEY)


def main():
    
    while True:
        sentence = input('YOU:')
        if sentence == 'quit':
            break
        
        sentence = tokenize(sentence)
        X = bag_of_words(sentence,all_words)
        X = X.reshape(1,X.shape[0])
        X = torch.from_numpy(X)
        output = model(X)
        _,predicted = torch.max(output,dim=1)
        tag = tags[predicted.item()]

        probs = torch.softmax(output,dim=1)
        prob = probs[0][predicted.item()]

        if prob.item() >0.75:
            for intent in intents['intents']:
                if tag == intent['tag']:
                    print(f'{bot_name}:{random.choice(intent["responses"])}')
        else:
            print(f'{bot_name}: i dont  understand')

main()
