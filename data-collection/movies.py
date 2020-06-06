#!/usr/bin/env python
# coding: utf-8

# In[31]:


import requests
from datetime import timedelta, datetime
import json
import urllib
import pandas as pd
import numpy as np


# In[3]:


data = pd.read_csv("C:/Users/student/Downloads/Python/06_06/boxoffice.csv", encoding="ANSI")


# In[4]:


data


# In[28]:


movie_list = (data['movieCd'].unique())
url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key=49e6836be0a4a7e6d821f27658663e03&'
movie_info = []


# In[34]:


for i in movie_list:
    tmp_url = url + 'movieCd=' + str(i)
    request = requests.get(tmp_url)
    response = request.text
    tmp = json.loads(response)
    tmp = tmp.get('movieInfoResult').get('movieInfo')
    print(tmp)
    movieCd = tmp.get('movieCd')
    movieNm = tmp.get('movieNm')
    movieNmEn = tmp.get('movieNmEn')
    movieNmOg = tmp.get('movieNmOg')
    watchGradeNm = tmp.get('audits')[0].get('watchGradeNm')
    openDt = tmp.get('openDt')
    showTm = tmp.get('showTm')
    genreNm = tmp.get('genres')[0].get('genreNm')
    try:
        peopleNm = tmp.get('directors')[0].get('peopleNm')
    except IndexError:
        peopleNm = np.nan
    movie_info.append([movieCd,movieNm,movieNmEn,movieNmOg,watchGradeNm,openDt,showTm,genreNm,peopleNm])


# In[44]:


movies = pd.DataFrame(movie_info)
movies.columns=['영화 대표코드' , '영화명(국문)' , '영화명(영문)' , '영화명(원문)' , '관람등급' , '개봉연도' , 
                '상영시간' , '장르' , '감독명']
movies.to_excel("C:/Users/student/Downloads/Python/06_06/movies.xlsx", index=False)


# In[ ]:


movieCd,movieNm,movieNmEn,movieNmOg,watchGradeNm,openDt,showTm,genreNm,peopleNm


# In[33]:


type(np.nan)


# In[ ]:




