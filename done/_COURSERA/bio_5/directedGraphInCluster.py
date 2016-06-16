import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))

import directedGraph as dG
import equalitySet as eS

class Cluster(dG.Node):
	def __init__(self, base, count = 1, multiplier = 1):
		super(Cluster, self).__init__(base)
		self.count = count
		self.multiplier = multiplier

def mergeClusters(Cluster1, Cluster2):
	mergeClusterName = Cluster1.base + " " + Cluster2.base
	totalCount = Cluster1.count + Cluster2.count
	multiplier = Cluster1.count * Cluster2.count
	mergeCluster = Cluster(mergeClusterName, totalCount, multiplier)
	mergeCluster.outs = [ Cluster1, Cluster2 ]
	#print mergeCluster.outs
	#print " count and multiplier ", mergeCluster.count, mergeCluster.multiplier
	return mergeCluster


