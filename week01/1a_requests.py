#   使用requests库获取豆瓣影评

import requests

user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0"

header = {'user-agent':user_agent}

myurl = "https://movie.douban.com/top250?start=0"

response = requests.get(myurl,headers=header)

print(response.text)
print(f'返回码是：{response.status_code}')

