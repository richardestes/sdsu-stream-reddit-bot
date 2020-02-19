import praw
import re
import time

reddit = praw.Reddit(client_id='oRDWYVEIfzVDAg',
                     client_secret='DkfD4aB3VvrXExaJbSALR_hCmlc',
                     user_agent='<console:ncaa_stream_app:0.0.1 (by /u/sdsu-stream-bot)>',
                     username='sdsu-stream-bot',
                     password=''
                     )

print(reddit.read_only)

subreddits = ['programmerhumor']
pos = 0
errors = 0

title = "HD | Boise State vs San Diego State | CBSSN | MISR:1 mbps | Clicks: 2 | English | Mobile : Yes"
url = "https://www.viprow.net/sports-basketball-online"

def post():
    global subreddits
    global pos
    global errors

    try:
        subreddit = reddit.subreddit(subreddits[pos])
        subreddit.submit(title,url=url)
        print("Posted to " + subreddits[pos])

        pos = pos + 1
        post()

        if (pos>=len(subreddits) - 1):
            post()
        else:
            print ("Done")
    except praw.exceptions.APIException as e:
        print (e.message)
        if (e.error_type == "RATELIMIT"):
            delay = re.search("(\d+) minutes?", e.message)

            if delay:
                delay_seconds = float(int(delay.group(1)) * 60)
                time.sleep(delay_seconds)
                post()
            else:
                delay = re.search("(\d+) seconds", e.message)
                delay_seconds = float(delay.group(1))
                time.sleep(delay_seconds)
                post()
    except:
        errors = errors + 1
        if (errors > 5):
            print("Shit, we crashed.")
            exit(1)

post()



