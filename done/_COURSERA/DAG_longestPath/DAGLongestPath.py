import sys, os
import copy
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))

import simpleGraphWeight as sGW

def longestPath(nodes, weights, sourse, sink):
    ordered = orderNodesTopologically(nodes, sourse)
    S, Backtrace = backtraceOrderedNodes(ordered, weights)
    path = pathFormBacktrace(Backtrace, sourse, sink, ordered)
    sinkIndex = ordered.index(sink)
    return S[sinkIndex], path

def orderNodesTopologically(nodes, sourse):
    originalSourse = findOriginalSourceFromNodes(sourse)
    ordered = [originalSourse]
    processedItems = set()
    processedItems.add(originalSourse) 
    unordered = set(originalSourse.outs)
    i = 0
    while len(unordered) > 0 and i < 1000:
        i +=1
        unordered_ = set()
        for unode in unordered:
            allInKnown, unknownNode = isAllNodeKnown(unode, processedItems)
            if allInKnown:
                processedItems.add(unode)
                if unode in unordered_:
                    unordered_.remove(unode)
                ordered.append(unode)
                for n in unode.outs:
                    if n not in processedItems:
                        unordered_.add(n)
            else:
                unordered_.add(unknownNode)
                unordered_.add(unode)
        unordered = unordered_
    ordered_ = [originalSourse]
    for node in ordered:
        if len(node.ins) > 0:
            ordered_.append(node)
    return ordered_

def isAllNodeKnown(node, processedItems):
    allInKnown = True
    nIns = copy.copy(node.ins)
    for innode in nIns:
        if innode not in processedItems:
            if len(innode.ins) > 0:
                return False, innode
            else:
                breakAllConnections(innode, processedItems)
    return True, None

def breakAllConnections(node, processedItems):
    for outNode in node.outs:
        outNode.ins.remove(node)
        if len(outNode.ins) == 0:
            breakAllConnections(outNode, processedItems)
    processedItems.add(node)

def backtraceOrderedNodes(ordered, weights):
    Backtrace = [ordered[0]]
    S = [0]
    for i in xrange(1, len(ordered)):
        node = ordered[i]
        def nodeWeight(nodeIn, node):
            index = ordered.index(nodeIn)
            w = sGW.weightFromSet(nodeIn, node, weights)
            Sn = S[index] + w.weight
            return (nodeIn, Sn)
        Distances = [nodeWeight(n, node) for n in node.ins]
        maxNode = max(Distances, key=lambda x: x[1])
        Backtrace.append((maxNode[0]))
        S.append(maxNode[1])
    return S, Backtrace

def pathFormBacktrace(Backtrace, sourse, sink, ordered):
    sinkIndex = ordered.index(sink)
    nextIndex = sinkIndex
    nextNode = None
    path = [ sink ]
    while nextNode != sourse:
        nextNode = Backtrace[nextIndex]
        path.insert(0, nextNode)
        nextIndex = ordered.index(nextNode)
    return path
        

def findOriginalSourceFromNodes(sourse):
    if len(sourse.ins) == 0:
        return sourse
        for inN in sourse.ins:
            return findOriginalSourceFromNodes(inN)
    return None
        