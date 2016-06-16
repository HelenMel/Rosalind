import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))

import simpleGraph as sG
import simpleGraphWeight as sGW

def neighbor_joining_run(D, n):
    T = set([sG.Node(x) for x in xrange(0, n)])
    leafNames = [x for x in xrange(0, n)]
    Limbs = []
    T, Limbs = neighborjoining(D, n, T, Limbs, leafNames)
    Limbs = sorted(Limbs, key= lambda x: x.node1.base)
    return Limbs

def neighborjoining(D, n, T, Limbs, leafNames):
    if n == 2:
        limbLength = D[0][1]
        Leaf1 = sG.nodeFromSet(leafNames[0], T)
        Leaf2 = sG.nodeFromSet(leafNames[1], T)
        createLimb(Limbs, Leaf1, Leaf2, limbLength)
        return T, Limbs
    TotalDistance = [sum(x) for x in D]
    nD = neighborDistanceMatrix(D, n, TotalDistance)
    i, j = minItemIndexes(nD, n)
    Delta = float(TotalDistance[i] - TotalDistance[j]) / (n - 2)
    Dij = D[i][j]
    limbLengthI = (Dij + Delta) / 2.0
    limbLengthJ = (Dij - Delta) / 2.0
    addNewRowAndColumnForJoinedLeaf(D, n, i, j)
    i, j = orderedTwo(i, j)
    Di, Dj = popCorrespondingRowAndColums(D, i, j)
    LeafJBase = leafNames.pop(j); LeafIBase = leafNames.pop(i)
    LeafI = sG.nodeFromSet(LeafIBase, T)
    LeafJ = sG.nodeFromSet(LeafJBase, T)
    joinedLeafBase = len(T)
    joinedLeaf = createRootNode(T, LeafI, LeafJ, joinedLeafBase)
    leafNames.append(joinedLeafBase)

    # recursion starts here
    T, Limbs = neighborjoining(D, n - 1, T, Limbs, leafNames)

    createLimb(Limbs, LeafI, joinedLeaf, limbLengthI)
    createLimb(Limbs, LeafJ, joinedLeaf, limbLengthJ)
    return T, Limbs

# save edge (Limb) length
def createLimb(Limbs, leaf1, leaf2, length):
    Limbs.append(sGW.NodsWeight(leaf1, leaf2, length))
    Limbs.append(sGW.NodsWeight(leaf2, leaf1, length))

# create node and connect edges
def createRootNode(T, LeafI, LeafJ, rootBase):
    newNode = sG.Node(rootBase);
    LeafI.addEdge(newNode); LeafJ.addEdge(newNode)
    newNode.addEdge(LeafI); newNode.addEdge(LeafJ)
    T.add(newNode)
    return newNode

# remove i and j columns from D
def popCorrespondingRowAndColums(D, i, j):
    for row in D:
        row.pop(j); row.pop(i)
    Dj = D.pop(j); Di = D.pop(i)
    return Di, Dj

def orderedTwo(i, j):
    if i < j:
        return i, j
    else:
        return j, i

# add new row and column
def addNewRowAndColumnForJoinedLeaf(D, n, i, j):
    Dij = D[i][j]
    Dnew = []
    for k in xrange(0, n):
        Dmk = (D[k][i] + D[k][j] - Dij) / 2.0
        D[k].append(Dmk)
        Dnew.append(Dmk)
    Dnew.append(0)
    D.append(Dnew)

def minItemIndexes(D, n):
    minValue = sys.maxint
    minI = -1; minJ = -1
    for i in xrange(0, n):
        for j in xrange(0, n):
            if D[i][j] < minValue and i != j:
                minValue = D[i][j]
                minI = i; minJ = j
    return minI, minJ

def neighborDistanceMatrix(D, n, TotalDistance):
    def distance(i, j):
        return (D[i][j] * (n - 2) - TotalDistance[i] - TotalDistance[j])
    nD = [[0] * n for x in xrange(0, n)]
    for i in xrange(0, n):
        for j in xrange(i + 1, n):
            dist = distance(i, j)
            nD[i][j] = dist
            nD[j][i] = dist
    return nD

D = [[0, 14, 17, 17], [14, 0, 7, 13], [17, 7, 0, 16], [17, 13, 16, 0]]
TotalDistance = [sum(x) for x in D]
print neighborDistanceMatrix(D, 4, TotalDistance)

#DS = [[0, 20, 9, 11], [20, 0, 17, 11], [9, 17, 0, 8], [11, 11, 8, 0]]
TotalDistanceS = [sum(x) for x in D]
i = 1
j = 2
Dij = D[i][j]
Delta = float(TotalDistanceS[i] - TotalDistanceS[j]) / (4 - 2)
print Delta
print  (Dij + Delta) / 2.0
print  (Dij - Delta) / 2.0