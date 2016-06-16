import math
import sys

def squaredErrorDistortion(Data, Centers):
	n = len(Data)
	return sum([pow(distanceToCenters(point, Centers), 2) for point in Data]) / n

def distanceToCenters(Point1, Centers):
    minDistance = sys.float_info.max
    for i in Centers:
        dist = distance(i, Point1)
        if dist < minDistance:
            minDistance = dist
    return minDistance

def distance(PointsList1, PointsList2):
    def dis(x1,x2):
        return pow(x1 - x2,2)
    return math.sqrt(sum(map(dis, PointsList1, PointsList2)))