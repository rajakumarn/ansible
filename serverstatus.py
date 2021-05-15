#!C:\Python27\python.exe
import os
import sys
import paramiko
import socket
vowel=0
count=0
fname = raw_input("Enter the file with extention and path:  ")
usrname = raw_input("Enter the login ID:  ")
pword = raw_input("Enter the login password:  ")
with open(fname, 'r') as f:
    for line in f:
        count += 1
name = open(fname, 'r')
server=name.readlines()
while vowel != count:
    try:
        name=server[vowel][:-1]
        print(name)
        vowel+=1
        nbytes = 8092
        hostname = r"{}".format(name)
        port = 22
        username = usrname
#        password = pword
#        command = 'uptime'
#        command1 = 'nslookup %s | tail -2 | cut -c 10-22' % (hostname)
        command2 = 'free -lm | grep -E Mem | cut -c 1-22'
        client = paramiko.Transport(hostname, port)
#        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(username=username, password=password)
        stdout_data = []
        stderr_data = []
        session = client.open_channel(kind='session')         
        session.exec_command(command1)       
        while True:
             if session.recv_ready():
                   stdout_data.append(session.recv(nbytes))
                   print(''.join(stdout_data))
             if session.recv_stderr_ready():
                   stderr_data.append(session.recv_stderr(nbytes))
             if session.exit_status_ready():
                   break
             print('exit status: ', session.recv_exit_status())
             print(''.join(stdout_data))
             print(''.join(stderr_data))
             session.close()
             client.close()
    except paramiko.ssh_exception.SSHException as e:
        print("Server Not Rechable:",e)
        continue
