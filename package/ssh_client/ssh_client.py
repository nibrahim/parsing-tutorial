# Exercise 17 and 18 

import paramiko
import subprocess

class CiscoClient(object):
    def __init__(self, name, host):
        self.user, self.host = name, host

    def execute_command(self, cmd):
        cmd = ["/usr/bin/ssh","{}@{}".format(self.user, self.host), cmd]
        p = subprocess.Popen(cmd, stdout = subprocess.PIPE)
        p.wait()
        return p.stdout.read().strip()

class CiscoClient2(object):
    def __init__(self, name, host):
        self.user, self.host = name, host
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(host,
                            username=name,
                            key_filename ="/home/noufal/.ssh/id_rsa")
    
    def execute_command(self, cmd):
        i,o,e = self.client.exec_command(cmd)
        return o.read()

        
# import os
# print os.getpid()
# s = CiscoClient2('noufal', 'noufalibrahim.name')
# for i in range(20):
#     print s.execute_command("uptime")

# subprocess  0.47s user 0.13s system 1% cpu 43.831 total
# paramiko  0.38s user 0.03s system 4% cpu 9.739 total



    
