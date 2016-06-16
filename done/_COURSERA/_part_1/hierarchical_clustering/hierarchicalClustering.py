import numpy
import sys, os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_5')))

import directedGraphInCluster as dGIC
import numpy as np

def hierarchicalClustering(Data, n):
	# try without T
	D = np.array(fixDiagonalValue(Data, n))
	Clusters = [dGIC.Cluster(str(x)) for x in xrange(1, n + 1)]
	Answer = []
	while len(Clusters) > 1:
		minD = np.unravel_index(np.argmin(D), D.shape)
		mCluster = newCluster(minD[0], minD[1], Clusters)
		Answer.append(str(mCluster))
		dist = distToNewCluster(minD[0], minD[1], Clusters, D)
		D = extendDWithDistances(D, dist)
		Clusters.append(mCluster)
		D, Clusters = removeOldClustersForIndexes(minD, D, Clusters)
	return Answer

def removeOldClustersForIndexes(indx, D, Clusters):
	D = np.delete(D, indx, 0)
	D = np.delete(D, indx, 1)
	Clusters = [i for j, i in enumerate(Clusters) if j not in indx]
	return D, Clusters

def newCluster(i1, i2, Clusters):
	C1 = Clusters[i1]
	C2 = Clusters[i2]
	return dGIC.mergeClusters(C1, C2)

def distToNewCluster(i1, i2, Clusters, D):
	C1 = Clusters[i1]
	C2 = Clusters[i2]
	nC = len(Clusters)
	dist = np.zeros((1, nC))
	for x in xrange(0, nC):
		ClusterX = Clusters[x]
		#print "Cluster x count", ClusterX.count
		# if its not working, try to use multiplier
		dist[0, x] = (D[x, i1] * C1.count + D[x, i2] * C2.count) / (C1.count + C2.count)
	return dist

def extendDWithDistances(D, dist):
	D = np.append(D, dist, 0)
	distY = numpy.append(dist, [[float('+inf')]], 1).T
	D = np.append(D, distY, 1)
	return  D

# make diagonal not equal zero
def fixDiagonalValue(Data, n):
	for x in xrange(0, n):
		Data[x][x] = float('+inf')
	return Data