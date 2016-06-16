import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))

import directedGraph as dG
import equalitySet as eS

class NodsWeight(object):
    """node of ACGT graph"""
    def __init__(self, start, end, weight):
        super(NodsWeight, self).__init__()
        self.start = start
        self.end = end
        self.weight = weight

    def __str__(self):
        return "" + str(self.start) + " -> " + str(self.end) + " = " + str(self.weight)

    def __repr__(self):
        return str(self.start) + " -> " + str(self.end) + " = " + str(self.weight)

    def __key(self):
        return (self.start, self.end)

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        if not isinstance(other, NodsWeight):
            return NotImplemented
        return (self.start == other.start) and (self.end == other.end)

def weightFromSet(start, end, weights):
    weight = NodsWeight(start, end, 1.0)
    return eS.itemFromSet(weight, weights)