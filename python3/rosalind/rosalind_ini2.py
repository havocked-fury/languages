#!/usr/bin/python3

inFile = open("in.txt", 'r')

inData = list(map(int, inFile.read().split()))

a = inData[0]
b = inData[1]

print(a**2+b**2)

inFile.close()

