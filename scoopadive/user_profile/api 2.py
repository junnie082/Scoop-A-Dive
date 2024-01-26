# views.py
import json

from django.shortcuts import render
import requests
from urllib.parse import unquote


encodedKey = '%2FnoWZKULUcFiE2qPjFRA8lMQzCcatH%2B16NIEYuEzAIpdSqPKDt0FsNoIX%2B5UCm1nC78fOqVkIZJya7IVgSq67g%3D%3D'
decodedKey = '/noWZKULUcFiE2qPjFRA8lMQzCcatH+16NIEYuEzAIpdSqPKDt0FsNoIX+5UCm1nC78fOqVkIZJya7IVgSq67g=='
def get_majors():
    print("get_majors")
    url = 'http://api.data.go.kr/openapi/tn_pubr_public_univ_major_api'
    params = {'serviceKey': encodedKey, 'pageNo': '1', 'numOfRows': '100', 'type': 'xml', 'YR': '2022', 'CTPV_CD': '41',
              'CTPV_NM': '경기도', 'SGG_CD': '610', 'SGG_NM': '광주시', 'SCHL_NM': 'ICT폴리텍대학', 'SCHL_SE_NM': '기능대학',
              'LSSN_TERM': '2년', 'DEG_CRSE_CRS_NM': '전문학사', 'DAN_CRS_NM': '주간', 'SCSBJT_STTS_NM': '기존',
              'SCSBJT_NM': '기타(소속학과없음)', 'SCSBJT_CD_NM': 'Z99999999999', 'STD_CLSF_AFIL_CD': 'A99999',
              'UNIV_ONESLF_AFIL_NM': '인문사회', 'COLLEGE_NM': '단과대구분없음', 'SCHL_SCSBJT_PROP_NM': '일반과정', 'MAIN_SUBJ_NM': '',
              'MTCLTN_FXNO_CNT': '0', 'GRA_CNT': '0', 'RELAT_CR_NM': '', 'MDFCN_YMD': '2014-03-28',
              'CRTR_YMD': '2022-12-20', 'instt_code': 'B340014', 'instt_nm': '한국대학교육협의회'}
    print("api_key_decode: " + encodedKey)
    res = requests.get(url, params=params)
    print("res: " + str(res.content))
    # if res.status_code == 200:
    #     try:
    #         majors = res.json()
    #         print("majors:", majors)
    #     except json.JSONDecodeError as e:
    #         print("Error decoding JSON:", e)
    #         print("Response content:", res.text)
    # else:
    #     print("API request failed with status code:", res.status_code)



