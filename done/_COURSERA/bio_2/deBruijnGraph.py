import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))

import simpleGraph as sG
import equalitySet as eS

def deBruijn(Text, k):
	nodes = set()
	for i in xrange(0, len(Text) - k + 1):
		addNodeAndEdgeToSet(nodeAndEdgeFromText(Text[i : i + k]), nodes)
	return sortedNodes(nodes)

def deBruijnFromList(list):
	nodes = set()
	for Text in list:
		addNodeAndEdgeToSet(nodeAndEdgeFromText(Text), nodes)
	return sortedNodes(nodes)

def nodeAndEdgeFromText(Text):
	base = Text[ : - 1]
	edge = Text[1: ]
	node = sG.Node(base)
	return (node, edge)

def addNodeAndEdgeToSet((node, edge), nodes):
	eqNode = eS.Grab(node)
	if eqNode in nodes:
		eqNode.match.addEdge(edge)
	else:
		node.addEdge(edge)
		nodes.add(node)

def sortedNodes(nodes):
	sortedNodes = list(nodes)
	sortedNodes.sort(key = lambda c: c.base)
	return sortedNodes
	




		