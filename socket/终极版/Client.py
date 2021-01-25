import json
import struct
from socket import *


c = socket(AF_INET,SOCK_STREAM)
c.connect(('192.168.50.189',8019))

while True:
    cmd = input('请输入需要执行的命令:').strip()
    if len(cmd) == 0:
        continue
    c.send(cmd.encode('utf-8'))

    # 1) 先收固定长度的头信息
    header_size = c.recv(4)
    header_len = struct.unpack('i',header_size)[0]
    # 2) 接收头信息,并解析
    json_str_bytes = c.recv(header_len)
    json_str = json_str_bytes.decode('utf-8')
    header_dic = json.loads(json_str)
    print(header_dic)
    total_size = header_dic['total_size']

    # 2) 再根据的到头信息得到整理数据的大小
    recv_size = 0
    while recv_size < total_size:
        recv_data = c.recv(1024)
        recv_size += len(recv_data)
        #cmd_res += res_data
        print(recv_data.decode('utf-8'),end='')
    else:
        print()
