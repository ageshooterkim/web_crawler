import requests
from bs4 import BeautifulSoup

url = "https://www.kshop.co.kr/category/70000138"
result = requests.get(url)

bs_obj = BeautifulSoup(result.content, "html.parser")
print(bs_obj)

