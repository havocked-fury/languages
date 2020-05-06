#!/usr/bin/python3

def pow(b,n):
    for x in range(n):
        b*=b
    return b

b = int(input())
n = int(input())
print(pow(b,n))
