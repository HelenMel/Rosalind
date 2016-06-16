import sys, os
from collections import deque
import copy
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_4')))

import directedGraph as dG
import directedWeightGraph as dWG
import directedLabelGraph as dLG
import nucleotides as alphabet

def parseStringsToTreeAndLabels(lines):
    # assume that index could not be repeated
    newNodeIndex = 0; nodes = set(); labels = set(); tLenght = 0
    for line in lines:
        ln, rn = line.split("->")
        try:
            nodeOutValue = int(ln)
        except ValueError:
            continue
        nodeOut = dG.nodeFromSet(nodeOutValue, nodes)
        try:
            nodeInValue = int(rn)
        except ValueError:
            nodeInValue = newNodeIndex
            newLabel = dLG.NodeLabel(nodeInValue, rn)
            labels.add(newLabel)
            newNodeIndex += 1
            tLenght = len(rn)
        nodeIn = dG.nodeFromSet(nodeInValue, nodes)
        nodeOut.addOut(nodeIn); nodeIn.addIn(nodeOut)
    rootBase = 566
    rootNode = dG.nodeFromSet(rootBase, nodes)
    rootNode.ins = []
    removeAllUselessIns(nodes, rootBase)
    #print "remove useless completed"
    #print nodes
    return nodes, labels, tLenght

def removeAllUselessIns(nodes, rootBase):
    node = dG.nodeFromSet(rootBase, nodes)
    for outNode in node.outs:
        try:
            outNode.outs.remove(node)
        except ValueError:
            "do nothing"
        outNode.ins = [node]
        removeAllUselessIns(nodes, outNode.base)

def smallParsimony_run(Tree, Labels, m, n):
    totalScore = 0; rootB = -1
    Weights = set()
    for i in xrange(0, m):
        S, rootBase, Backtrack = smallParsimony(Tree, Labels, i, n)
        rootB = rootBase
        rootS = S[rootBase]
        minK = min(rootS, key = rootS.get)
        minS = rootS[minK]
        extendLabelWithBase(minK, rootBase, Labels)
        outputBacktrack(rootBase, minK, Tree, Backtrack, Labels, n)
        #print Labels
        updateWeights(rootBase, minK, Tree, Weights, Labels, i)
        totalScore += minS
    Weights = removeRootWeight(Weights, rootB, Tree)
    Weights = doubleWeights(Weights)
    #print Weights
    return totalScore, combineWeightsAndLabelsIntoStrings(Weights, Labels)

def removeRootWeight(Weights, rootBase, Tree):
    rootNode = dG.nodeFromSet(rootBase, Tree)
    one = rootNode.outs[0]
    two = rootNode.outs[1]
    oldEdge1 = dWG.weightFromSet(rootBase, one.base, Weights)
    Weights.remove(oldEdge1)
    oldEdge2 = dWG.weightFromSet(rootBase, two.base, Weights)
    Weights.remove(oldEdge2)
    newEdge = dWG.NodsWeight(one.base, two.base, oldEdge1.weight + oldEdge2.weight)
    Weights.add(newEdge)
    return Weights

def doubleWeights(Weights):
    newWeights = copy.copy(Weights)
    for weight in Weights:
        oppositeWeight = dWG.NodsWeight(weight.end, weight.start, weight.weight)
        newWeights.add(oppositeWeight)
    return newWeights

def combineWeightsAndLabelsIntoStrings(Weights, Labels):
    lines = []
    for weight in Weights:
        startNodeLabel = dLG.labelNodeFromSet(weight.start, Labels)
        endNodeLabel = dLG.labelNodeFromSet(weight.end, Labels)
        weightLabel = format(weight.weight, '.0f')
        description = startNodeLabel.label + "->" + endNodeLabel.label + ":" + weightLabel
        lines.append(description)
    return lines

def updateWeights(base, symbol, Tree, Weights, Labels, i):
    node = dG.nodeFromSet(base, Tree)
    for outNode in node.outs:
        weight = weightWithBase(node.base, outNode.base, Weights)
        outNodeLabel = dLG.labelNodeFromSet(outNode.base, Labels)
        outNodeSymbol = outNodeLabel.label[i]
        if outNodeSymbol != symbol:
            weight.weight += 1
        updateWeights(outNode.base, outNodeSymbol, Tree, Weights, Labels, i)

