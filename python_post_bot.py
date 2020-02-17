import praw
import re
import time

reddit = praw.Reddit(client_id='oRDWYVEIfzVDAg',
                     client_secret='DkfD4aB3VvrXExaJbSALR_hCmlc',
                     user_agent='<console:ncaa_stream_app:0.0.1 (by /u/sdsu-stream-bot)>',
                     username='sdsu-stream-bot',
                     password='SDDeveloper42!'
                     )

print(reddit.read_only)

subreddits = ['ncaabballstreams', 'sdsu']
pos = 0
