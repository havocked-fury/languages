#!/usr/bin/python3

# This gave wrong answer

fileData = open("in.txt", 'r')

data = fileData.read()

data.strip('\n')

words = data.split(' ')

dic = dict() 

for it in words:
    if it not in dic: 
        dic[it]=1
    else:
        dic[it]+=1

for it in dic.items():
    print(it[0].strip('\n'), it[1])

fileData.close()

