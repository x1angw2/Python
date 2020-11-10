#! /usr/bin/env python3
for n in range(2, 2**15):
    for x in range(2, n):
        if n % x == 0:
            break
    else:
        # 循环中没有找到元素
        print(n, ' 是质数')
