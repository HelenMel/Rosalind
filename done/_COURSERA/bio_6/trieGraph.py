import sys, os
import copy
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))

import equalitySet as eS

class TrieNode(object):
	"""node of Trie graph"""
	def __init__(self, base, parent, incomeLetter):
		super(TrieNode, self).__init__()
		self.base = base
		self.incomeLetter = incomeLetter
		self.parent = parent
		self.outs = []

	def addOut(self, out):
		self.outs.append(out)

	def isLeaf(self):
		return len(self.outs) == 0

	def isOneOut(self):
		return (len(self.outs) == 1)

	def isRoot(self):
		return (self.parent is None)

	def __str__(self):
		return "" + str(self.base) + ":" + self.incomeLetter

	def __repr__(self):
		if self.parent is None:
			return "ROOT:"+ str(self.base) + ":" + self.incomeLetter
		return str(self.parent.base) + "->" + str(self.base) + ":" + self.incomeLetter

	def __key(self):
		if self.parent is None:
			return (self.base, self.incomeLetter)
		return (self.base, self.incomeLetter, self.parent.base)

	def __hash__(self):
		return hash(self.__key())

	def __eq__(self, other):
		if not isinstance(other, TrieNode):
			return NotImplemented
		return self.__key() == other.__key()

	def show(self):
		if self.parent is None:
			return "ROOT:"+ str(self.base) + "," + self.incomeLetter
		return str(self.parent.base) + "->" + str(self.base) + ":" + self.incomeLetter

class LabeledTrieNode(TrieNode):
	"""docstring for LabeledTrieNode"""
	def __init__(self, base, parent, incomeLetter, label = -1, length = 0):
		super(LabeledTrieNode, self).__init__( base, parent, incomeLetter)
		self.label = label
		self.length = length

	def __key(self):
		if self.parent is None:
			return (self.base, self.incomeLetter, self.label)
		return (self.base, self.incomeLetter, self.parent.base, self.label)

	def __hash__(self):
		return hash(self.__key())

	def __eq__(self, other):
		if not isinstance(other, LabeledTrieNode):
			return NotImplemented
		return self.__key() == other.__key()

	def __str__(self):
		return "" + str(self.base) + ":" + self.incomeLetter + "(" + str(self.label) + ")"

	def __repr__(self):
		if self.parent is None:
			return "ROOT:"+ str(self.base) + "," + self.incomeLetter
		return str(self.parent.base) + "->" + str(self.base) + "," + self.incomeLetter + "(" + str(self.label) + ")" + "L" + str(self.length)

	def show(self):
		if self.parent is None:
			return "ROOT:"+ str(self.base) + "," + self.incomeLetter
		return str(self.parent.base) + "->" + str(self.base) + "," + self.incomeLetter + "(" + str(self.label) + ")" + "L" + str(self.length)

def findEdge(node, symbol):
    for out in node.outs:
        if out.incomeLetter == symbol:
            return out
    return None

def labeledNodeFromSet(base, parent, incomeLetter, label, nodes):
	node = LabeledTrieNode(base, parent, incomeLetter, label)
	return eS.itemFromSet(node, nodes)

def pathFromNodeToRoot(node, root):
    s = [node]
    while node.parent is not root:
        node = node.parent
        s.insert(0, node)
    return s

def pathFromNodeToLeafs(node, nodeManipulation):
	nodeManipulation(node)
	for outNode in node.outs:
		pathFromNodeToLeafs(outNode, nodeManipulation)
