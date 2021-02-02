import requests
import re
from bs4 import BeautifulSoup

url = "http://www.stockq.org/"
request = requests.get(url)

soup = BeautifulSoup(request.text, "html.parser")

# 總共有三個table存在tables裡
tables = soup.find_all('table', class_='marketdatatable')

# 從每個table中取出該class裡第二個超連結(第一個為xx股市指數行情，第二個就是股市名稱)
for table in tables:
    names = table.find_all('a')[1:]
    for name in names:
        print(name.text)