import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))

import directedGraph as dG

def parseLineToValues(x):
	prefix = x[:-1]
	suffix = x[1:]
	nodeValue = prefix
	outs = [suffix]
	return (nodeValue, outs)

def parseAsGraphSet(lines):
	nodes = set()
	for line in lines:
		nodeValue, outs = parseLineToValues(line)
		lineGraphParser(nodeValue, outs, nodes)
	return nodes

def lineGraphParser(nodeValue, outs, nodes):
	node = dG.nodeFromSet(nodeValue, nodes)
	def applyOutNode(outValue, nodes, inNode):
		outNode = dG.nodeFromSet(outValue, nodes)
		outNode.addIn(inNode)
		return outNode
	nodesOut = [applyOutNode(out, nodes, node) for out in outs]
	node.outs.extend(nodesOut)

#print info
def nodesPathToLine(path):
	node = path
	line = str(node.base)
	while True:
		if len(node.outs) == 0:
			break
		node = node.outs[0]
		line += str(node.base[-1])
		if node is path:
			break
	return line