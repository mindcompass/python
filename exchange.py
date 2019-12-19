import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/marketindex/"

req =requests.get(url).text
soup =BeautifulSoup(req, 'html.parser') # json같은 파일도 가능함

exchange =soup.select_one("#exchangeList > li.on > a.head.usd > div > span.value")

print(exchange.text)

