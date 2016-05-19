'''
Created on 2015-6-4

@author: yzt
'''
from numpy import zeros, log, array
from os.path import os

def getDataSet0():
    if os.access("AllElectronics.txt", os.F_OK):
        f = open("AllElectronics.txt")
        line = f.readline()
        dataset = [];data = [];labels = []
        for line in f.readlines():
            data = line.split()
            labels.append(data[-1])
            dataset.append(data[0:len(data) - 1])
        f.close()
        return labels, dataset
    return "file is not exsists"



def loadDataSet():
    dataset = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
               ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
               ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
               ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
               [ 'mr', 'licks', 'ate', 'my' , 'steak', 'how', 'to', 'stop', 'him'],
               ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    labels = [0, 1, 0, 1, 0, 1]
    return labels, dataset

def getDataSet():
    dataset = [];labels = [];temp = []
    with open('spam_train.txt') as f:
        for line in f:
            temp = line.strip().split()
            labels.append(int(temp[0]))
            dataset.append(temp[1:])
    f.close()
    return labels, dataset

def createVacList(dataset):
    vacSet = set([])
    for data in dataset:
        vacSet = vacSet | set(data)
    return list(vacSet)

def getBitOfVacList(vacList, inputSet):
    returnVec = [0] * len(vacList)
    for word in inputSet:
        if word in vacList:
            returnVec[vacList.index(word)] = 1
    return returnVec

def trainNaiveBayes(matrixNB, trainLabels):
    numTrainDocs = len(matrixNB)
    numWords = len(matrixNB[0])
    isSpam = sum(trainLabels) / float(numTrainDocs)
    p0Docs = 0.0; p1Docs = 0.0
    p0Num = zeros(numWords); p1Num = zeros(numWords)
    for i in range(numTrainDocs):
        if trainLabels[i] == 1:
            p1Num += matrixNB[i]
            p1Docs += 1
        else:
            p0Num += matrixNB[i]
            p0Docs += 1
    p1Vec = (array(p1Num) + 1) / float(p1Docs + 2)
    p0Vec = (array(p0Num) + 1) / float(p0Docs + 2)
    return p1Vec, p0Vec, isSpam        

def saveFileAs(dataset):
    f = open('result.txt', 'w')
    for line in dataset:
        f.write(str(line) + '\n')
    f.close()
    
def classifyNB(thisDoc, p1Vec, p0Vec, isSpam):
    '''
    p1 = sum(p1Vec * thisDoc) + log(isSpam)
    p0 = sum(p0Vec * thisDoc) + log(1 - isSpam)
    '''
    p1 = 0.0; p0 = 0.0
    for i in range(len(thisDoc)):
        k1 = p0Vec[i]/p1Vec[i]
        k2 = (1-p0Vec[i])/(1-p1Vec[i])
        p1 += (1-thisDoc[i])*log(1 - p1Vec[i])*k2+thisDoc[i]*log(p1Vec[i])*k1
        p0 += (1-thisDoc[i])*log(1 - p0Vec[i])/k2+thisDoc[i]*log(p0Vec[i])/k1
    p1 += log(isSpam)
    p0 += log(1 - isSpam)
    
    if p1 > p0:
        return 1
    else:
        return 0
    
def createVocabList(dataSet):
    tempVocabulary = {}
    vocabulary = {}
    for mail in dataSet:
        for word in set(mail):
            if word in tempVocabulary:
                tempVocabulary[word] += 1
            else:
                tempVocabulary[word] = 1
    for key in tempVocabulary:
        if tempVocabulary[key] >= 30:     
            vocabulary[key] = tempVocabulary[key]
    return list(vocabulary.keys())

def spamTest():
    err = 0
    labels, dataset = getDataSet()
    vacList = createVocabList(dataset)
    print 'word vector:' + str(len(vacList))
    matrixNB = []
    for inputSet in dataset:
        matrixNB.append(getBitOfVacList(vacList, inputSet))
    p1Vec, p0Vec, isSpam = trainNaiveBayes(matrixNB, labels)
    f = open('spam_test.txt')
    for line in f.readlines():
        temp = line.strip().split()
        
        thisDoc = getBitOfVacList(vacList, temp[1:])
        label = classifyNB(thisDoc, p1Vec, p0Vec, isSpam)
        if label != int(temp[0]):
            err += 1
    f.close()
    return err
    # saveFileAs(p1Vec)
    # print p0Vec

if __name__ == '__main__':
    print 'error rate is:' + str(spamTest()/1000.0*100)+'%'
    
