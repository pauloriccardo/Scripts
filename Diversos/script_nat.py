import paramiko
import time
 
ssh = paramiko.SSHClient()


 
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
 
ssh.connect('localhost', username='user', password='pass', look_for_keys=False)
 
#stdin, stdout, stderr = ssh.exec_command('cmd')
#print stdout.readlines()

def exec_cmd(self,cmd):

    if stderr.channel.recv_exit_status() != 0:
        print(stderr.read())
    else:
        print(stdout.read())

y = 101

for x in range(1,100):
    exec_cmd('NAT64_ADD 10.150.1.' + str(x) + ' ' + 'fda0::11a:0:0:642b:d' + str(y)) # NAT64_ADD
    y += 1
    time.sleep ( 1 )

y = 101

for x in range(1,100):
    exec_cmd('NAT64_MOD fda0::11a:0:0:642b:d' + str(y) + ' ' + 'fda0::11a:0:0:642b:d' + str(x)) # NAT64_MOD
    y += 1
    time.sleep ( 3 )


    import paramiko


class SSH:
    def __init__(self):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect('10.55.45.144', username='suporte', password='suporte', look_for_keys=False)

    def exec_cmd(self,cmd):
        stdin,stdout,stderr = self.ssh.exec_command(cmd)
        if stderr.channel.recv_exit_status() != 0:
            print (stderr.read())
        else:
            print (stdout.read())

if __name__ == '__main__':

    y = 11

    for x in range(1,10):
        ssh = SSH()
        ssh.exec_cmd('NAT64_ADD 10.150.1.' + str(x) + ' ' + 'fda0::11a:0:0:642b:d' + str(y))
        y += 1
