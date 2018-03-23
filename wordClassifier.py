import nltk
from nltk import word_tokenize
from nltk import sent_tokenize
from nltk.corpus import stopwords
from nltk.corpus import wordnet
#wordnet for using sysnsets

text = input()
sent = sent_tokenize(text)
for i in sent:
    token = word_tokenize(i)
    print(token)

stop = set(stopwords.words("english"))

filteredSentence = []
for w in token:
    if w not in stop:
        filteredSentence.append(w)

print("filtered sentence: ",filteredSentence)




#create a database of all the symptoms and compare it with the tokens and stemmed tokens
#if comparision % is more than 80, consider them else dont

#ask use to verify the symptoms
#if user adds something, filter the sentence and compare it from the database
#if match is >80%, add ot otherwise google it and add symptoms  
