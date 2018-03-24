import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
import pandas as pd
import numpy as np
import json
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import random


#greeting file
gr = pd.read_csv('E:\\MedBot\\Greeting Dataset.csv', engine='python')
gr = np.array(gr)
gd = gr[:,0]

#thankyou file
tu = pd.read_csv('E:\\MedBot\\ThankYou.csv', engine='python')
tu = np.array(tu)
td = gr[:,0]

#welcome file
wc = pd.read_csv('E:\\MedBot\\Welcome Dataset.csv', engine='python')
wc = np.array(wc)
wd = wc[:,0]

#age file
ag = pd.read_csv('E:\\MedBot\\AGE Dataset.csv', engine='python')
ag = np.array(ag)
ad = ag[:,0]

#bye file
by = pd.read_csv('E:\\MedBot\\BYE Dataset.csv', engine='python')
by = np.array(by)
bd = by[:,0]

#name file
nm = pd.read_csv('E:\\MedBot\\Name Dataset.csv', engine='python')
nm = np.array(nm)
nd = nm[:,0]

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
        

def getName(text):
    #text is a/many sentence
    #takes the user response and returns name of the user
    filtered = stopWords(text)
    stemmed = stemming(filtered)
##    print("stemmed",stemmed)
    tag = nltk.pos_tag(stemmed)
    #print(tag)
    noun=[]
    for i in range(len(tag)):
##        print(tag[i][1])
        if ((str(tag[i][1])=='NN' or str(tag[i][1])=='NNP') and str(tag[i][0])!='name'):
            noun.append(tag[i][0])
##    print(noun)
##    chunkGram = r"""Chunk: {<NN+>*}  """
##    chunkParser = nltk.RegexpParser(chunkGram)
##    chunked = chunkParser.parse(tag)
##    print(chunked)
##    for i in chunked:
##        if i != ('name', 'NN'):
##            name = i
##            print('i=',i[0])
##
##    print(name[0])
    return noun

def greet():
    k = random.randint(0,50)
    print(gd[k%11])

def askName():
    k = random.randint(0,50)
    print(nd[k%7])
    inp = input()
    return inp

def askAge():
    k = random.randint(0,50)
    print(ad[k%8])
    inp = input()
    return inp

def getAge(text):
    #text is a sentence(string)
    #expected output: age in number
    filtered = stopWords(text)
    for i in filtered:
        try:
            age = int(i)
        except Exception as e:
            continue
    return age

def askGender():
    print('Are you a Male or a Female?')
    inp = input()
    return inp

def sorry():
    print('I\'m sorry I could not understand that. Let\'s try again.')

def getGender(text):
    #text is a sentence(string)
    #expected output: 'Male' or 'Female'
    filtered = stopWords(text)
    for i in filtered:
        if i.lower()=='male' or i.lower()=='female':
            gender = i
            flag=1
    if flag!=1:
        return 0
    else:
        return gender

def getEmail():
    


#Starting the conversation 
greet()
print('I\'m MedBot, your personal health assistant.')
print("I can help you find out what's going on with a simple symptom assisment.")
ufName = askName()
name = getName(ufName)
ufAge = askAge()
age = getAge(ufAge)
ufGender = askGender()
gender = getGender(ufGender)
while gender==0:
    sorry()
    ufGender = askGender()
    gender = getGender(ufGender)
print('To help you keep a record of your symptoms and enable us to provide you with better assistance, we would like you to provide us with your email. This is mandatory.')
email = getEmail()

##print('name = {}, age = {}'.format(name[0],age))
print('Okay {} '.format(name[0]))
print('Can you please discribe ')

##while(True):
    #because the user might type things continuously
    #return when the user says something to stop the conversation

    #get a random number for greeting(size = 0-7)      
