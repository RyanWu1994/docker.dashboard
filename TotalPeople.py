#!/usr/bin/env python
# coding: utf-8

import json
import requests
import time
import pandas as pd
import os

from fake_useragent import UserAgent
from sqlalchemy import create_engine
from collections import Counter

ua = UserAgent()
headers = {"User-Agent":ua.random}
def GetApi():
    url = "https://scapi.zanstartv.com/v1/pcnt/?appName=solar&Room="
    res = requests.get(url,headers=headers)
    api = json.loads(res.text)
    result = []
    localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    total = int(api["total"])
    result.append({"time": localtime,"total" : total})
    return result

def List_to_mysql(user,passwd,ip,db_name,table_name,result_list):
    engine = create_engine('mysql+mysqlconnector://'+ user +':'+ passwd +'@'+ip+'/'+ db_name +'?charset=utf8', encoding='utf-8')
    con = engine.connect()
    for item in result_list:
        df = pd.DataFrame(item, index=[0])
        try:
            df.to_sql(name=table_name,con=con,if_exists='append',index=False)
        except Exception as e:
            if 'PRIMARY' in str(e):
                print("error: ", e)
                pass
    con.close() 
    engine.dispose()

user = "ryan"
passwd = "Aa123456"
ip = "0.0.0.0:3306"
db_name = "solar"
table_name = "dashboard"

result_list = GetApi()
List_to_mysql(user,passwd,ip,db_name,table_name,result_list)
