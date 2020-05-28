import paramiko
import time
import sys, os
from datetime import datetime

ipv6 = ''

class SSH:
    def __init__(self):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect('host', username='user', password='pass', look_for_keys=False)
        self.saida = ''

    def exec_cmd(self,cmd):
        stdin,stdout,stderr = self.ssh.exec_command(cmd)
        if stderr.channel.recv_exit_status() != 0:
            print (stderr.read())
        else:
            self.saida = str(stdout.read())
            print(self.saida)

    def obter_ipv4(self,ipv6new):
        global ipv4, ipv6
        self.exec_cmd('show run | i ' + ipv6new[-9:] )

        if self.saida == "b''":
            print('IPv6  ' + ipv6new[-9:] + ' nao encontrado ' )
        else:
            partes = self.saida.split(None)
            ipv6 = partes[3]
#            ipv4 = partes[4]
#            ipv4 = ipv4[:-5]

    def close_ssh(self):
        self.ssh.close()


    def show_all(self):
        global ipv4, ipv6
        self.exec_cmd('show nat64 translations' )

        if self.saida == "b''":
            print('Sem retorno' )
        else:
            partes = self.saida.split(None)
            ipv6 = partes[3]
            ipv4 = partes[4]
            ipv4 = ipv4[:-5]
            print(partes)

if __name__ == '__main__':

    day = datetime.now().strftime("%Y%m%d")
    path = os.path.dirname(os.path.abspath(__file__))
    nome_file = os.path.join(path + '\\bkp', 'Inconsistencias_' + day + ".txt")
    arquivo = open(nome_file, 'r')
    temp = arquivo.readlines()

#    cisco = SSH()
#    cisco.show_all()

    for line in temp:
        linha = line.split(',')
        ipv4 = linha[0]
        ipv6new = linha[1]
        ssh = SSH()
        ssh.obter_ipv4(ipv6new)
        if ipv4 != '':
            ssh = SSH()
            ssh.exec_cmd('conf t \n' + 'no nat64 v6v4 static ' + ipv6 + ' ' + ipv4 + ' forced\n' )
            time.sleep(1)
            ssh = SSH()
            ssh.exec_cmd('conf t \n' + 'nat64 v6v4 static ' + ipv6new + ' ' + ipv4 +  '\n'  )
            time.sleep(1)
        ssh.close_ssh()