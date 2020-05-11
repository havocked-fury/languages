#!/usr/bin/python3

inFile = open ("in.txt", 'r')

inData = list(map(int, inFile.readline().split() ) )
a = inData[0]
b = inData[1]

ans = 0

for it in range(a,b):
    if(it%2==1):
        ans += it

print(ans)
