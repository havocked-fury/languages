#!/usr/bin/python3

import time
import calendar

ticks = time.time()
print("Ticks: %f" % ( ticks) )

local = time.localtime(ticks)
print("Local time : ", local)
print("Formatted time: ", time.asctime(local))

cal = calendar.month(2019,5)
print(cal)
