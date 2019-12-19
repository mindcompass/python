import requests
from bs4 import BeautifulSoup

url = "https://movie.naver.com/movie/bi/mi/point.nhn?code=187940"

req =requests.get(url).text
