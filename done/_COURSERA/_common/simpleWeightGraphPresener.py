import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))

import directedGraph as dG
import simpleGraphWeight as sGW

def parseLineWithWeightToValues(x):
    node, outN = x.split("->")
    out, weightN = outN.split(":")
    weight = float(weightN)
    return (int(node), int(out), weight)

def parseLineStringWithWeightToValues(x):
    node, outN = x.split(" -> ")
    out, weightN = outN.split(": ")
    weight = float(weightN)
    return (str(node), str(out), weight)

def parseAsGraphSet(lines):
    return parseAsGraphSetWithParseFunction(lines, parseLineWithWeightToValues)

def parseAsLineGraphSet(lines):
    return parseAsGraphSetWithParseFunction(lines, parseLineStringWithWeightToValues)

def parseAsGraphSetWithParseFunction(lines, parseFunction):
    nodes = set()
    weights = set()
    for line in lines:
        nodeName, out, weight = parseFunction(line)
        node = dG.nodeFromSet(nodeName, nodes)
        outNode = dG.nodeFromSet(out, nodes)
        node.addOut(outNode)
        outNode.addIn(node)
        w = sGW.weightFromSet(node, outNode, weights)
        w.weight = weight
    return (nodes, weights)

