

from nltk import sent_tokenize, word_tokenize, wordpunct_tokenize
import pandas as pd
import numpy as np
import nltk

# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('averaged_perceptron_tagger')

summ_model_name = 'google/pegasus-cnn_dailymail'



from transformers import pipeline, AutoTokenizer

summarizer = pipeline("summarization", model=summ_model_name)

summ_tokenizer = AutoTokenizer.from_pretrained(summ_model_name)

def first_char_capital(sentence):
    return sentence[0].upper() == sentence[0]

def get_sentences(text):
    sent = []
    sentences = sent_tokenize(text)
    print(sentences)
    for s in sentences:
        s = s.strip()
        if not s:
            continue
        if s in ['”']:
            sent[-1] += s
        elif first_char_capital(s):
            if len(sent)>0 and sent[-1].endswith(':'):
                sent[-1] +=s
            else:
                sent.append(s)
        else:
            if len(sent)>0:
                sent[-1]+=s
            else:
                sent.append(s)
    return sent

def get_summarize_text(text):
  
    summ_text_1 = summarizer([text], min_length = 5, max_length=150, do_sample = False)[0]["summary_text"]
    return summ_text_1

# ex_text = 'Tesla soon established his own laboratory, where his inventive mind could be given free rein. He experimented with shadowgraphs similar to those that later were to be used by Wilhelm Röntgen when he discovered X-rays in 1895. Tesla’s countless experiments included work on a carbon button lamp, on the power of electrical resonance, and on various types of lighting.'


# row = get_summarize_text(ex_text)

# print(row)




