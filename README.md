# 220 Tutorials - Madlibs Twitter Bot
A Python script that finds the most recent tweet you were mentioned in, uses AI to figure out out if the word in the mention is a noun/verb/adjective, and tweets a funny sentence containing that word

## Prerequesities
Before running the code or beginning the tutorial, ensure you have

* Python 3 - https://www.python.org/downloads/
* tweepy
* random
* nltk 

`pip install tweepy && pip install random && pipi install nltk`

Follow [this tutorial](https://www.guru99.com/download-install-nltk.html) for downloading nltk.

## How it works
Our code uses the tweepy API to find the most recent mention on Twitter and adds it to a string, removing the @ tag. It then uses the wordnet database to 
figure out if the word is a noun, verb, or adjective, and tweets a funny sentence accordingly. 

## Wordnet
Wordnet is a word database that has so many capabilities. We're just using one of them here! [Find out more here](https://wordnet.princeton.edu/)
