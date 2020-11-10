#! /usr/bin/env python3
a = int(input("输入开始数:"))
b = int(input("输入结束数:"))
c = 0
while a <= b:
    c = a + c
    a += 1
#    print(a)
#    print(c)

print(c)
