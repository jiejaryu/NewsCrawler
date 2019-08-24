import requests 
from bs4 import BeautifulSoup
import pandas as pd
 
# get website content
url = 'https://news.google.com/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNR3QwTlRFU0JYcG9MVlJYS0FBUAE?hl=zh-TW&gl=TW&ceid=TW%3Azh-Hant'
r = requests.get(url)
web_content = r.text

soup = BeautifulSoup(web_content,'lxml')

a_tags = soup.find_all('a',class_='DY5T1d')


# print news titles
titleList = []

for title in a_tags:
  titleList = titleList + [title.string]
print(titleList)


# get news links in html
linkList = []

for link in a_tags:
	linkList = linkList + [link.get('href')]
#print(linkList)


# fix links to normal url format
rawLink = []

for i in linkList:
	rawLink = rawLink + [i.replace('.','https://news.google.com',1)]

print(rawLink)