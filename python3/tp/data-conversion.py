#!/usr/bin/python3

# This program doesn't run
# Some types can't be casted into others
# Even with python abstractions

def printint(x):
    print(int(x,10))

def printfloat(x):
    print(float(x))

def printcomplex(x):
    print(complex(x))

def printstr(x):
    print(str(x))

def printrepr(x):
    print(repr(x))

def printlist(x):
    print(list(x))

def printset(x):
    print(set(x))

intval = 123
floatval = 314.15
complexval = 21+4j
strval = "String"
listval = [intval,floatval,complexval,strval]

#printfloat(complexval) invalid
printrepr(intval)
printrepr(listval)
printint(listval)
