#!/usr/bin/python3

inFile = open ("in.txt", 'r')

lines = inFile.readlines()

for it in range(0,len(lines)):
    if it%2==1 :
        print(lines[it].strip('\n'))

inFile.close()
