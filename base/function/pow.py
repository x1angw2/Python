#! /usr/bin/env python3

def power(x,y):
    def pow(a,b):
        print(a**b)
    pow(x,y)
x = int(input("请输入底数："))
y = int(input("请输入幂："))
power(x,y)
