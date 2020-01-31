#!/usr/bin/python

import os
import re
import time
import praw
import random
import atexit
import logging
from time import strftime
from random_words import RandomWords
from systemd.journal import JournalHandler

reddit = praw.Reddit('HaveSomeWords')

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

# Try to write logs to journald.
log = logging.getLogger('log')
log.addHandler(JournalHandler())
log.setLevel(logging.DEBUG)

log.info("Script started")

rw = RandomWords()

replyhead = "I hear that you are missing some words. Here are some random ones that you may find useful.\n"
replytail = "\n---\n^^Bzoorp! ^^I'm ^^a ^^bot. ^^If ^^there ^^is ^^a ^^problem ^^with ^^me, ^^then ^^contact ^^my ^^[creator](https://www.reddit.com/message/compose/?to=SatoriVII)."

repliedto = []

def pbot():
    wl = open("/home/satori7/Dropbox/Code/Python/HaveSomeWords/whitelist.list", "r")
    whitelist = wl.readlines()
    whitelist = ''.join(whitelist)
    wl.close()
    for comment in reddit.subreddit(whitelist).comments(limit=100):
        if re.search('have no words', comment.body, re.IGNORECASE) and comment.id not in repliedto:
            log.info('Replied to a post in ' + str(comment.subreddit))
            print("Got one")
            rwords = rw.random_words(count=19)
            roneword = rw.random_words(count=1)
            reply = replyhead + ", ".join(rwords) + replytail
            comment.reply(reply)
            repliedto.append(comment.id)
            return pbot

while True:
    pbot()
    time.sleep(2)
