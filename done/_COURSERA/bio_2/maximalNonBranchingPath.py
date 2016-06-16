import sys, os
import copy
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))

import directedGraph as dG

def maximalNonBranchingPath(Graph):
	paths = []
	unvisitedNodes = copy.copy(Graph)
	for node in Graph:
		if not node.isOneInOut():
			if len(node.outs) > 0:
				removeNode(node, unvisitedNodes)
				for outNode in node.outs:
					pathStart = dG.pathNode(node)
					pathEnd = pathStart
					pathEnd = newPathEnd(pathEnd, outNode, unvisitedNodes)
					shouldContinue = outNode.isOneInOut()
					while shouldContinue:
						if len(pathEnd.outs) == 0:
							break;
						shouldContinue = pathEnd.outs[0].isOneInOut()
						pathEnd = newPathEnd(pathEnd, pathEnd.outs[0], unvisitedNodes)
					pathEnd.outs = []
					paths.append(pathStart)
	shouldContinue = len(unvisitedNodes) != 0
	while shouldContinue:
		pathStart = findCycleFromNodes(unvisitedNodes)
		paths.append(pathStart)
		shouldContinue = len(unvisitedNodes) != 0
	return paths

def findCycleFromNodes(unvisitedNodes):
	node = next(iter(unvisitedNodes))
	removeNode(node, unvisitedNodes)
	pathStart = copy.copy(node)
	pathStart.ins = []
	pathEnd = pathStart
	while True:
		pathEnd = newPathEnd(pathEnd, pathEnd.outs[0], unvisitedNodes)
		if pathEnd.outs[0] is node:
			pathEnd.outs = [ pathStart ]
			pathStart.ins = [ pathEnd ]
			break;
	return pathStart

def newPathEnd(pathEnd, node, unvisitedNodes):
	removeNode(node, unvisitedNodes)
	newPathEnd = copy.copy(node)
	newPathEnd.ins = [ pathEnd ]
	pathEnd.outs = [ newPathEnd ]
	return newPathEnd

def removeNode(node, nodes):
	if node in nodes:
		nodes.remove(node)
