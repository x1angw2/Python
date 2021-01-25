import subprocess
import struct
from socket import *

s = socket(AF_INET,SOCK_STREAM)
s.bind(('192.168.50.189',8019))
s.listen(5)

# 循环
while True:
    # 从半链接池中取出一个链接请求,建立双向链接并拿到链接对象
    conn,client_addr = s.accept()

    # 拿到链接对象,开始通讯循环
    while True:
        try:
            # 一般命令的字符不多
            cmd = conn.recv(1024)
            if len(cmd) == 0:
                break
            # 调用subprocess模块执行命令
            obj = subprocess.Popen(cmd.decode('utf-8'),
                                 shell = True,
                                 stdout = subprocess.PIPE,
                                 stderr = subprocess.PIPE
                                 )

            stdout = obj.stdout.read()
            stderr = obj.stderr.read()
            # 得到需要发送的数据总大小
            total_size = len(stdout) + len(stderr)
            
            # 1) 先发头信息
            header = struct.pack('i',total_size)
            conn.send(header)


            # 2) 再发数据
            conn.send(stdout + stderr)
        except Exception:
            break
    conn.close()
