# 한입에 웹 크로링  : 파이션 데이터 수십 자동화 한 방에 끝내기
# 10장 : 세계 곡물 가격 JSON 데이터 호출해서 엑셀로 차트 그리기

from urllib.request import urlopen
import json

def print_grain_from_to(from_date, to_date):
    url = "http://www.krei.re.kr:18181/chart/main_chart/index/kind/W/sdate/" + from_date + "/edate/" + to_date
    html = urlopen(url)
    json_objs = json.load(html)

    for item in json_objs:
        print(item['date'] + "@" + item['settlement'])
#전체        print(item)

from_date = "2010-01-01"
to_date = "2019-03-07"
print_grain_from_to(from_date, to_date)
