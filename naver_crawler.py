import urllib.request
import bs4

url = "https://www.naver.com/"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")

top_right = bs_obj.find("ul", {"id":"PM_ID_serviceNavi"})
print(top_right)

lis = top_right.findAll("li")

for  li in lis:
    a_tag = li.find("a")
    span = a_tag.find("span", {"class":"an_txt"})
    print(span.text)
