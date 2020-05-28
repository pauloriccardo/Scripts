#! /usr/bin/env python
import MySQLdb
import datetime

con = MySQLdb.connect(host='host', user='user', passwd='pass', db='name_database')

cursor = con.cursor()

dt = (datetime.date.today() - datetime.timedelta(days = 1)).strftime("%d/%m/%Y")

with open('E450.csv') as csv: # abertura de arquivo

    for lines in csv:
        line = lines.split(',')
        model = line[0]
        meter = line[1]
        total = line[2]
        percent = line[3]
        query = "INSERT INTO medidor VALUES(%s,%s,%s,%s,%s)"
        args = (dt,model, meter, total, percent)
        cursor.execute(query, args)
con.commit()