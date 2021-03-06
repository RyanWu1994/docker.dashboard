import json
import requests
import time
import pandas as pd
import os
import mysql.connector
from fake_useragent import UserAgent
from sqlalchemy import create_engine

#from collections import Counter

mydb = mysql.connector.connect(
  host = os.environ['MYSQL_HOST'],
  user = os.environ["MYSQL_USER"],
  password = os.environ['MYSQL_PASSWORD'],
  database = os.environ["MYSQL_DB"],
  connect_timeout = 1000,
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS `dashboard` (`id` INT NOT NULL AUTO_INCREMENT,`time` CHAR(50) NULL,`total` INT NULL DEFAULT NULL,PRIMARY KEY (`id`));")
mycursor.close()
mydb.commit()
mydb.close()

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

user = os.environ['MYSQL_USER']
passwd = os.environ['MYSQL_PASSWORD']
ip = str(os.environ['MYSQL_HOST'])+":"+str(os.environ['MYSQL_PORT'])
db_name = os.environ['MYSQL_DB']
table_name = os.environ['MYSQL_TABLE']

while True:
    result_list = GetApi()
    List_to_mysql(user,passwd,ip,db_name,table_name,result_list)
    time.sleep(15)