import sys, os
import copy
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_6')))

import trieGraph as tG

def longestRepeatProblem(Trie, root):
    maxNode = root
    maxLength = 0
    for out in root.outs:
        if len(out.outs) > 1:
            node_, length = outLength(out, 0)
            if length > maxLength:
                maxLength = length
                maxNode = node_
    s = [maxNode]
    while maxNode.parent is not root:
        maxNode = maxNode.parent
        s.insert(0, maxNode)
    return s

def outLength(node, length):
    maxNode = node
    nodeLength = length + node.length
    maxLength = nodeLength
    for out in node.outs:
        if len(out.outs) > 1:
            node_, length = outLength(out, nodeLength)
            if length > maxLength:
                maxLength = length
                maxNode = node_
    return maxNode, maxLength         
    