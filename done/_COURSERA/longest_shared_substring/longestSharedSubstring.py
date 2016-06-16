import sys, os
import copy
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_6')))

import suffixTreeConstruction as sTC
import coloredTree as cT

def longestSharedSubstring(Text1, Text2):
    Text = combineString(Text1, Text2)
    Tree, root = sTC.modifiedSuffixTreeConstructionWithRoot(Text)
    print "tree is found"
    Color = cT.leafsColors(Tree, root, len(Text1))
    cT.treeColoring(Tree, root, Color)
    print "tree is coloring"
    return longestBothPath(Color, root)

def combineString(Text1, Text2):
    return Text1 + "#" + Text2 + "$"

def longestBothPath(Color, root):
    maxNode = root
    maxLength = 0
    for out in root.outs:
        if Color[out] == cT.bothTextColor():
            node_, length = outLength(out, 0, Color)
            if length > maxLength:
                maxLength = length
                maxNode = node_
    s = [maxNode]
    while maxNode.parent is not root:
        maxNode = maxNode.parent
        s.insert(0, maxNode)
    return s
    
def outLength(node, length, Color):
    maxNode = node
    nodeLength = length + node.length
    maxLength = nodeLength
    for out in node.outs:
        if Color[out] == cT.bothTextColor():
            node_, length = outLength(out, nodeLength, Color)
            if length > maxLength:
                maxLength = length
                maxNode = node_
    return maxNode, maxLength 

#print longestSharedSubstring("ma", "TTGAATGACTCCTATAACGAACTTCGACATGGCA")