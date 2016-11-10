#import os, base64, time

#oauth_consumer_key=''
#oauth_nonce = base64.base63encode(os.urandom(32))
#oauth_signature_method = HMAC-SHA1
#oauth_timestamp = str(int(time.time()))
#oauth_version='1.0'

import tweepy

consumer_key = 'dO8qYUOk22LqPYQD5h6WZ3Cp2'
consumer_secret = 'l8LOOvYM6BsyH0YNAvmvRerRbhQLO2qj1j0LlhfdTK0m14IVX1'
access_token = '1480581678-SxL799KNagjx2lOad43REX6e6dHIZFQqQpizyOB'
access_token_secret = 'nTvOhlNytYiiK5O9DJaZnG7gTIAXxee9ANNSSSqt2sceV'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet

