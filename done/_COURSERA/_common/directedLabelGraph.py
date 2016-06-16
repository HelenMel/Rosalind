import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))

import equalitySet as eS

class NodeLabel(object):
    """node of ACGT graph"""
    def __init__(self, base, label):
        super(NodeLabel, self).__init__()
        self.base = base
        self.label = label

    def __str__(self):
        return "" + str(self.base)+ " : " + str(self.label)

    def __repr__(self):
        return str(self.base) + " : " + str(self.label)

    def __key(self):
        return (self.base)

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        if not isinstance(other, NodeLabel):
            return NotImplemented
        return self.__key() == other.__key()

def labelNodeFromSet(nodeValue, labels):
    newLabelNode = NodeLabel(nodeValue, "@!$")
    return eS.itemFromSet(newLabelNode, labels)