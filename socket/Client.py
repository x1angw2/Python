import socket 
import os 
import time

ip = '192.168.50.189'
port = 8019

c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect((ip,port))

# 通讯循环
while True:
    msg = input('echo some text:').strip()
    if len(msg) == 0:
        continue
    c.send(msg.encode('utf-8'))
    s_res = c.recv(1024)
    print(s_res.decode('utf-8'))
c.close()
