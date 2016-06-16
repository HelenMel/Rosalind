import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))

import equalitySet as eS

class Node(object):
	"""node of ACGT graph"""
	def __init__(self, base):
		super(Node, self).__init__()
		self.base = base
		self.edges = []

	def addEdge(self, edge):
		self.edges.append(edge)

	def __str__(self):
		return "" + str(self.base)

	def __repr__(self):
		return "" + str(self.base) + " -> " + ",".join(map(str,self.edges))

	def __hash__(self):
		return hash(self.base)

	def __eq__(self, other):
		if not isinstance(other, Node):
			return NotImplemented
		return self.base == other.base

# may be parsing is not exactly this class responsibility
def parseLineToValues(x):
	inN, outN = x.split(" -> ")
	outs = outN.split(",")
	return (inN, outs)

def nodeFromSet(nodeValue, nodes):
	node = Node(nodeValue)
	eqNode = eS.Grab(node)
	if eqNode in nodes:
		return eqNode.match
	else:
		nodes.add(node)
		return node

def parseAsGraphSet(lines):
	nodes = set()
	for line in lines:
		inN, outs = parseLineToValues(line)
		node = nodeFromSet(int(inN), nodes)
		nodesOut = [nodeFromSet(int(out), nodes) for out in outs]
		node.edges = nodesOut
	return nodes

def nodesPathToLine(path):
	node = path
	line = str(node.base)
	while len(node.edges) > 0:
		node = node.edges.pop()
		line += "->" + str(node.base)
	return line
	
