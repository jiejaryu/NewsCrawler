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

for tag in a_tags:
  titleList = titleList + [tag.string]
print(titleList)


# print news links
newsList = []

for tag in a_tags:
	newsList = newsList + [tag.get('href')]
print(newsList)
