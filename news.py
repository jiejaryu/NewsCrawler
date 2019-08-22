import requests 
from bs4 import BeautifulSoup
import pandas as pd
 
 
url = 'https://news.google.com/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNR3QwTlRFU0JYcG9MVlJYS0FBUAE?hl=zh-TW&gl=TW&ceid=TW%3Azh-Hant'
r = requests.get(url)
web_content = r.text


soup = BeautifulSoup(web_content,'lxml')

a_tags = soup.find_all('a',class_='DY5T1d')

# print(a_tags)

titleList = []

# print news titles
for tag in a_tags:
  titleList = titleList + [tag.string]

print(titleList)


# titleList = [tag.text for tag in a_tags]
# print(titleList)
