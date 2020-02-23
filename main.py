import praw
import re
import time
import requests
import getpass
import string
from security import encrypt_password, check_encrypted_password
from sports import check_if_game_today

# Bot Credential Setup 
# botname = input("Enter bot user name: (sdsu-stream-bot)")
botname = "sdsu-stream-bot"
unencrypted_password = getpass.getpass("Enter the bot password: ")
hash = encrypt_password(unencrypted_password)
print("Checking if password was encrypted successfully...")

if(check_encrypted_password(unencrypted_password, hash)):
    print("Password successfully encrypted.")
else:
    print("Uh oh, password was not encrypted correctly. Exiting...")
    exit(1)

# Bot Creation
print("Connecting to Reddit...")
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
    print("Uh oh, looks like Reddit is in read only mode. Exiting...")
    exit(1)
else:
    print("Reddit is not in read only mode. Continuing...")

check_if_game_today()

# subreddit = reddit.subreddit('SecretSharedDawn')

# for submission in subreddit.stream.submissions():
#     if "test post" in submission.title:
#         print("Submission found. Replying...")
#         reply_text = "hello i am a bot!"
#         submission.reply(reply_text)
#         print("Replied to post.")
#         break
#     else:
#          continue

subreddit = reddit.subreddit('ncaaBBallStreams')

for submission in subreddit.stream.submissions():
    # do something with submission

    if "San Diego St" in submission.title:
        split_title = submission.title.split("vs")
        reddit_title_left = split_title[0]
        # print(reddit_title_left)
        split_colon = reddit_title_left.split(":")
        # print(split_colon[1])
        reddit_team_name_left = split_colon[1].lstrip()
        print(reddit_team_name_left)
        r_vs = re.compile(r"^\W+")  
        tmp_right = r_vs.sub("",split_title[1])
        reddit_title_right = tmp_right.split()
        reddit_team_name_right = reddit_title_right[0]
        print(reddit_team_name_right)
        # Get comments / create comment in submission
        print("Submission found. Replying with link...")
        game_title = reddit_team_name_left + "vs " + reddit_team_name_right
        print(game_title)
        reddit_team_left_formatted = reddit_team_name_left.translate(str.maketrans('', '', string.punctuation))
        reddit_team_name_left_link = reddit_team_left_formatted.lower().strip().lstrip().replace(' ', '-')
        print(reddit_team_name_left_link)
        reddit_team_right_formatted = reddit_team_name_right.translate(str.maketrans('','', string.punctuation))
        reddit_team_name_right_link = reddit_team_right_formatted.lower().strip().lstrip().replace(' ', '-')
        
        game_link = reddit_team_name_left_link + "-vs-" + reddit_team_name_right_link + "-1-online-stream"
        print(game_link)
        reply_text = "**HD** | [" + game_title + "](https://www.viprow.net/" + game_link +") | Clicks: 2 | English | Disable Adblock"
        print(reply_text)
        # submission.reply(reply_text)
        break
    else:
        continue
