import tweepy
import json
import random
import secrets



def lambda_handler(event, context):
    data = json.load(open('all_tweets2.json'))

    #print random tweets
    random_tweet = random.choice(data)

    #should hide these
    consumer_key = secrets.consumer_key
    consumer_secret = secrets.consumer_secret
    access_token = secrets.access_token
    access_token_secret = secrets.access_token_secret

    auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token,access_token_secret)

    api = tweepy.API(auth)

    tweet_post_result = api.update_status(random_tweet)

    return {
        'statusCode': 200,
        'body': json.dumps('It worked!')
    }

