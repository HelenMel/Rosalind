import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))

import directedGraph as dG
import equalitySet as eS

class NodsWeight(object):
	"""node of ACGT graph"""
	def __init__(self, node1, node2, weight):
		super(NodsWeight, self).__init__()
		self.node1 = node1
		self.node2 = node2
		self.weight = weight

	def mirrorNode(self):
		return NodsWeight(self.node2, self.node1, self.weight)

	def show(self):
		return str(self.node1) + "->" + str(self.node2) + ":" + format(self.weight, '.0f')

	def __str__(self):
		return "" + str(self.node1) + " - " + str(self.node2) + " = " + str(self.weight)

	def __repr__(self):
		return str(self.node1) + " - " + str(self.node2) + " = " + str(self.weight)

	def __hash__(self):
		return hash(self.node1) ^ hash(self.node2)

	def __eq__(self, other):
		if not isinstance(other, NodsWeight):
			return NotImplemented
		if self.node1 == other.node1 and self.node2 == other.node2:
			return True
		if self.node1 == other.node2 and self.node2 == other.node1:
			return True
		return False

def weightFromSet(node1, node2, weights):
	weight = NodsWeight(node1, node2, 1.0)
	return eS.itemFromSet(weight, weights)