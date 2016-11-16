consumer_key='dO8qYUOk22LqPYQD5h6WZ3Cp2'
consumer_secret='l8LOOvYM6BsyH0YNAvmvRerRbhQLO2qj1j0LlhfdTK0m14IVX1'

access_token='1480581678-SxL799KNagjx2lOad43REX6e6dHIZFQqQpizyOB'
access_token_secret='nTvOhlNytYiiK5O9DJaZnG7gTIAXxee9ANNSSSqt2sceV'

import tweepy
import time

#major_news_outlets = ['CNN','FoxNews','MSNBC','USATODAY','nytimes','wsj','cbsnews']

major_news_outlets = ['CNN']

def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            print "Waiting..."
            time.sleep(15 * 60)
        except tweepy.TweepError:
            print "Waiting..."
            time.sleep(15 * 60)
        except StopIteration as e:
            print type(e)
            return
            #print "Exception: " + e.msg

def process(unfiltered_json_tweet):
    f = open("test.txt",'a')
    f.write(str(unfiltered_json_tweet))
    f.write("\n")

    #return filtered_json_tweet

def save(json_tweet):
    return


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


#limit_handled(tweepy.Cursor(api.search,q="since:2015-4-12 until:2016-11-14 donald OR trump OR hillary OR clinton from:CNN ")

query_string = "since:2015-4-12 until:2016-11-14 donald OR trump OR hillary OR clinton from:"

for news_outlet in major_news_outlets:
    query_string += news_outlet
    for tweet in limit_handled(tweepy.Cursor(api.search,q="since:2016-11-10 until:2016-11-14 donald OR trump OR hillary OR clinton from:CNN").items()):
        print query_string
        #print 'type: ' + str(type(tweet))
        #print tweet._json
        process(tweet._json)
        #print filtered_tweet




