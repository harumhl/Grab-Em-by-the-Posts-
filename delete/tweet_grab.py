consumer_key='dO8qYUOk22LqPYQD5h6WZ3Cp2'
consumer_secret='l8LOOvYM6BsyH0YNAvmvRerRbhQLO2qj1j0LlhfdTK0m14IVX1'

access_token='1480581678-SxL799KNagjx2lOad43REX6e6dHIZFQqQpizyOB'
access_token_secret='nTvOhlNytYiiK5O9DJaZnG7gTIAXxee9ANNSSSqt2sceV'

import tweepy
import time
import json
import os

#major_news_outlets = ['CNN','FoxNews','MSNBC','USATODAY','nytimes','wsj','cbsnews']

major_news_outlets = ['CNN']

def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError as e:
            print type(e)
            print "Waiting..."
            sleep(15)
        except tweepy.TweepError as e:
            print type(e)
            print "Waiting..."
            sleep(15)
        except StopIteration as e:
            print type(e)
            #return
            #print "Exception: " + e.msg

def sleep(minutes):
    for i in range(minutes):
        print "Sleeping for minute ",i
        time.sleep(60)

def make_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def process(unfiltered_json_tweet):
    time_stamp = unfiltered_json_tweet["created_at"].split()
    month = month_to_num(time_stamp[1])
    day = time_stamp[2]
    year = time_stamp[5]
    twitter_account = unfiltered_json_tweet["user"]["screen_name"]
    #print month,day,year
    #print twitter_account
    file_path = "tweets" + "/" + \
                twitter_account + "/" + \
                year + "/" + \
                month + "/" + \
                twitter_account + "-" + \
                year + "-" + month + "-" + day + ".txt"

    make_dir("tweets")
    make_dir("tweets" + "/" + twitter_account)
    make_dir("tweets" + "/" + twitter_account + "/" + year)
    make_dir("tweets" + "/" + twitter_account + "/" + year + "/" + month)

    with open(file_path, 'a') as outfile:
        json.dump(unfiltered_json_tweet, outfile)
        outfile.write("\n")
    #f = open("test.txt",'a')
    #f.write(str(unfiltered_json_tweet))
    #f.write("\n")

    #return filtered_json_tweet

def save(json_tweet):
    return

def month_to_num(month_abbr):
    return{
        "Jan":"1",
        "Feb":"2",
        "Mar":"3",
        "Apr":"4",
        "May":"5",
        "Jun":"6",
        "Jul":"7",
        "Aug":"8",
        "Sep":"9",
        "Oct":"10",
        "Nov":"11",
        "Dec":"12"
    }[month_abbr]


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


#limit_handled(tweepy.Cursor(api.search,q="since:2015-4-12 until:2016-11-14 donald OR trump OR hillary OR clinton from:CNN ")

start_date="2016-4-1"
end_date="2016-11-3"

#Test Start dates
#start_date="2016-11-14"
#end_date="2016-11-15"

query_string = "since:" + start_date + " until:" + end_date + " donald OR trump OR hillary OR clinton from:"

for news_outlet in major_news_outlets:
    query_string += news_outlet
    for tweet in limit_handled(tweepy.Cursor(api.search,q=query_string).items()):
        print query_string
        #print 'type: ' + str(type(tweet))
        #print tweet._json
        process(tweet._json)
        #print filtered_tweet




