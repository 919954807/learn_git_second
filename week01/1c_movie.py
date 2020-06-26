import requests
import lxml.etree

#抓取页面详细信息

#电影详细页面
url='https://movie.douban.com/subject/1292052/'

user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"

#声明为字典使用字典的语法赋值
header = {}
header['user-agent'] = user_agent
response = requests.get(url,headers=header)

#xml化处理
selector = lxml.etree.HTML(response.text)

#电影名称+斜杠text
file_name = selector.xpath('//*[@id="content"]/h1/span[1]/text()')
print(f'电影名称：{file_name}')

#上映日期
plan_date = selector.xpath('//*[@id="info"]/span[10]/text()')
print(f'上映日期：{plan_date}')

#评分
rating = selector.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')
print(f'评分：{rating}')

mylist = [file_name,plan_date,rating]

import pandas as pd
movie1 = pd.DataFrame(data=mylist)

#windows需要使用gbk字符集
movie1.to_csv('./week01/movie1.csv',encoding='utf8',index=False,header=False)