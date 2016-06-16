import sys, os
import copy
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_6')))

import suffixTreeConstruction as sTC
import coloredTree as cT
import trieGraph as tG

def shortestNonSharedSubstring(Text1, Text2):
    Text = combineString(Text1, Text2)
    Tree, root = sTC.modifiedSuffixTreeConstructionWithRoot(Text)
    #print "tree is found", Tree
    Color = cT.leafsColors(Tree, root, len(Text1))
    cT.treeColoring(Tree, root, Color)
    #print "tree is coloring", Color
    minNode = shortestNode(Tree, Color, Text, root)
    return tG.pathFromNodeToRoot(minNode, root)

def shortestNode(Tree, Color, Text, root):
    minNode = root
    minLength = len(Text)
    outs = root.outs
    while len(outs) > 0:
        outs_ = []
        for node in outs:
            outs_ = outs_ + node.outs
            name = fittingName(Color, node, Text, root)
            if name is None:
                continue
            if len(name) < minLength:
                minLength = len(name)
                minNode = node
        if minLength < len(Text):
            return minNode
        else:
            outs = outs_
    return minNode

def fittingName(Color, node, Text, root):
    if Color[node] != cT.bothTextColor():
        nodeName, color = nodeDescription(node, Color, Text)
        if node.length > validNodeLength(node, root):
            print "parent", [node.parent], " c ", Color[node.parent]
            print "node", [node], " c ", Color[node]
            print "node id", hex(id(node))
            for childNode in node.outs:
                print "child ", [childNode], " c ", Color[childNode]

            return validColorName(nodeName)
    return None

# node description include node string and node color
def nodeDescription(node, Color, Text):
    nodeName = sTC.nodeStringFromText(node, Text)
    color = Color[node]
    return (nodeName, color)

def validNodeLength(node, root):
    if node.parent == root:
        return 1
    return 0

def validColorName(name):
    if separatorLetter() not in name and finishLetter() not in name:
            return name
    return None

def combineString(Text1, Text2):
    return Text1 + separatorLetter() + Text2 + finishLetter()

def separatorLetter():
    return "#" 

def finishLetter():
    return "$"

