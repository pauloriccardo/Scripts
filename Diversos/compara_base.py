import sys, os
from datetime import datetime

day = datetime.now().strftime("%Y%m%d")
path = os.path.dirname(os.path.abspath(__file__))
file1 = os.path.join(path + '\\bkp', '10.3.148.7_' + day + ".txt")
file2 = os.path.join(path + '\\bkp', '10.3.148.8_' + day + ".txt")
file3 = os.path.join(path + '\\bkp', 'Inconsistencias_' + day + ".txt")

arquivo1 = open(file1, 'r')
arquivo2 = open(file2, 'r')
resposta = open(file3, 'w')

temp1 = arquivo1.readlines()
temp2 = arquivo2.readlines()


#if len(temp1) != len(temp2):
for line in temp1:
    if line not in temp2:
        resposta.write(line)
    continue


arquivo1.close()
arquivo2.close()
resposta.close()