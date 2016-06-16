import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))

import directedGraph as dG
import equalitySet as eS

class NodeWithGaps(dG.Node):
	def __init__(self, base, pairBase):
		super(NodeWithGaps, self).__init__(base)
		self.pairBase = pairBase
	
	def __str__(self):
		return "" + str(self.base) + "|" + str(self.pairBase)

	def __repr__(self):
		return ",".join(map(str,self.ins)) + " -> " + str(self.base) + "|" + str(self.pairBase) + " -> " + ",".join(map(str,self.outs))

	def __key(self):
		return (self.base, self.pairBase)

	def __hash__(self):
		return hash(self.__key())

	def __eq__(self, other):
		if not isinstance(other, NodeWithGaps):
			return NotImplemented
		return self.__key() == other.__key()

def parseLineToValues(x):
	prefix = x[:-1]
	suffix = x[1:]
	nodeValue = prefix
	out = suffix
	return (nodeValue, out)

def parseAsGraphSet(lines):
	nodes = set()
	for line in lines:
		base, pair = line.split('|')
		nodeValue, outValue = parseLineToValues(base)
		nodePair, outPair = parseLineToValues(pair)
		lineGraphParser(nodeValue, nodePair, outValue, outPair, nodes)
	return nodes

def lineGraphParser(nodeValue, nodePair, outValue, outPair, nodes):
	node = nodeFromSet(nodeValue, nodePair, nodes)
	def applyOutNode(outValue, outPair, nodes, inNode):
		outNode = nodeFromSet(outValue, outPair, nodes)
		outNode.addIn(inNode)
		return outNode
	nodeOut = applyOutNode(outValue, outPair, nodes, node)
	node.addOut(nodeOut)

def nodeFromSet(nodeValue, nodePair, nodes):
	node = NodeWithGaps(nodeValue, nodePair)
	return eS.itemFromSet(node, nodes)

#print info
def nodesPathToLine(path, k, d):
	return mergePrefixAndSuffix(prefixAndSuffixFromPath(path), k, d)

def prefixAndSuffixFromPath(path):
	node = path
	prefixString = str(node.base)
	suffixString = str(node.pairBase)
	while True:
		if len(node.outs) == 0:
			break
		node = node.outs[0]
		prefixString += str(node.base[-1])
		suffixString += str(node.pairBase[-1])
		if node is path:
			break
	print "prefix", prefixString
	print "sufix", suffixString
	return (prefixString, suffixString)

def mergePrefixAndSuffix((prefixString, suffixString), k, d):
	for x in xrange(k + d, len(prefixString)):
		if prefixString[x] != suffixString[x - k - d]:
			return "Error"
	return prefixString + suffixString[ -(k + d):]
