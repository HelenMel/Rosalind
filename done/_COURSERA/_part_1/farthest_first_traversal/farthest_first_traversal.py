from collections import namedtuple
import math
import sys

import readFile
import useful

from collections import namedtuple
MyPoint = namedtuple("MyPoint", "X")

def run():
    listOfLines = readFile.listFromInput()
    Data, k, m = parse(listOfLines)
    print "results"
    result = listToPrint(farthestFirstTraversal(Data, k))
    print result
    readFile.lineToOutput(result)
    
def parse(listOfLines):
    (k,m) = map(int,listOfLines[0].split(" "))
    Data = map(toPoint, listOfLines[1:])
    return (Data, k, m)

def toPoint(string):
    return MyPoint(map(float, string.split(" ")))

def farthestFirstTraversal(Data, k):
    Centers = [Data.pop(0).X]
    if len(Data) < k:
        print "wrong data"
        print len(Data)
        print k
        return
    
    while len(Centers) < k:
        DataPoint = maxDistance(Data, Centers)
        Data = filter(lambda a: a != DataPoint, Data)
        Centers.append(DataPoint.X)
    return Centers

def maxDistance(Data, Centers):
    maxDistance = 0
    newCenter = Data[0]
    for point in Data:
        dist = distanceToCenters(point, Centers)
        if dist > maxDistance:
            maxDistance = dist
            newCenter = point
    return newCenter
         
#Centers is matrix
def distanceToCenters(Point1, Centers):
    minDistance = sys.float_info.max
    for i in Centers:
        dist = distance(i, Point1.X)
        if dist < minDistance:
            minDistance = dist
    return minDistance

def distance(PointsList1, PointsList2):
    def dis(x1,x2):
        return pow(x1 - x2,2)
    return math.sqrt(sum(map(dis, PointsList1, PointsList2)))

def listToPrint(list):
    return "\n".join(" ".join(str(y) for y in rows) for rows in list)
