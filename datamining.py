import tweepy
import json
import csv

# 4 cadenas para la autenticacion
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
# con este objeto realizaremos todas las llamadas al API
api = tweepy.API(auth,
                 wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True)

def strip_undesired_chars(tweet):
    stripped_tweet = tweet.replace('\n', ' ').replace('\r', '')
    char_list = [stripped_tweet[j] for j in range(len(stripped_tweet)) if ord(stripped_tweet[j]) in range(89654)]
    stripped_tweet=''
    for j in char_list:
        stripped_tweet=stripped_tweet+j
    return stripped_tweet

alltweets=[]

#Buscar Tweets

#new_tweets = api.search(q="plandemic",count=10000) #TerrorismoSanitario #AstraZeneca 
                                                  #AntiPassSanitaire #antipass #nogreenpass #novax  #VaccineCertificate #flue 
                                                  #Delta vaccine dangerous pfizer sputnik covid plandemic #vaccine
                                                  #TheGreatReset  #SCAMDEMIC #Covid19 #pandemic #coronavirus
                                                  #NoVaccinePassportsAnywhere  #experimental 
query= "#plandemic"
new_tweets = [status
   for status in tweepy.Cursor(api.search, q = query).items(1000)
]

outtweets = [( tweet.created_at, tweet.text , tweet.retweet_count, tweet.favorite_count, tweet.lang, tweet.user.name, tweet.user.id, tweet.user.followers_count) for tweet in new_tweets]


with open('covid19tweets.csv', "a", encoding="utf-8", newline='') as f:       
        writer = csv.writer(f)
        #writer.writerow(['created_at','text','retweet_count', 'favorite_count','lang', 'user', 'user id','user followers', 'possibly sensitive'])
        writer.writerows(outtweets)


