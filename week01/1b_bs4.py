# 使用BeautifulSoup解析网页

import requests
from bs4 import BeautifulSoup as bs



user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"

header = {'user-agent':user_agent}

myurl = 'https://movie.douban.com/top250'

response = requests.get(myurl,headers=header)

bs_info = bs(response.text,'html.parser') #用html.pares方式解析

# Python 中使用for in 形式的循环，Python使用缩进来做语句分隔
for tags in bs_info.find_all('div',attrs={'class':'hd'}):
    for atag in tags.find_all('a',):
        print(atag.get('href'))
        #获取所有链接
        print(atag.find('span',).text)
        #获取电影名字

