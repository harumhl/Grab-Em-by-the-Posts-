import urllib2
import json
import datetime
import csv
import time

APP_ID="1303950803000918"
APP_SECRET="0ed9079d51e40ed406168bf199cf7425"

ACCESS_TOKEN = APP_ID + "|" + APP_SECRET

page_id = 'nytimes'

def testFacebookPageData(page_id, access_token):
    
    # construct the URL string
    base = "https://graph.facebook.com/v2.4"
    node = "/" + page_id
    parameters = "/?access_token=%s" % access_token
    url = base + node + parameters
    
    # retrieve data
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    data = json.loads(response.read())
    
    print json.dumps(data, indent=4, sort_keys=True)

def request_until_succeed(url):
    req = urllib2.Request(url)
    success = False
    while success is False:
        try: 
            response = urllib2.urlopen(req)
            if response.getcode() == 200:
                success = True
        except Exception, e:
            print e
            time.sleep(5)
            
            print "Error for URL %s: %s" % (url, datetime.datetime.now())

    return response.read()    

def testFacebookPageFeedData(page_id, access_token):
    
    # construct the URL string
    base = "https://graph.facebook.com/v2.4"
    node = "/" + page_id + "/feed" # changed
    parameters = "/?access_token=%s" % access_token
    url = base + node + parameters
    
    # retrieve data
    data = json.loads(request_until_succeed(url))
    
    return data
    #return json.dumps(data, indent=4, sort_keys=True)

facebook_json = testFacebookPageFeedData(page_id, ACCESS_TOKEN)

file_path = "facebook_sample_data.txt"
with open(file_path, 'a') as outfile:
    json.dump(facebook_json, outfile)
    outfile.write("\n")

