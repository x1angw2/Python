#! /usr/bin/env python3
import time

print("这是一个求两个整数的最大公约数的小脚本")
def gcd(a,b):
    if (a % b) == 0:
        print(a,"和",b,"的最大公约数是：",b)
    else:
        return gcd(b,a%b)
time.sleep(1)
x = int(input("请输入第一个整数："))
y = int(input("请输入第二个整数："))
gcd(x,y)

