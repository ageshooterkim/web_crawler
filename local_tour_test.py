# 한입에 웹 크로링  : 파이션 데이터 수십 자동화 한 방에 끝내기
# 11장 : 공공 데이타 API 이용하기

import requests
import bs4

endpoint = "http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaBasedList?"
serviceKey = "Te%2BlyZEiFaOrmBRoX7rpT7%2F19C4kAyMMyBueBuvh6F%2BPG5%2BJTeNv%2FS%2BmrBT06CAkBlLlqr8VxhGNHuPN6AKxVA%3D%3D"

numOfRows = "10"
pageSize = "1"
pageNo = "1"
MobileOS = "ETC"
MobileApp = "AppTest"
arrange = "A"
contentTypeId ="15"
areaCode = "1"
sigungucode = "4"
listYN ="Y"

paramset = "serviceKey=" + serviceKey + "&" + "numOfRows=" + numOfRows + "&" + "pageSize=" + pageSize + "&" + "pageNo=" + pageNo + "&" + "MobileOS=" + MobileOS + "&" + "MobileApp=" + MobileApp + "&" + "arrange=" + arrange + "&" + "contentTypeId=" + contentTypeId + "&" + "areaCode=" + areaCode + \
          "&" + "sigungucode=" + sigungucode + "&" + "listYN=" + listYN

url = endpoint + paramset
print(url)
result = requests.get(url)
bs_obj = bs4.BeautifulSoup(result.content, "html.parser")
print(bs_obj.findAll("title"))
