import math
import numpy
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_5')))

import pointsDistances as pD

def centersFromData(Data, beta, k, m, steps):
	Centers = numpy.array(Data[:k])
	Points = numpy.array(Data)
	n = len(Points)
	for i in xrange(0, steps):
		HiddenMatrix = centersToClusters(Points, Centers, beta, k, m)
		Centers = clusterToCenters(Points, HiddenMatrix, n, k, m)
	print "stop"
	return Centers

def centersToClusters(Points, Centers, beta, k, m):
	n = len(Points)
	HiddenMatrix = numpy.zeros((k, n))
	for i in xrange(0, k):
		center = Centers[i]
		for j in xrange(0, n):
			point = Points[j]
			distance = numpy.sqrt(numpy.sum((point-center)**2))
			HiddenMatrix[i, j] = math.exp(-beta * (distance))
	sumAll = HiddenMatrix.sum(axis=0, keepdims=True)
	return (HiddenMatrix / sumAll[:,None]).reshape(k, n)
	
def clusterToCenters(Points, HiddenMatrix, n, k, m):
	sums = HiddenMatrix.dot(numpy.ones(n)).T
	Centers = HiddenMatrix.dot(Points);
	return (Centers / sums[:,None]).reshape(k, m)
	