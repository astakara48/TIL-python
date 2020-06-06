import requests
from datetime import timedelta, datetime
import json
import urllib
import pandas as pd


# url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?'
# key = '49e6836be0a4a7e6d821f27658663e03'
# targetDt = 20200531
# movie_list=[]
# for i in range(0, 14, 7):
#     time = datetime(2020, 5, 31) - timedelta(i)
#     day = str(time.day)
#     month = str(time.month)
#     year = str(time.year)
#     if len(month) == 1:
#         month = '0'+month
#     date = year+month+day

#     BoxOfficeURL = url+'key='+key+'&targetDt='+date+'&weekGb=0'
#     response = requests.get(BoxOfficeURL)
#     movie_dict = json.loads(response.text)

#     tmp = movie_dict.get('boxOfficeResult').get('weeklyBoxOfficeList')
#     for num in tmp:
#         tmp_list = [num.get('movieCd'),num.get('movieNm'),num.get('audiAcc')]
    