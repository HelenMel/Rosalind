import sys, os
import copy
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))

import directedGraph as dG
import directedLabelEdge as edge
import nucleotides as info

def parseLineToNodes(line):
    nodesValues = [0]
    nodesValues += map(int, line.split(" "))
    nodes = []
    for nodeValue in nodesValues:
        nodes.append(dG.Node(nodeValue))
    return nodes

def edgeGraphToAnswer(edges):
    def representEdge(edge):
        return str(edge.start) + "->" + str(edge.end) + ":" + edge.label
    return [representEdge(edge) for edge in edges]

def nodesToSpectrumGraph(nodes):
    massTable = info.massIntTable()
    massSet = info.massIntSet()
    edges = []
    unvisitedNodes = copy.copy(nodes)
    for node in nodes:
        unvisitedNodes.remove(node)
        for anotherNode in unvisitedNodes:
            if node == anotherNode:
                continue
            diff = node.base - anotherNode.base
            if abs(diff) in massSet:
                edges.append(newEdgeWithNodes(node, anotherNode, massTable))
    return edges, nodes

def newEdgeWithNodes(node, anotherNode, massTable):
    diff = node.base - anotherNode.base
    if diff < 0:
        start = node.base; end = anotherNode.base;
        node.addOut(anotherNode); anotherNode.addIn(node)
    else:
        start = anotherNode.base; end = node.base;
        anotherNode.addOut(node); node.addIn(anotherNode)
    label = ""
    for k,v in massTable.items():
        if v == abs(diff):
            label = k
            break
    return edge.LabeledEdge(start, end, label)