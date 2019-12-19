import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com/"

req = requests.get(url).text

soup = BeautifulSoup(req, 'html.parser')
#################

selector = "#section_politics > div.com_list > div > ul > li > a > strong"



one = soup.select(selector)


for item in one :
   print(item.text)


# list_news = soup.select(selector)

# print(list_news)

# for item in list_news :
#    print(item.text)