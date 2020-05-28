import paramiko
import time

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

    def obter_ipv4(self):
        global ipv4, ipv6
        self.exec_cmd('show run | i ' + ipv6old )

        if self.saida == "b''":
            print('IPv6  ' + ipv6old + ' nao encontrado ' )
        else:
            partes = self.saida.split(None)
            ipv6 = partes[3]
            ipv4 = partes[4]
            ipv4 = ipv4[:-5]

    def close_ssh(self):
        self.ssh.close()

if __name__ == '__main__':

    y = 1001
    ipv4 = ''
    ipv6 = ''

    for x in range(1,2):
        ipv6old = 'FDA2::23:1C:6400:8080:' + str(y)
        ipv6new = 'FDA2::ff:1C:6400:8080:' + str(y)
        ssh = SSH()
        ssh.obter_ipv4()
        if ipv4 != '':
            ssh = SSH()
            ssh.exec_cmd('conf t \n'  + ' no nat64 v6v4 static ' + ipv6 + ' ' + ipv4 + ' forced\n')
            time.sleep(1)
            ssh = SSH()
            ssh.exec_cmd('conf t \n' + ' nat64 v6v4 static ' + ipv6new + ' ' + ipv4 +  '\n'  )
            time.sleep(1)
        ssh.close_ssh()
        y += 1
