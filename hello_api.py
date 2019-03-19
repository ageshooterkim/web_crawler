# 한입에 웹 크로링  : 파이션 데이터 수십 자동화 한 방에 끝내기
# 9장 : 네이버 API 이용하기

import requests
from urllib.parse import urlparse

def get_api_result(keyword, display, start):
#블로그   url = "https://openapi.naver.com/v1/search/blog?query=" + keyword + "&display=" + str(display) + "&start=" + str(start)
   url = "https://openapi.naver.com/v1/search/news?query=" + keyword + "&display=" + str(display) + "&start=" + str(start)
   result = requests.get(urlparse(url).geturl(),
         headers={"X-Naver-Client-Id":"RgsCqASqeN4vPrBaph8q",
                  "X-Naver-Client-Secret":"J5vMdG_WhI"})
   return result.json()

def call_and_print(keyword, page):
    json_obj = get_api_result(keyword, 100, page)
    print(json_obj['display'], json_obj['start'], len(json_obj['items']))
    for item in json_obj['items']:
        title = item['title'].replace("<b>","").replace("</b>","")
#블로그        print(title + "@" + item['bloggername'] + "@" + item['link'] + "@" + item['postdate'])
        print(title + "@" + item['originallink'] + "@" + item['link'] + "@" + item['pubDate'])
        #print(item)

keyword = "구월동 맛집"
call_and_print(keyword, 1)
call_and_print(keyword, 101)
call_and_print(keyword, 201)
call_and_print(keyword, 301)
call_and_print(keyword, 401)
call_and_print(keyword, 501)