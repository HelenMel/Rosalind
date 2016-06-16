import sys, os
import copy
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))

import directedGraph as dG
import directedWeightGraph as dWG

# before we should decrease nodes count

def presentNodesWeights(weights, nodes, n):
    S = []
    [S.append([0] * n) for x in xrange(0, n)]
    for i in xrange(0, n):
        for j in xrange(0, n):
            if i != j:
                nI = dG.nodeFromSet(i, nodes)
                nJ = dG.nodeFromSet(j, nodes)
                w = dWG.weightFromSet(nI, nJ, weights)
                S[i][j] = w.weight

    return "\n".join([" ".join(format(y, '.0f') for y in rows) for rows in S])

def distancesWithNodesAndWeights(nodes, weights, n):
    nonLeafsNodes = nonLeafs(nodes, n)
    while len(nonLeafsNodes) > 0:
        knot = nonLeafsNodes.pop()
        weights = removeKnot(knot, weights)
    return weights

# its a set
def nonLeafs(nodes, n):
    nonLeafsItems = set()
    for node in nodes:
        if not isLeaf(node, n):
            nonLeafsItems.add(node)
    return nonLeafsItems

# change weights but dont touch knots
def removeKnot(node, weights):
    outs = node.outs
    newWeights = copy.copy(weights)
    for outA in outs:
        removeNodeTarget(outA, node)
        for outB in outs:
            if outA != outB:
                removeMediator(outA, outB, node, weights, newWeights)
    return newWeights

#function modifies weights and nodes
def removeMediator(nodeA, nodeB, mediator, weights, newWeights):
    addNodeTarget(nodeA, nodeB)
    # add new weights
    mergeNodeLengths(nodeA, nodeB, mediator, weights, newWeights)
    
# carefull with hash!
# can it be, that only one of it is there?
def mergeNodeLengths(nodeA, nodeB, mediator, weights, newWeights):
    AMItems = nodesFromWeights(nodeA, mediator, weights)
    BMItems = nodesFromWeights(nodeB, mediator, weights)
    if len(AMItems) > 0 and len(BMItems) > 0:
        AMlen = AMItems[0]
        BMlen = BMItems[0]
        weight = AMlen.weight + BMlen.weight
        ABlen = dWG.NodsWeight(nodeA, nodeB, weight)
        toRemove = AMItems + BMItems
        for item in toRemove:
            if item in newWeights:
                newWeights.remove(item)
        newWeights.add(ABlen)

def nodesFromWeights(startNode, endNode, weights):
    nodes = []
    len1 = dWG.NodsWeight(startNode, endNode, 1.0)
    if len1 in weights:
        nodes.append(dWG.weightFromSet(startNode, endNode, weights))
    len2 = dWG.NodsWeight(endNode, startNode, 1.0)
    if len2 in weights:
        nodes.append(dWG.weightFromSet(endNode, startNode, weights))
    return nodes

def removeNodeTarget(node, oldTarget):
    node.ins.remove(oldTarget)
    node.outs.remove(oldTarget)

def addNodeTarget(node, newTarget):
    node.ins.append(newTarget)
    node.outs.append(newTarget)

def isLeaf(node, n):
    return (node.base < n)