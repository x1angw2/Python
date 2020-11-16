#! /usr/bin/env python3
def bin(a):
    if a < 2:
        return a
    else:
        return bin(a%2)

