
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/"
req = requests.get(url).text

soup = BeautifulSoup(req, 'html.parser')

#print(soup)

kospi=soup.select_one('#KOSPI_now')
print(kospi.text)