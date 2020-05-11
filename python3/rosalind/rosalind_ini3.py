#!/usr/bin/python3

inFile = open ("in.txt", 'r')

string = inFile.readline ()

inData = list(map(int, inFile.readline().split() ) )

print(string[inData[0]:(inData[1]+1)], string[inData[2]:(inData[3]+1)])
