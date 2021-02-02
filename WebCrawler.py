import requests
from bs4 import BeautifulSoup

# 要爬的網址
url = "https://www.ptt.cc/bbs/hotboards.html"

# 取得網頁內容，回傳一個物件
request = requests.get(url)

# 網頁原始碼
source = request.text

# 建立html解析器
soup = BeautifulSoup(source,"html.parser")

# 抓取每個div class="board-name"的元素，回傳一個list
nameElements = soup.find_all("div", class_="board-name")

# 將元素中的文字部分取出，存成list
names = [element.text for element in nameElements]

# 抓取每個div class="board-nuser"的元素，回傳一個list
popularityElements = soup.find_all("div", class_="board-nuser")

# 取出文字部分並轉整數(因為人氣是用整數表示)
popularity = [int(element.text) for element in popularityElements]

# 使用zip()可將兩個list組合成一個，如果兩者大小不同，則以較短的為主
for name, pop in zip(names, popularity):
    print(name, pop)
