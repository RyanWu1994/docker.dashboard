import os
import mysql.connector

def init_1():
    mydb = mysql.connector.connect(
    host = "192.168.0.10",
    user = "root",
    password = "1qaz@WSX",
    connect_timeout = 1000,
    )
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS solar;")
    mycursor.execute("GRANT ALL PRIVILEGES ON *.* TO 'ryan'@'%';")
    mycursor.execute("FLUSH PRIVILEGES;")
    mycursor.close()
    mydb.commit()
    mydb.close()

def init_2():
    mydb = mysql.connector.connect(
    host = "192.168.0.10",
    user = "root",
    password = "1qaz@WSX",
    database = "solar",
    connect_timeout = 1000,
    )
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE IF NOT EXISTS `dashboard` (`id` INT NOT NULL AUTO_INCREMENT,`time` CHAR(50) NULL,`total` INT NULL DEFAULT NULL,PRIMARY KEY (`id`));")
    mycursor.close()
    mydb.commit()
    mydb.close()

init_1()
init_2()