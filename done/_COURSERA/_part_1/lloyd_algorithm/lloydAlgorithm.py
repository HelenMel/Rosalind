import random

import pointsDistances

def lloydAlgorithm(Data, k):
    Centers, Points = selectRandomCenters(Data,k)
    Centers = foundNewCenters(Points, Centers)
    return Centers

def selectRandomCenters(Data, k):
    Centers = []
    if len(Data) < k:
        print "wrong data"
        return
    Centers = Data[:k]
    #for i in range(k):
    #    newCenter = random.choice(Data)
    #    index = Data.index(newCenter)
    #    Centers.append(newCenter)
    return (Centers, Data)

def foundNewCenters(Points, Centers):
	clasters = makeClasters(Points, Centers)
	newCenters = []
	for i in range(len(Centers)):
		newCenters.append(gravityCenter(clasters[i], Centers[i]))
	if Centers == newCenters:
		return newCenters
	else:
		return foundNewCenters(Points, newCenters)

def makeClasters(Points, Centers):
	clasters = []
	for i in range(len(Centers)):
		clasters.append([])

	for point in Points:
		nearestCenter, dist = pointsDistances.nearestCenterWithDistance(point, Centers)
		index = Centers.index(nearestCenter)
		clasters[index].append(point)
	return clasters

def gravityCenter(Points, Center):
	Points = filter(lambda a: a != Center, Points)
	if  len(Points) == 0:
		return Center
	n = float(len(Points))
	m = len(Points[0])
	transpPoints = [[row[i] for row in Points] for i in range(m)]

	return [sum(x)/n for x in transpPoints]