import requests
from bs4 import BeautifulSoup

url = "https://www.naver.com/"
req = requests.get(url).text

soup = BeautifulSoup(req, 'html.parser')

# print(soup)


search = soup.select("#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a > span.ah_k")

# selector = "#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a > span.ah_k"

# search = soup.select_one(selector)




for item in search :
   print(item.text)

