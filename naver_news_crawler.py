import urllib.request
import bs4

url = "https://news.naver.com"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")

newsnow_txarea = bs_obj.find("ul", {"class":"newsnow_txarea"})
lis = newsnow_txarea.findAll("li")

for li in lis:
    strong = li.find("strong")
    print(strong.text)

print("---------------------------------------------------")
newsnow_txarea = bs_obj.find("ul", {"id": "text_today_main_news_428288"})
lis2 = newsnow_txarea.findAll("li")

for li in lis2:
    strong = li.find("strong")
    print(strong.text)