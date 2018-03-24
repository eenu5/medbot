import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
import pandas as pd
import numpy as np
import json
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import random

#new libraries
import difflib

sr = pd.read_csv('E:\\MedBot\\final dataset.csv', engine='python')
sr = np.array(sr)
dis = sr[:,1]
symp = sr[:,2]

dis = np.array(dis)
symp = np.array(symp)

def stopWords(text):
    #text is a sentence
    stopw = set(stopwords.words('english'))
    filtered = []
    words = word_tokenize(text)
    for i in words:
        if i not in stopw:
            filtered.append(i)
    return filtered

def stemming(text):
    #text could be a sent or word
    ps = PorterStemmer()
    empty = []
    for w in text:
        empty.append(w)
    return empty

def getSymptoms():
    print('Please tell me about your symproms')
    inp = input()
    sent = sent_tokenize(inp)
    filt = stopWords(inp)
    
    #compare input with csv file with filtered sentence
    i1=i2=i3=0
    max1=0
    max2=1
    max3=2
    for i in range(symp.size):
        sequence = difflib.SequenceMatcher(isjunk=None, a=filt, b=symp[i])
        diff = sequence.ratio()*100
        if(diff>max1):
            max3=max2
            max2=max1
            max1=diff
            i1=i
        elif(diff>max2):
            max3=max2
            max2=diff
            i2=i
        elif(diff>max3):
            max3=diff
            i3=i

    print('Diagnosed Diseases are:')
    if(i1!=i2!=i3):
        print(dis[i1])
        print(dis[i2])
        print(dis[i3])
    else:
        print(dis[i1])
               
     

Sym = getSymptoms()


