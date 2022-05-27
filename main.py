import sys
import tweepy
import json
import time

# get configs
try:
    with open('twitterconfig.json', 'r') as f:
        config = json.load(f)
except:
    print("config file error. New Config generated. Please verify token data in config file.")
    with open('twitterconfig.json', 'w') as f:
        config = {"consumerKey": "",
                  "consumerSecret": "",
                  "authToken" : "",
                  "authSecret" : "",
                  "watchlist": [],
                  "searchInterval": 10}
        json.dump(config, f)
    sys.exit()


client = tweepy.Client(consumer_key=config['consumerKey'], consumer_secret=config['consumerSecret'],
                       access_token=config['authToken'], access_token_secret=config['authSecret'])



while True:
    # get timeline
    timeline = {}
    for user in config['watchlist']:
        timeline[user] = []
        response = client.get_users_tweets(id=user,max_results=config['tweetcount'],user_auth=True)
        for tweet in response.data:
            l = {'id' : tweet.id,
                 'text' : tweet.text}
            timeline[user].append(l)

    #saving timelinedata
    with open('tweetdata.json', 'w') as f:
        json.dump(timeline,f)

    print('updated datafile.')

    time.sleep(int(config['searchInterval']))



