import sys, os
import time
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_3')))

import scoringMatrix as sM
from bio_3 import middle_edge as mE

def linear_space_alignment_run(v, w):
    scoreTable = sM.defaultMatrix()
    return linear_space_alignment(v, w, 0, len(v), 0, len(w), scoreTable)

def linear_space_alignment(v, w, top, bottom, left, right, scoreTable):
    if left == right:
        return v[top: bottom], "-" * len(v[top: bottom]), 0
    if top == bottom:
        return "-" * len(w[left: right]), w[left: right], 0
    midNode, nextNode, length = mE.middle_edge(v, w, top, bottom, left, right, scoreTable)
    out1L, out2L, _ = linear_space_alignment(v, w, top, midNode[0], left, midNode[1], scoreTable)
    edge = nodesToEdge(midNode, nextNode)
    out1M, out2M = edgeToLetter(edge, v, w, nextNode)
    out1R, out2R, _ = linear_space_alignment(v, w, nextNode[0], bottom, nextNode[1], right, scoreTable)
    out1 = out1L + out1M + out1R
    out2 = out2L + out2M + out2R
    if isLastIteration(v, w, top, bottom, left, right):
        return out1, out2, length
    return out1, out2, 0

def isLastIteration(v, w, top, bottom, left, right):
    if top == 0 and bottom == len(v) and left == 0 and right == len(w):
        return True
    return False

def nodesToEdge(node1, node2):
    if node1[0] + 1 == node2[0] and node1[1] + 1 == node2[1]:
        return diagonalB()
    if node1[0] == node2[0] and node1[1] + 1 == node2[1]:
        return rightB()
    if node1[1] == node2[1] and node1[0] + 1 == node2[0]:
        return downB()
    assert False

def edgeToLetter(edge, v, w, midNode):
    if edge == diagonalB():
        return v[midNode[0] - 1], w[midNode[1] - 1]
    elif edge == rightB():
        return "-", w[midNode[1] - 1]
    elif edge == downB():
        return v[midNode[0] - 1], "-"

def downB():
    return "|"

def rightB():
    return "->"

def diagonalB():
    return '\\'

#print middle_edge_run("PLEASANTLY", "MEASNLY")
#print linear_space_alignment_run("PLEASANTLY", "MEANLY")