def outputBacktrack(nodeBase, symbol, Tree, Backtrack, Labels, n):
    node = dG.nodeFromSet(nodeBase, Tree)
    if isLeaf(node, n):
        return
    for outNode in node.outs:
        outLabel = Backtrack[nodeBase][symbol][outNode.base]
        if isLeaf(outNode, n):
            continue
        extendLabelWithBase(outLabel, outNode.base, Labels)
        outputBacktrack(outNode.base, outLabel, Tree, Backtrack, Labels, n)

def weightWithBase(startNodeBase,endNodeBase, Weights):
    newWeight = dWG.NodsWeight(startNodeBase, endNodeBase, 0.0)
    if newWeight in Weights:
        return dWG.weightFromSet(startNodeBase, endNodeBase, Weights)
    else:
        Weights.add(newWeight)
    return newWeight

def extendLabelWithBase(additionalSymbol, nodeBase, Labels):
    newLabel = dLG.NodeLabel(nodeBase, additionalSymbol)
    if newLabel in Labels:
        labelNode = dLG.labelNodeFromSet(nodeBase, Labels)
        labelNode.label += additionalSymbol
    else:
        Labels.add(newLabel)

def smallParsimony(Tree, Labels, i, n):
    Tag, S = initialTagsAndS(Tree, Labels, i, n)
    Backtrack = {}
    Untaged = deque([k for k,v  in Tag.items() if v == 0])
    rootBase = 0
    while len(Untaged) > 0:
        if len(Untaged) == 1:
            rootBase = Untaged[0]
        nodeBase = Untaged.popleft()
        node = dG.nodeFromSet(nodeBase, Tree)
        if isNodeRipe(node, Tag):
            Tag[nodeBase] = 1
            daughterNode = node.outs[0]
            sonNode = node.outs[1]
            minScore(nodeBase, daughterNode, sonNode, S, Backtrack)
        else:
            Untaged.append(nodeBase)
    root = dG.nodeFromSet(rootBase, Tree)
    assert len(root.ins) == 0
    return S, rootBase, Backtrack

def minScore(nodeBase, daughterNode, sonNode, S, Backtrack):
    for k in alphabet.nucleotides:
        daughterScore, daughterSymbol = minScoreForNode(daughterNode.base, S, k)
        sonScore, sonSymbol = minScoreForNode(sonNode.base, S, k)
        score = daughterScore + sonScore
        addToS(S, nodeBase, k, score)
        pre = { daughterNode.base: daughterSymbol,
                sonNode.base: sonSymbol }
        addToS(Backtrack, nodeBase, k, pre)
    return

def minScoreForNode(nodeBase, S, symbol):
    minScore = float('inf'); minSymbol = ""
    for i in alphabet.nucleotides:
        score = S[nodeBase][i]
        if symbol != i:
            score += 1
        if score < minScore:
            minScore = score
            minSymbol = i
    for j in alphabet.nucleotides:
        if minScore - 1 == S[nodeBase][j]:
            return minScore, j
    return minScore, minSymbol

def isNodeRipe(node, Tag):
    for outNodes in node.outs:
        if Tag[outNodes.base] == 0:
            return False
    return True

def initialTagsAndS(Tree, Labels, i, n):
    Tag = {}
    S = {}
    for node in Tree:
        Tag[node.base] = 0
        if isLeaf(node, n):
            Tag[node.base] = 1
            for k in alphabet.nucleotides:
                nL = dLG.labelNodeFromSet(node.base, Labels)
                if nL.label[i] == k:
                    Sk = 0
                else:
                    Sk = float('inf')
                addToS(S, node.base, k, Sk)
    return Tag, S

def isLeaf(node, n):
    if node.base < n:
        return True
    return False

def addToS(S, nodeBase, k, Sk):
    if nodeBase in S:
        S[nodeBase][k] = Sk
    else:
        S[nodeBase] = { k: Sk }