import urllib2
import json
import datetime
import csv
import time

#APP_ID=""
#APP_SECRET=""

ACCESS_TOKEN = APP_ID + "|" + APP_SECRET

#page_id = 'nytimes'

RELEVANT_NEWS_SITES = ['usatoday','wsj','CBSNews']

WORDS_IN_RELEVNT_STATUSES = ['donald','trump','hillary','clinton','electoral','election','president-elect']

OLDEST_RELEVANT_DATE = [2015,4,12]
MOST_RECENT_RELEVANT_DATE = [2016,11,16]

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

def getFacebookPageFeedData(page_id, access_token, num_statuses):
    
    # construct the URL string
    base = "https://graph.facebook.com"
    node = "/" + page_id + "/feed" 
    parameters = "/?fields=message,link,created_time,type,name,id,likes.limit(1).summary(true),comments.limit(1).summary(true),shares&limit=%s&access_token=%s" % (num_statuses, access_token) # changed
    url = base + node + parameters
    
    # retrieve data
    data = json.loads(request_until_succeed(url))
    
    return data

def processFacebookPageFeedStatus(status):
    
    # The status is now a Python dictionary, so for top-level items,
    # we can simply call the key.
    
    # Additionally, some items may not always exist,
    # so must check for existence first
    
    status_id = status['id']
    status_message = '' if 'message' not in status.keys() else status['message'].encode('utf-8')
    link_name = '' if 'name' not in status.keys() else status['name'].encode('utf-8')
    status_type = status['type']
    status_link = '' if 'link' not in status.keys() else status['link']
    
    
    # Time needs special care since a) it's in UTC and
    # b) it's not easy to use in statistical programs.
    
    status_published = datetime.datetime.strptime(status['created_time'],'%Y-%m-%dT%H:%M:%S+0000')
    status_published = status_published + datetime.timedelta(hours=-5) # EST
    status_published = status_published.strftime('%Y-%m-%d %H:%M:%S') # best time format for spreadsheet programs
    
    # Nested items require chaining dictionary keys.
    
    num_likes = 0 if 'likes' not in status.keys() else status['likes']['summary']['total_count']
    try:
        num_comments = 0 if 'comments' not in status.keys() else status['comments']['summary']['total_count']
    except KeyError as e:
        print e
        num_comments = 0
    num_shares = 0 if 'shares' not in status.keys() else status['shares']['count']
    
    # return a tuple of all processed data
    return (status_id, status_message, link_name, status_type, status_link,
           status_published, num_likes, num_comments, num_shares)

def scrapeFacebookPageFeedStatus(page_id, access_token):
    with open('%s_facebook_statuses.csv' % page_id, 'wb') as file:
        w = csv.writer(file)
        w.writerow(["status_id", "status_message", "link_name", "status_type", "status_link",
           "status_published", "num_likes", "num_comments", "num_shares"])
        
        has_next_page = True
        num_processed = 0   # keep a count on how many we've processed
        scrape_starttime = datetime.datetime.now()
        
        print "Scraping %s Facebook Page: %s\n" % (page_id, scrape_starttime)
        
        statuses = getFacebookPageFeedData(page_id, access_token, 100)
        
        while has_next_page:
            for status in statuses['data']:

                status_data = processFacebookPageFeedStatus(status)
                date = status_data[5].split("-")
                year = int(date[0])
                month = int(date[1])
                day = int(date[2].split()[0])
                status=status_data[1]

                #print year,month,day
                #print "status:",status


                if datetime.datetime(year,month,day) < datetime.datetime(OLDEST_RELEVANT_DATE[0],OLDEST_RELEVANT_DATE[1],OLDEST_RELEVANT_DATE[2]):
                    return
                if datetime.datetime(year,month,day) < datetime.datetime(MOST_RECENT_RELEVANT_DATE[0],MOST_RECENT_RELEVANT_DATE[1],MOST_RECENT_RELEVANT_DATE[2]):
                    if any(x in status.lower() for x in WORDS_IN_RELEVNT_STATUSES):
                        w.writerow(status_data)
                else:
                    pass

                
                # output progress occasionally to make sure code is not stalling
                num_processed += 1
                if num_processed % 1000 == 0:
                    print "%s Statuses Processed: %s" % (num_processed, datetime.datetime.now())
                    
            # if there is no next page, we're done.
            if 'paging' in statuses.keys():
                statuses = json.loads(request_until_succeed(statuses['paging']['next']))
            else:
                has_next_page = False
                
        
        print "\nDone!\n%s Statuses Processed in %s" % (num_processed, datetime.datetime.now() - scrape_starttime)

'''
facebook_json = getFacebookPageFeedData(page_id, ACCESS_TOKEN,100)

file_path = "facebook_sample_data.txt"
with open(file_path, 'a') as outfile:
    json.dump(facebook_json, outfile)
    outfile.write("\n")
'''

'''
test_status = getFacebookPageFeedData(page_id, ACCESS_TOKEN, 1)["data"][0]
#print json.dumps(test_status, indent=4, sort_keys=True)

processed_test_status = processFacebookPageFeedStatus(test_status)
print processed_test_status
'''

for page_id in RELEVANT_NEWS_SITES:
    scrapeFacebookPageFeedStatus(page_id, ACCESS_TOKEN)
