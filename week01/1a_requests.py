#   使用requests库获取豆瓣影评

import requests

user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"

header = {'user-agent':user_agent}

myurl = "https://movie.douban.com/top250?start=0"

response = requests.get(myurl,headers=header)

print(response.text)
print(f'返回码是：{response.status_code}')

