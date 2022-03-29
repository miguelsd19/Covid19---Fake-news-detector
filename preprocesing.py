
from textblob import TextBlob ## if not work use pip install TextBlob ---- pip install -U textblob
import re
import process as p
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import preprocessor as c
import csv


c.set_options(c.OPT.URL,c.OPT.RESERVED,c.OPT.EMOJI)

def procesing(tweet):

    #Limpiamos el tweet
    tweet=c.clean(tweet)
    

    regex = '[\\!\\"\\#\\$\\%\\&\\\'\\(\\)\\*\\+\\,\\-\\.\\/\\:\\;\\<\\=\\>\\?\\@\\[\\\\\\]\\^_\\`\\{\\|\\}\\~]'
    tweet = re.sub(regex , ' ', tweet)

    # Eliminación de páginas web (palabras que empiezan por "http")
    tweet = re.sub('http\S+', ' ', tweet)

    # sin usuarios
    tweet = re.sub('@\S+',' ', tweet)

    # sin etiquetas
    tweet = re.sub('#\S+',' ', tweet)
    print("Done")

    #quitamos el "RT"
    tweet= tweet.replace('RT', ' ')

    tweet=c.clean(tweet)

    tweet = re.sub("\\s+", ' ', tweet)

    tokenized_tweet = tweet.split(sep = ' ')

    # Eliminación de tokens con una longitud < 2
    tokenized_tweet = [token for token in tokenized_tweet if len(token) > 1]

    return  tweet, tokenized_tweet
var=0
with open('datasetENG.csv', 'r', encoding="cp850", newline='') as tweets:
    reader=csv.reader(tweets)
    #abrimos el tweet que vamos a escribir
    with open('cleantweets.csv', "w",encoding="utf-8", newline='') as f: 
        writer = csv.writer(f)
        for record in reader:
            num,text,retweet_count,favorite_count,lang,user,user_id, user_followers=record #Descomprimimos las columnas del csv
            tweet_text,tokenized_tweet=procesing(text)#Pasamos la columna text por el proceso y retorna los argumentos sentiment,pol,sub,tweet_text
            writer.writerow([tweet_text,user,retweet_count,tokenized_tweet])#Escribimos en el csv los valores
            var=var+1
            print(var)