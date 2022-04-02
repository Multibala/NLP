from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
from sklearn.svm import SVC
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split




def analyze(text):
    txt = f_vectorizer.transform([text])
    res = model.predict(txt)
    return 'spam' if res  == [1] else 'not spam'

def setup():
    df = pd.read_csv('data/spam.csv',encoding = 'ISO-8859-1')
    df = df.iloc[:,: 2]
    df.columns = ['label','data'] 
    df['b_labels'] = df['label'].map({'spam':1,'ham':0})
    y = df['b_labels'].to_numpy()
    df_train,df_test,y_train,y_test = train_test_split(df['data'],y,test_size = 0.2,random_state = 1)

    tfidf = TfidfVectorizer(decode_error='ignore')
    X_train = tfidf.fit_transform(df_train)
    X_test = tfidf.transform(df_test)
    temp1 = MultinomialNB()
    temp1.fit(X_train,y_train)
    tfidf_score = temp1.score(X_test,y_test)

    featurizer = CountVectorizer(decode_error='ignore')
    X_train = featurizer.fit_transform(df_train)
    X_test = featurizer.transform(df_test)
    temp2 = MultinomialNB()
    temp2.fit(X_train,y_train)
    
    cv_score = temp2.score(X_test,y_test)
    global model
    global f_vectorizer
      
    model,f_vectorizer = [(temp1,tfidf),(temp2,featurizer)][float(cv_score)>float(tfidf_score)]
   
    
# run()
# print(analyze('Great! I hope you like your man well endowed. I am  &lt;#&gt;  inches...'))   



