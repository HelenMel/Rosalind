import math
import sys

def squaredErrorDistortion(Data, Centers):
	n = len(Data)
	return sum([pow(distanceToCenters(point, Centers), 2) for point in Data]) / n

def nearestCenterWithDistance(Point1, Centers):
    minDistance = sys.float_info.max
    closestCenter = Centers[0]
    for center in Centers:
        dist = distance(center, Point1)
        if dist < minDistance:
            minDistance = dist
            closestCenter = center
    return (closestCenter, minDistance)

def distanceToCenters(Point1, Centers):
    closestCenter, minDistance = nearestCenterWithDistance(Point1, Centers)
    return minDistance

def distance(Points1, Points2):
    def dis(x1,x2):
        return pow(x1 - x2,2)
    return math.sqrt(sum(map(dis, Points1, Points2)))