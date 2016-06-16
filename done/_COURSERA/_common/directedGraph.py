import sys, os
import copy
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))

import equalitySet as eS

class Node(object):
	"""node of ACGT graph"""
	def __init__(self, base):
		super(Node, self).__init__()
		self.base = base
		self.ins = []
		self.outs = []

	def addOut(self, out):
		self.outs.append(out)

 	def addIn(self, inx):
		self.ins.append(inx)

	def isOneInOut(self):
		return ((len(self.ins) == 1) and (len(self.outs) == 1))

	def __str__(self):
		return "" + str(self.base)

	def __repr__(self):
		return ",".join(map(str,self.ins)) + " -> " + "<node>" + str(self.base) + "/<node>" + " -> " + ",".join(map(str,self.outs))

	def __hash__(self):
		return hash(self.base)

	def __eq__(self, other):
		if not isinstance(other, Node):
			return NotImplemented
		return self.base == other.base

def pathNode(node):
	newPathNode = copy.copy(node)
	newPathNode.ins = []
	newPathNode.outs = []
	return newPathNode

def nodesWithUnequalInAndOut(nodes):
	moreIn = []
	moreOut = []
	for node in nodes:
		if len(node.ins) != len(node.outs):
			if len(node.ins) > len(node.outs):
				moreIn.append(node)
			else:
				moreOut.append(node)
	return (moreIn, moreOut)

def nodeFromSet(nodeValue, nodes):
	node = Node(nodeValue)
	return eS.itemFromSet(node, nodes)

def moveToValue(nodeValue, path):
	node = path
	while True:
		if node.base == nodeValue:
			return node
		node = node.outs[0]
		if node is path:
			break
	return node

# INPUT
def parseLineToValues(x):
	nodeValue, outN = x.split(" -> ")
	outs = outN.split(",")
	return (nodeValue, outs)

def parseAsGraphSet(lines):
	nodes = set()
	for line in lines:
		nodeValue, outs = parseLineToValues(line)
		lineGraphParser(nodeValue, outs, nodes)
	return nodes

def lineGraphParser(nodeValue, outs, nodes):
	# its wrong to think, that that should be int
	node = nodeFromSet(int(nodeValue), nodes)
	def applyOutNode(outValue, nodes, inNode):
		outNode = nodeFromSet(outValue, nodes)
		outNode.addIn(inNode)
		return outNode
	nodesOut = [applyOutNode(int(out), nodes, node) for out in outs]
	node.outs.extend(nodesOut)

#OUTPUT
def nodesPathToLine(path):
	node = path
	line = str(node.base)
	while True:
		if len(node.outs) == 0:
			break
		node = node.outs[0]
		line += " -> " + str(node.base)
		if node is path:
			break
	return line

	
