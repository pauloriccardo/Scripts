#! /usr/bin/env python

# Conectando ao banco de dados MYSQL
import sys
import MySQLdb 
import pymssql
import cx_Oracle
import ConfigParser
import os

config = ConfigParser.ConfigParser()
config.read("export.conf")

banco = config.get("DB", "banco")
host = config.get("DB", "host")
user = config.get("DB", "user")
pw = config.get("DB", "pass")

if banco == 'mssql':
    db = pymssql.connect(host=host, user=user, password=pw, database='database name')
elif banco == 'mysql':
    db = MySQLdb.connect(host=host, user=user, passwd=pw, db='database name')
elif banco == 'oracle':
    db = cx_Oracle.connect( user, pw, dsn=host )
else:
    print("Banco invalido")
    

with open("query/E450.sql") as sql:
    query = sql.read()   


cursor = db.cursor()

cursor.execute(query) # Consulta ao banco


with open('CSV/E450.csv' ,'w') as csv: # Criacao e abertura de arquivo
   # csv.write("model,meter,total,percent\n") # Escrevendo no arquivo 

    for linha in cursor.fetchall():
        csv.write("%s,%s,%s,%s\n" % (linha[0],linha[1],int(linha[2]),int(linha[3])))