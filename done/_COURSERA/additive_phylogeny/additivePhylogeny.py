import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_4')))

import limbLength as lL
import simpleGraph as sG
import simpleGraphWeight as sGW

internalNodeIndex = 0

def additivePhylogenyRun(D, n):
    global internalNodeIndex
    internalNodeIndex = n
    return additivePhylogeny(D, n)

def additivePhylogeny(D, n):
    global internalNodeIndex
    # D is distances matrix, n is matrix size
    if n == 2:
        return treeConsistingOnEdge(D[0][1])
    last = n - 1
    limbLength = lL.limbLength(n, last, D)
    for j in xrange(0, last):
        D[j][last] = D[j][last] - limbLength
        D[last][j] = D[j][last]
    i, k = selectThreeLeavesInRow(D, last, n)
    dx = D[i][last];
    removeColumn(D, last)
    Tree, Weights = additivePhylogeny(D, n - 1)
    knot = createAndAddKnotNode(Tree, Weights, dx, i, k, internalNodeIndex)
    internalNodeIndex += 1
    l = createAndAddLeaf(Tree, Weights, knot, last, limbLength)
    return Tree, Weights

# create node and wight
def treeConsistingOnEdge(Dij):
    node1 = sG.Node(0); node2 = sG.Node(1)
    node1.addEdge(node2); node2.addEdge(node1)
    Tree = set(); Tree.add(node1); Tree.add(node2)
    weight = sGW.NodsWeight(node1, node2, Dij)
    Weights = set(); Weights.add(weight)
    return Tree, Weights

# may be it is not a leaves it is just indexes?
def selectThreeLeavesInRow(D, j, n):
    # for each two items in row, compute the one with
    row = D[j]
    for i in xrange(0, n):
        for k in xrange(i + 1, n):
            if i == j or k == j:
                continue
            if D[i][k] == (row[i] + row[k]):
                return (i, k)
    print "false row", row
    assert False, "cant break any edge"

def removeColumn(D, j):
    D.pop(j)
    for row in D:
        row.pop(j)

# return node and checking old nodes
def createAndAddKnotNode(Tree, Weights, distance, i, k, internalIndex):
    leafStart = sG.nodeFromSet(i, Tree); leafEnd = sG.nodeFromSet(k, Tree)
    startNode, endNode, dx = closestNodesWithDistanceOnPath(Tree, Weights, leafStart, leafEnd, distance)
    # create knot 
    knotName = internalIndex
    knot = sG.Node(knotName)
    # append new node
    placeNodeBetweenNodes(startNode, endNode, knot)
    Tree.add(knot)

    #update weight
    updateWeights(Weights, startNode, endNode, knot, dx)
    return knot

def updateWeights(Weights, startNode, endNode, knot, dx):
    oldWeight = sGW.weightFromSet(startNode, endNode, Weights)
    Weights.remove(oldWeight)
    startToNodeW = sGW.NodsWeight(startNode, knot, dx)
    endToNodeW = sGW.NodsWeight(endNode, knot, oldWeight.weight - dx)
    Weights.add(startToNodeW); Weights.add(endToNodeW)

def placeNodeBetweenNodes(startNode, endNode, knot):
    startNode.edges.remove(endNode); endNode.edges.remove(startNode)
    startNode.addEdge(knot); endNode.addEdge(knot);
    knot.addEdge(startNode); knot.addEdge(endNode);

# it returns start and end nodes and distance to start node
# start and end are leafs
def closestNodesWithDistanceOnPath(Tree, Weights, start, end, distance):
    currentD = 0
    preD = 0
    visited = set()
    path = pathFromLeafToLeaf(start, end, visited)
    if path is None:
        print "no path ", start, end
        assert False, "Should be expected"
    currentNode = None
    nextNode = path.pop()
    if nextNode != start:
        assert False, "Should be equals"
    while currentD < distance:
        currentNode = nextNode
        nextNode = path.pop()
        preD = currentD
        currentD += sGW.weightFromSet(currentNode, nextNode, Weights).weight
    dx = distance - preD
    return currentNode, nextNode, dx

def pathFromLeafToLeaf(start, end, visited):
    if start == end:
        return [ end ]
    edgeNodes = start.edges
    visited.add(start)
    for edgeNode in edgeNodes:
        if edgeNode in visited:
            continue
        if isLeaf(edgeNode) and edgeNode != end:
            continue
        path = pathFromLeafToLeaf(edgeNode, end, visited)
        if path is not None:
            path.append(start)
            return path
    return None

def isLeaf(node):
    if len(node.edges) < 2:
        return True
    return False

def createAndAddLeaf(Tree, Weights, knot, base, limbLength):
    leaf = sG.Node(base);
    leaf.addEdge(knot); knot.addEdge(leaf)
    Tree.add(leaf)
    limbW = sGW.NodsWeight(leaf, knot, limbLength)
    Weights.add(limbW)
    return leaf

# weights presentation
def presentWeights(Weights):
    WeightList = []
    for weight in Weights:
        WeightList.append(weight)
        WeightList.append(weight.mirrorNode())
    WeightList.sort(key = lambda x: x.node1.base)
    return "\n".join([x.show() for x in WeightList])

