#!/usr/bin/python3

iterator = 1
lim = int(input())

while iterator <= lim:
    print(iterator)
    iterator += 1

print("\n\n")

#while lim -= 1: invalid syntax
#    print(lim)

lim = int(input())

for it in range(lim):
    print(it)

# break and continue exist
