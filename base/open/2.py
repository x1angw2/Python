#! /usr/bin/env python3

a = open("/Users/wezhon/dev/Python/base/open/duihua1",mode="r")
jia = open("/Users/wezhon/dev/Python/base/open/boy_*.txt",mode="a")
kefu = open("/Users/wezhon/dev/Python/base/open/girl_*.txt",mode="a")
jiayu_name = "小甲鱼"
kefu_name = "小客服"

for list_a in a:
    if jiayu_name in list_a:
        jia.write(list_a[5:])
    elif kefu_name in list_a:
        kefu.write(list_a[5:])
    else:
        print("本行数据为",list_a)

print("操作完成")


