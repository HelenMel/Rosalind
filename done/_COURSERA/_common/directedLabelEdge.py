import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))

import equalitySet as eS

class LabeledEdge(object):
    """node of ACGT graph"""
    def __init__(self, start, end, label):
        super(LabeledEdge, self).__init__()
        self.start = start
        self.end = end
        self.label = label

    def __str__(self):
        return "" + str(self.start) + " -> " + str(self.end) + ":" + str(self.label)

    def __repr__(self):
        return str(self.start) + " -> " + str(self.end) + ":" + str(self.label)

    def __key(self):
        return (self.start, self.end)

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        if not isinstance(other, LabeledEdge):
            return NotImplemented
        return self.__key() == other.__key()

def edgeFromSet(start, end, edges):
    edge = LabeledEdge(start, end, "")
    return eS.itemFromSet(edge, edges)