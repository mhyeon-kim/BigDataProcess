#!/usr/bin/python3

import sys
import datetime

try:
    readF = open(sys.argv[1])
    writeF = open(sys.argv[2], "wt")
    
    dic = dict()
    data = []
    day = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    for line in readF:
        line = line.rstrip()
        info = line.split(",")
        dates = info[1].split("/")
        weekDay = day[datetime.date(int(dates[2]), int(dates[0]), int(dates[1])).weekday()]
        info_key  = info[0] + "," + weekDay

        if info_key not in dic:
            dic[info_key] = info[2] + "," + info[3]
        else:
            info_list = dic[info_key].split(",")
            tmp1 = int(info_list[0]) + int(info[2])
            tmp2 = int(info_list[1]) + int(info[3])
            dic[info_key] = str(tmp1) + "," + str(tmp2)

    for i in dic.keys():
        writeF.write(i + " " + dic[i] + "\n")


except FileNotFoundError:
    print("파일이 없습니다.")
finally:
    readF.close()
    writeF.close()
