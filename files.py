import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
import pandas as pd
import numpy as np
import json

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
