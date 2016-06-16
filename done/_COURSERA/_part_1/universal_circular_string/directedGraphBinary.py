import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_2')))

from itertools import product
import directedGraphString as dGS
import directedGraph as dG

def generateBinaryArrayLength(k):
	return [ ''.join(x) for x in product('01', repeat=k) ]

def generateBinaryGraphSet(k):
	lines = generateBinaryArrayLength(k)
	return dGS.parseAsGraphSet(lines)

def nodesPathToLine(nodes, k):
	startNode = dG.moveToValue(("0" * (k - 1)), nodes)
	print " NEW Start", startNode
	node = startNode
	line = str(node.base)
	while True:
		if len(node.outs) == 0:
			break
		node = node.outs[0]
		line += str(node.base[-1])
		if node.outs[0] is startNode:
			break
	return line
