import tweepy

#Major news outlets and their tweets: (oldest w)
major_news_outlets = {'CNN':(0,1),
                      'FoxNews':(0,1),
                      'MSNBC':(0,1),
                      'USATODAY':(0,1),
                      'nytimes':(0,1),
                      'wsj':(0,1),
                      'cbsnews':(0,1)}

def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(15 * 60)



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

'''
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text
'''

#api.user_timeline([id/user_id/screen_name][, since_id][, max_id][, count][, page])


cnn_tweets = api.user_timeline('CNN')
print type(cnn_tweets)
for tweet in cnn_tweets:
    print 'type: ' + str(type(tweet))
    print tweet._json



