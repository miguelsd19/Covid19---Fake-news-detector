from textblob import Word
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer as L
import spacy
from textblob import TextBlob
from textblob import Word

def lematize(words):
    nlp = spacy.load('en_core_web_sm')
    text1 = nlp(" ".join(words))
    words.clear()
    for word in text1:
         words.append(word.lemma_)
    return words

def stopremove(tokens,tweet):
    stop_words=set(stopwords.words('english')) 
    filtered_sentence = [w for w in tokens if not w in stop_words] 
    
    for w in tokens: 
        if w not in stop_words: 
            filtered_sentence.append(w)

    return filtered_sentence

def deletecopy(text):
    text=list(dict.fromkeys(text))
    return text

def sentiment(text):
    blob=TextBlob(text)
    var=blob.sentiment.polarity
    var1=blob.sentiment.subjectivity
    if var<0 :
        sent='negative'
    elif var>0:
        sent='positive'
    elif var==0:
        sent='neutral'
    return sent,var,var1
   