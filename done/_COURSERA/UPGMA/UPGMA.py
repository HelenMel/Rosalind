import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))

import simpleGraph as sG
import simpleGraphWeight as sGW

def UPGMA(D, n):
    # D and Clusters indexes should be sync
    Clusters = [(x, [x]) for x in xrange(0, n)]
    T = set([sG.Node(x) for x in xrange(0, n)])
    print T
    Age = {}
    for v in T:
        Age[v] = 0
    while len(Clusters) > 1:
        i, j, Dij = twoClosestClusters(D)
        i, j = orderTwo((i, j))
        Ci, Cj = popFromClusters(Clusters, i, j)
        CnewItems = Ci[1] + Cj[1]
        CnewBase, CnewNode = createRootNode(T, Ci[0], Cj[0])
        Cnew = (CnewBase, CnewItems)
        Age[CnewNode] = Dij / 2;
        Di, Dj = popCorrespondingRowAndColums(D, i, j)
        addRowAndColumnOfDistances(D, Di, Dj,len(Clusters), len(Ci[1]), len(Cj[1]))
        Clusters.append(Cnew)
    root = sG.nodeFromSet(Clusters[0][0], T)
    # for each edge
    Lengths = []
    for node in T:
        for edge in node.edges:
            length = Age[edge] - Age[node]
            Lengths.append(sGW.NodsWeight(node, edge, length))
    return sorted(Lengths, key = lambda x: x.node1.base)

def addRowAndColumnOfDistances(D, Di, Dj, lC, lCi, lCj):
    Dnew = []
    for m in xrange(0, lC):
        Dm = distanceBetweenClusters(Di, Dj, lCi, lCj, m)
        Dnew.append(Dm)
        D[m].append(Dm)
    Dnew.append(0.0)
    D.append(Dnew)

# distance between clusters
def distanceBetweenClusters(Di, Dj, lenCi, lenCj, m):
    return (float(Di[m] * lenCi) + float(Dj[m] * lenCj)) / (lenCi + lenCj)

# remove i and j from clusters
def popFromClusters(Clusters, i, j):
    Cj = Clusters.pop(j)
    Ci = Clusters.pop(i)
    return Ci, Cj

# remove i and j columns from D
def popCorrespondingRowAndColums(D, i, j):
    for row in D:
        row.pop(j); row.pop(i)
    Dj = D.pop(j); Di = D.pop(i)
    return Di, Dj

#create node and connect edges
def createRootNode(T, CiBase, CjBase):
    newRootBase = len(T)
    newNode = sG.Node(newRootBase);
    CiRoot = sG.nodeFromSet(CiBase, T)
    CjRoot = sG.nodeFromSet(CjBase, T)
    CiRoot.addEdge(newNode); CjRoot.addEdge(newNode)
    newNode.addEdge(CiRoot); newNode.addEdge(CjRoot)
    T.add(newNode)
    return newRootBase, newNode
    # add weights

def orderTwo((i, j)):
    if i < j:
        return i, j
    else:
        return j, i

#return indexes for Cluster matrix
def twoClosestClusters(D):
    # we need to figure out place cluster in D matrix.
    minValue = sys.float_info.max
    minI = -1; minJ = -1
    for i in xrange(0, len(D)):
        for j in xrange(i + 1, len(D[0])):
            if i != j and D[i][j] < minValue:
                minValue = D[i][j]
                minI = i; minJ = j
    return minI, minJ, float(minValue)

D = [[0, 20, 17, 11], [20, 0, 20, 13], [17, 20, 0, 10], [11, 13, 10, 0]]
#print UPGMA(D, 4)