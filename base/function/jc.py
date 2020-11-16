#! /usr/bin/env python3
b = 1
if a > 0:
    def jc(a):
        b = a * b 
        a -= 1
        return jc(a)

    c = int(input())
    jc(c)
    
