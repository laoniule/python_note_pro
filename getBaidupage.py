from bs4 import BeautifulSoup
import requests

res=requests.get('https://www.sohu.com')

localBaidu=BeautifulSoup(res.text,'lxml')

type(localBaidu)
playFile=open('./baidu.html','wb','utf-8')


for chunk in localBaidu.iter_content(100000):
        playFile.write(chunk)

playFile.close()


