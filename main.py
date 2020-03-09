import praw
import re
import time
import requests
import getpass
import string
import logging
import math
import progressbar
from security import encrypt_password, check_encrypted_password
from sports import check_if_game_today

# Bot Credential Setup
botname = "sdsu-stream-bot"
unencrypted_password = getpass.getpass("Enter the bot password: ")


def create_progress_bar(secs):
    # 900 = 15 mins
    # 1800 = 30 mins
    # 3600 = 1 hour
    # 7200 = 2 hours
    # 43200 = 12 hours
    # 86400 = 24 hours
    print('Sleeping for ' + str(secs) + ' seconds...')
    bar = progressbar.ProgressBar(max_value=100)
    for i in range(secs):
        time.sleep(1)
        tmp = i / secs * 100
        if ((tmp % 1) == 0):
            tmpInt = int(tmp)
            bar.update(tmpInt)


def test_submission(reddit_username, reddit_password):

    hash = encrypt_password(reddit_password)
    print("Checking if password was encrypted successfully...")
    if(check_encrypted_password(reddit_password, hash)):
        print("Password successfully encrypted.")
    else:
        print("Uh oh, password was not encrypted correctly. Exiting...")
        exit(1)

    # Bot Creation
    print("Connecting to Reddit...")
    reddit = praw.Reddit(client_id='oRDWYVEIfzVDAg',
                         client_secret='DkfD4aB3VvrXExaJbSALR_hCmlc',
                         user_agent='<console:ncaa_stream_app:0.0.1 (by /u/sdsu-stream-bot)>',
                         username=reddit_username,
                         password=reddit_password
                         )
    subreddit = reddit.subreddit('SecretSharedDawn')

    for submission in subreddit.stream.submissions():
        if "test post" in submission.title:
            print("Submission found. Replying...")
            reply_text = "hello i am a bot!"
            submission.reply(reply_text)
            print("Replied to post.")
            break
        else:
            continue


def post_sdsu_stream(reddit_username, reddit_password):

    hash = encrypt_password(reddit_password)
    print("Checking if password was encrypted successfully...\U0001F928")
    if(check_encrypted_password(reddit_password, hash)):
        print("Password successfully encrypted.")
    else:
        print("Uh oh, password was not encrypted correctly. Exiting...\n")
        exit(1)

    # Bot Creation
    print("Seeing if we can connect to reddit...\U0001F914")
    reddit = praw.Reddit(client_id='oRDWYVEIfzVDAg',
                         client_secret='DkfD4aB3VvrXExaJbSALR_hCmlc',
                         user_agent='<console:ncaa_stream_app:0.0.1 (by /u/sdsu-stream-bot)>',
                         username=reddit_username,
                         password=reddit_password
                         )
    # Check to see if post is in read only mode
    # We want it to be false
    print("Wow we connected to reddit awesome")
    print("Checking if Reddit praw obj is in read only mode...")
    if (reddit.read_only == True):
        print("Uh oh, looks like Reddit is in read only mode. Exiting...\n")
        exit(1)
    else:
        print("Reddit is not in read only mode. Continuing...\n")

    if check_if_game_today():

        subreddit = reddit.subreddit('ncaaBBallStreams')

        for submission in subreddit.stream.submissions():
            # do something with submission

            if "San Diego St" in submission.title:
                title = submission.title.split(":")
                game_title_with_time = title[1]
                game_title_with_time.lstrip()
                game_title = game_title_with_time.split("[")
                game_title_no_time = game_title[0]
                game_title_no_time.strip()
                # Get comments / create comment in submission
                print("Submission found. Replying with link...")
                print(game_title_no_time)
                reply_text = "**HD** | ["+game_title_no_time + \
                    "](https://www.viprow.me/sports-basketball-online) | Clicks: 2 | English | Disable Adblock"
                print(reply_text)
                submission.reply(reply_text)
                print(
                    "Replied to submission. \U0001F60D My job here is done. Going to sleep for 24 hours zzz...\U0001F634 \n")
                create_progress_bar(86400)
                break
            else:
                continue

    else:
        print("Game not found! Going to sleep for 2 hours zzz... \U0001F634 \n")
        create_progress_bar(7200)


while True:
    try:
        post_sdsu_stream(botname, unencrypted_password)
        # test_submission(botname, unencrypted_password)
        create_progress_bar(900)
    except Exception as e:  # probably an APIException error
        logging.basicConfig(filename='error_log.txt', level=logging.ERROR)
        logging.error(e)
        create_progress_bar(900)
