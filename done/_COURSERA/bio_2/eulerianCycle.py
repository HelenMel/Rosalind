import sys, os
import copy
import random
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))

import directedGraph as dG
import equalitySet as eS

def findEulerianPath(Graph):
	completedGraph, endNode, startNode = addExtraEdgesToCompleteGraph(Graph)
	pathStart = findEulerianCycle(completedGraph)
	pathStart, pathEnd = removeExtraEdgesToMakePath(pathStart, endNode, startNode)
	return pathStart

def findEulerianCycle(Graph):
	node = next(iter(Graph))
	#node = random.sample(Graph, 1)[0]
	pathStart = copy.copy(node)
	pathStart.ins = []
	pathStart.outs = []
	nextToStart = None

	while len(Graph) > 0:
		pathEnd = findCycle(node, pathStart, Graph)
		pathEnd = closeCycle(pathEnd, pathStart, nextToStart)
		if len(Graph) == 0:
			break;
		pathStart = newPathStart(Graph, pathStart)
		node = eS.itemFromSet(pathStart, Graph)
		nextToStart = pathStart.outs
	return pathStart

def findCycle(node, pathStart, Graph):
	pathEnd = pathStart
	while len(node.outs) > 0:
		nextNode = node.outs.pop(0)
		if len(node.outs) == 0:
			Graph.remove(node)
		newPathEnd = copy.copy(nextNode)
		newPathEnd.outs = []
		newPathEnd.ins = [ pathEnd ]
		pathEnd.outs = [ newPathEnd ]
		node = nextNode
		pathEnd = newPathEnd
	assert (pathStart.base == pathEnd.base), "Start " + str(pathStart) + " and end " + str(pathEnd) + " should be equal"
	return pathEnd

def closeCycle(pathEnd, pathStart, nextToStart):
	if nextToStart is None:
		pathEnd.outs = pathStart.outs
	else:
		pathEnd.outs = nextToStart
	return pathEnd

def newPathStart(Graph, pathStart):
	newStart = pathStart.outs[0]
	while True:
		if newStart in Graph:
			break;
		newStart = newStart.outs[0]
		if newStart is pathStart:
			break;
	return newStart

def addExtraEdgesToCompleteGraph(Graph):
	endNodes, startNodes = dG.nodesWithUnequalInAndOut(Graph)
	if len(endNodes) > 1:
		print "Too much nodes with edges IN > OUT"
	if len(startNodes) > 1:
		print "Too much nodes with edges OUT < IN"
	endNode = endNodes[0]
	startNode = startNodes[0]
	endNode.addOut(startNode)
	startNode.addIn(endNode)
	return (Graph, endNode, startNode)

def removeExtraEdgesToMakePath(cycleStart, endNode, startNode):
	currentNode = cycleStart
	newStart = None
	newEnd = None
	while True:
		if currentNode == startNode:
			if currentNode.ins[0] == endNode:
				newEnd = currentNode.ins[0]
				currentNode.ins = []
				newEnd.outs = []
				newStart = currentNode
				break
		currentNode = currentNode.outs[0]
		if currentNode is cycleStart:
			break;
	return (newStart, newEnd)
