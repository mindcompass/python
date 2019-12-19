import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com/"

req = requests.get(url).text

soup = BeautifulSoup(req, 'html.parser')
#################

selector = ".ranking_contents > ul > li:nth-child(1) > a"

one = soup.select_one(selector)
print(one.text)
# list_news = soup.select(selector)

# print(list_news)

# for item in list_news :
#    print(item.text)