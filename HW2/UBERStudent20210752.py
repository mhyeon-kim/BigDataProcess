#!/usr/bin/python3

import sys
import datetime

try:
    readF = open(sys.argv[1])
    writeF = open(sys.argv[2], "wt")
    
    day = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    for line in readF:
        line = line.rstrip()
        info = line.split(",")
        dates = info[1].split("/")
        weekDay = day[datetime.date(int(dates[2]), int(dates[0]), int(dates[1])).weekday()]

        writeF.write(info[0] + "," + weekDay + " " + str(info[2]) + "," + str(info[3]) + "\n")


except FileNotFoundError:
    print("파일이 없습니다.")
finally:
    readF.close()
    writeF.close()
