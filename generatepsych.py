from bs4 import BeautifulSoup
import json

all_objects = json.load(open('psychobjects4.json'))

all_tweets = []

for obj in all_objects:
    #works
    # print("This is a " + obj['titles'][0])

    titles = obj['titles'][0].split(',')[0]
    dates = obj['date'][0]
    url = obj['url']
    full_tweet_text = ("What is this thing from " + (dates) + "?! The " + (titles) +"... "+ (url))
    
    print(full_tweet_text)
    all_tweets.append(full_tweet_text)
    print('------------')


json.dump(all_tweets, open('all_tweets2.json','w'),indent=2)