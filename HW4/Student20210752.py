#!/usr/bin/python3

import sys
from os import listdir
import numpy as np
import operator

def createDataSet(dirName):
    labels = []
    trainingFile = listdir(dirName)
    data = len(trainingFile)
    matrix = np.zeros((data, 1024))

    for i in range(data):
        fileName = trainingFile[i]
        result = int(fileName.split('_')[0])
        labels.append(result)
        matrix[i, :] = vector(dirName +"/" +fileName)
    
    return matrix, labels

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis = 1)
    distances = sqDistances ** 0.5

    sortedDistances = distances.argsort()
    classCount = {}

    for i in range(k):
        voteIlabel = labels[sortedDistances[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) +1
        sortedClassCount = sorted(classCount.items(), key = operator.itemgetter(1), reverse = True)

    return sortedClassCount[0][0]

def vector(fileName):
    vector = np.zeros((1, 1024))

    f = open(fileName)
    for i in range(32):
        line = f.readline()
        for j in range(32):
            vector[0, 32 * i + j] = int(line[j])

    return vector


trainingFileName = sys.argv[1]
testFileName = sys.argv[2]

testFile = listdir(testFileName)
size = len(testFile)

matrix, labels = createDataSet(trainingFileName)

for i in range(1, 21):
    count = 0
    error = 0

    for j in range(size):
        result = int(testFile[j].split('_')[0])
        test = vector(testFileName + "/" + testFile[j])
        classify0Result = classify0(test, matrix, labels, i)
        count += 1

        if result != classify0Result:
            error += 1

    print(int(error / count * 100))
