import paramiko, getpass, os
from datetime import datetime

host = input('IP: ')
user = input('User: ')
pw = getpass.getpass("Password: ")

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=host, username=user, password=pw, look_for_keys=False)
stdin,stdout,stderr = ssh.exec_command('show nat64 translations ' )

if stderr.channel.recv_exit_status() != 0:
    print(stderr.read())
else:
   saida = stdout.read().decode('ascii')
   saida = saida.split(None)

ssh.close()

day = datetime.now().strftime("%Y%m%d")
path = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(path + '\\bkp', host + '_' + day + ".txt")
linhas = ''
ipv4 = '10.'
ipv6 = 'fda'
sair = 'tcp'

arquivo = open(file, 'w')

for i in range(1,len(saida)):
    if ipv4 in saida[i]:
        linhas += saida[i] + ','
    elif ipv6 in saida[i]:
        linhas += saida[i] + '\n'
    elif sair in saida[i]:
        break

arquivo.writelines(linhas)
arquivo.close()