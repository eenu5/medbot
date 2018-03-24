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
    print("stemmed",stemmed)
    for w in stemmed:
        if w.lower() != 'name':
            print(w)
            tag = nltk.pos_tag(w)
            namedEntity = nltk.ne_chunk(tag, binary=True)
            
    
    print('namesd',namedEntity)
   
    
            

def greet():
    k = np.random.randint(50)
    print(gd[k%11])

def askName():
    k = np.random.randint(50)
    print(nd[k%7])
    inp = input()
    return inp
