import praw
import re
import time
import requests
import getpass
from security import encrypt_password, check_encrypted_password

botname = input("Enter bot user name: (sdsu-stream-bot)")
unencrypted_password = getpass.getpass("Enter the bot password: ")
hash = encrypt_password(unencrypted_password)
check_encrypted_password(unencrypted_password, hash)
print(check_encrypted_password(unencrypted_password, hash))

reddit = praw.Reddit(client_id='oRDWYVEIfzVDAg',
                     client_secret='DkfD4aB3VvrXExaJbSALR_hCmlc',
                     user_agent='<console:ncaa_stream_app:0.0.1 (by /u/sdsu-stream-bot)>',
                     username=botname,
                     password=unencrypted_password
                     )

# Check to see if post is in read only mode
# We want it to be false
print("Checking if Reddit praw obj is in read only mode...")
if (reddit.read_only == True):
    print("Uh oh, looks like Reddit is in read only mode. Exiting.")
    exit(1)
else:
    print("Everything looks good!")

# # subreddit = reddit.subreddit('ncaaBBallStreams')
# subreddit = reddit.subreddit('programmerhumor')

# for submission in subreddit.stream.submissions():
#     # do something with submission

#     if "San Diego State" in submission.title:
#         # Get comments / create comment in submission
#         print("Submission found. Replying with link...")
#         reply_text = "**HD** | [Boise State vs San Diego State | CBSSN](https://www.viprow.net/sports-basketball-online) | MISR:1 mbps | Clicks: 2 | English | Mobile : Yes"
#         break
#     else:
#         continue
