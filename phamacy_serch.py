# 한입에 웹 크로링  : 파이션 데이터 수십 자동화 한 방에 끝내기
# 11장 : 공공 데이타 API 이용하기 (인천의 심야 약국 찾기)

from urllib.parse import quote
import requests
import bs4

endpoint = "http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire?"
serviceKey = "Te%2BlyZEiFaOrmBRoX7rpT7%2F19C4kAyMMyBueBuvh6F%2BPG5%2BJTeNv%2FS%2BmrBT06CAkBlLlqr8VxhGNHuPN6AKxVA%3D%3D"

Q0 = quote("인천광역시")
Q1 = quote("남동구")
ORD = "NAME"

# QT : 1(월), 2(화), 3(수), 4(목), 5(금), 6(토), 7(일), 8(공휴일)
QT = "8"
# day_of_the_week_dutytime : 월(dutytime1c), 화(dutytime2c) ..... 일(dutytime7c), 공휴일(dutytime8c)
day_of_the_week_dutytime = "dutytime8c"

pageNo ="1"
startPage = "1"
numOfRows = "5000"
paramset =  "serviceKey=" + serviceKey + "&" + "Q0=" + Q0 + "&" + "Q1=" + Q1 + "&" + "QT=" + QT + "&" + "ORD=" + ORD + "&" + "pageNo=" + pageNo + "&" + "startPage=" + startPage + "&" + "numOfRows=" + numOfRows

url = endpoint + paramset
result = requests.get(url)
bs_obj = bs4.BeautifulSoup(result.content, "html.parser")
items = bs_obj.findAll("item")

print(url)
print(items[0])
count = 0
for item in items:
    dutyaddr_item = item.find("dutyaddr")
    dutyname_item = item.find("dutyname")
    dutytel1_item = item.find("dutytel1")
    tagged_item = item.find(day_of_the_week_dutytime)

    if (dutyname_item != None) :
        dutyaddr_item = item.find("dutyaddr")
    else:
        dutyaddr_item = ""

    if (dutyname_item != None) :
        dutyname_item = item.find("dutyname")
    else:
        dutyname_item = ""

    if (dutytel1_item != None) :
        dutytel1_item = item.find("dutytel1")
    else:
        dutytel1_item = ""

    if (tagged_item != None) :
        tagged_item = item.find(day_of_the_week_dutytime)
    else:
        tagged_item.text = "1300"

    close_time = int(tagged_item.text)
    if (tagged_item != None):
        if(close_time > 2100):
            count += 1
            print(dutyaddr_item.text, "|", dutyname_item.text, "|", dutytel1_item.text, "|", close_time)

print("공휴일 오후 9시 이후까지 하는 약국의 수 : " + str(count))
