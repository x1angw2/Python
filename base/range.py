#! /usr/bin/env python3
a,b = 0,0
for i in range(100,-1,-1):
  a += b
  b += 1
print(a)


