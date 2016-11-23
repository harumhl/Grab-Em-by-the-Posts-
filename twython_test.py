from twython import Twython # pip install twython
import time # standard lib

''' Go to https://apps.twitter.com/ to register your app to get your api keys '''
CONSUMER_KEY = 'dO8qYUOk22LqPYQD5h6WZ3Cp2'
CONSUMER_SECRET = 'l8LOOvYM6BsyH0YNAvmvRerRbhQLO2qj1j0LlhfdTK0m14IVX1'
ACCESS_KEY = '1480581678-SxL799KNagjx2lOad43REX6e6dHIZFQqQpizyOB'
ACCESS_SECRET = 'nTvOhlNytYiiK5O9DJaZnG7gTIAXxee9ANNSSSqt2sceV'

#consumer_key='dO8qYUOk22LqPYQD5h6WZ3Cp2'
#consumer_secret='l8LOOvYM6BsyH0YNAvmvRerRbhQLO2qj1j0LlhfdTK0m14IVX1'

#access_token='1480581678-SxL799KNagjx2lOad43REX6e6dHIZFQqQpizyOB'
#access_token_secret='nTvOhlNytYiiK5O9DJaZnG7gTIAXxee9ANNSSSqt2sceV'

twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
lis = [798275328305045504] ## this is the latest starting tweet id
#lis = [791799119677448200] ##this is a starting id from october
while True: ## iterate through all tweets
## tweet extract method with the last list item as the max_id
    try:
        user_timeline = twitter.get_user_timeline(screen_name="CNN",count=200, include_retweets=False, max_id=lis[-1])
    except Exception as e:
        print type(e)

    for tweet in user_timeline:
        print tweet['text'] ## print the tweet
        lis.append(tweet['id']) ## append tweet id's

    print lis[-1]
    print "Going to sleep:"
    for j in range(0,4):
        print "Sleeping for minute:",j
        #time.sleep(60) ## 5 minute rest between api calls

    for tweet in user_timeline:
        print tweet['created_at'] ## print the tweet
        lis.append(tweet['id']) ## append tweet id's
