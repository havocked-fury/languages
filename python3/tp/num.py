#!/usr/bin/python3

intval = 132
floatval = 2**(0.5)
complexval = 45+6j

hexaval = 0xAF
octaval = 0o154

for it in [intval,floatval,complexval,hexaval,octaval]:
    print(it)

del intval, floatval, complexval, hexaval, octaval
