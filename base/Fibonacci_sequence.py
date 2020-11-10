#! /usr/bin/env python3

a=0
b=1
c=0

while b<1000:
    c += 1
    print("第",c,"次","斐波那契数列为：",b)
    a,b=b,a+b
    
