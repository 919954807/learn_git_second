import requests
from bs4 import BeautifulSoup as bs

#Python使用def定义函数，myurl是函数的参数
def get_url_name(myurl):
    user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"
    
    header = {'user-agent':user_agent}
    response = requests.get(myurl,headers=header)
    bs_info = bs(response.text,'html.parser')

    #Python中使用for in 形式的循环
    for tags in bs_info.find_all('div',attrs={'class':'hd'}):
        for atag in tags.find_all('a',):
            #获取所有链接
            print(atag.get('href'))
            #获取电影名字
            print(atag.find('span',).text)

#生成包含所有页面的元组，推导式一行
urls = tuple(f'https://movie.douban.com/top250?start={page*25}&filter=' for page in range(10)) 

#展开写法
a=[]
for page in range(10):
    pages = f'https://movie.douban.com/top250?start={page*25}&filter='
    a.append(pages)
tuple(a)
print(a)    

print(urls)

#控制请求的频率，引入time模块
from time import sleep

sleep(10)

for page in urls:
    get_url_name(page)
    sleep(5)