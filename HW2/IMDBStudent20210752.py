#!/usr/bin/python3
import sys

try:
    readF = open(sys.argv[1])
    writeF = open(sys.argv[2], "wt")
    
    genList = list()
    count = 0
    for line in readF:
        line = line.rstrip()
        gen = line.split("::")
        genre = gen[2].split("|")
        for i in genre:
            genList.append(i)
    genSet = set(genList)
    genCount = list()
    for i in genSet:
        genCount.append((i, genList.count(i)))
    for i in genCount:
        writeF.write(i[0] + " " + str(i[1]) + "\n")
except FileNotFoundError:
    print("파일이 없습니다.")
finally:
    readF.close()
