#!/usr/bin/env python

import paramiko, os
from datetime import datetime, timedelta

host = 'host'
user = 'user'
pw = 'password'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=host, username=user, password=pw, look_for_keys=False)
stdin,stdout,stderr = ssh.exec_command('show run | b nat64 v6v4 static' )

if stderr.channel.recv_exit_status() != 0:
   saida = stderr.read().decode('ascii')
else:
   saida = stdout.read().decode('ascii')

ssh.close()

day = datetime.now().strftime("%d-%m-%y")
hour = datetime.now().strftime("%H%M")

path = os.path.dirname(os.path.abspath(__file__))
path_bkp = os.path.join(path + '/bkp')

file = os.path.join(path_bkp , day + '_' + hour + ".txt")

arquivo = open(file, 'w')
arquivo.writelines(saida)
arquivo.close()