# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 16:26:56 2022

@author: user
"""
import pymysql

dbsetting = {
    "host":"127.0.0.1",
    "port":3306,
    "user":"johnny75129",
    "password":"mj09250129",
    "db":"jobs",
    "charset":"utf8"
    
    }

conn = pymysql.connect(**dbsetting)


choice = input("請輸入需要的服務: 1.新增員工 2.新增工作 3.修改員工 4.查詢員工 5.查詢員工編號")

if choice == "1":
    print("您選擇新增員工!")
    name = input("請輸入員工姓名: ")
    sex = input("請輸入性別: (M/F)")
    mobile = input("請輸入電話: ")
    date = input("請輸入到職日: YYYY/MM/DD")
    
    sql = "insert into employee (name,sex,tel,assume) values ('{}','{}','{}','{}')".format(name,sex,mobile,date)
    
    
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    
    print("新增完成!")
if choice == "2":
    print("您選擇新增工作")
    items = input("請輸入工作項目: ")
    info = input("請輸入工作詳述: ")
    employeeid = input("請輸入員工編號: ")
    
    sql = "insert into works (items,info,employeeid) values ('{}','{}','{}')".format(items,info,employeeid)
    
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()  
    
    print("新增完成")

if choice == "3":
    print("修改員工!")
    
    sql = "select * from employee"
    
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()  
    result = cursor.fetchall()
    
    for row in result:
        print("員工編號: ",row[0])
        print("姓名: ",row[1])
        print("姓別: ",row[2])
        print("電話: ",row[3])
        print("*"*30)
        
    num = input("請輸入欲修改的員工編號: ")
    mobile = input("請輸入新電話: ")
    sex = input("請輸入新性別: ")
    
    sql = "update employee set tel='{}',sex='{}' where id='{}'".format(mobile,sex,num)
    
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()  
    print("修改完畢!")
    
if choice == "4":
    num = input("請輸入欲查詢的員工編號: ")
    sql = "select name,sex,tel,assume from employee where id='{}'".format(num)
    
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    result = cursor.fetchone()

    print("姓名: ",result[0])
    print("性別: ",result[1])
    print("電話: ",result[2])
    print("到職日期: ",result[3])
    
if choice == "5":
    num = input("請輸入欲查詢的員工編號: ")
    
    sql = "select employee.name,works.items,works.info from employee inner join works on employee.id='{}' ".format(num)
    
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    result = cursor.fetchone()
    
    print("員工姓名: ",result[0])
    print("工作項目: ",result[1])
    print("工作詳述: ",result[2])
    