from requests_oauthlib import OAuth1Session
import json
import os
import re
import urllib
import config

# Twitterオブジェクトの生成
CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET

#ツイートを100件取得
twitter = OAuth1Session(CK,CS,AT,ATS)
mkdir_name = "mei_image"
def get_tweet(word):
   url = "https://api.twitter.com/1.1/search/tweets.json"
   params = {'q': word,
             'count': 100
             }
   req = twitter.get(url, params=params)
   timeline = json.loads(req.text)
   return timeline

#保存先を作る
def dir_check():
   if not os.path.isdir(mkdir_name):
       os.mkdir(mkdir_name)
   check_count = 0
   while True:
       if not os.path.isdir(mkdir_name + "/dir" + str(check_count)):
           os.mkdir(mkdir_name + "/dir" + str(check_count))
           dir_name = "/dir" + str(check_count)
           return dir_name
       check_count += 1

#画像取得
def get_photos(timeline, dir_name):
   global image
   global image_number
   image_number = 0
   check_image = []
   for tweet in timeline['statuses']:
       try:
           media_list = tweet['extended_entities']['media']
           for media in media_list:
               image = media['media_url']
               if image in check_image:
                   continue
               with open(mkdir_name + dir_name + "/mei_image_" + str(image_number) + "_" + os.path.basename(image), 'wb') as f:
                   img = urllib.request.urlopen(image).read()
                   f.write(img)
               check_image.append(image)
               image_number += 1
       except KeyError:
           pass

# 実行するやつ
if __name__ == '__main__':
   dir_name = dir_check()
   all_list = []
   keyword = "#芽依撮"
   timeline = get_tweet(keyword)
   get_photos(timeline, dir_name)
   print("Complete")