import sys, os
import copy
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_6')))

import suffixTreeConstruction as sTC
import trieGraph as tG

def nodesCount(Text):
    Tree, root = sTC.modifiedSuffixTreeConstructionWithRoot(Text)
    print "tree is found"
    C = set(Tree)
    count = 0
    for node in C:
        if node.label != -1 and node != root:
            count += 1
    print "Count", count

    print "Failed Color count ", len(C), " Tree count ", len(Tree)

def leafsColors(Tree, root, maxIndexText1):
    Color = { root : undefinedColor() }
    for node in Tree:
        if node.label == -1:
            Color[node] = undefinedColor()
        elif node.label <= maxIndexText1:
            Color[node] = text1Color()
        else:
            Color[node] = text2Color()
    print "Failed Color count ", len(Color), " Tree count ", len(Tree)
    return Color

def treeColoring(Tree, root, Color):
    ToCheck = {k: v for k, v in Color.items() if v == undefinedColor()}
    while len(ToCheck) > 0:
        ToCheck_ = copy.copy(ToCheck)
        for node, value in ToCheck.iteritems():
            node2 = None
            if node == root:
                node2 = root
            else:
                node2 = tG.labeledNodeFromSet(node.base, node.parent, node.incomeLetter, node.label, Tree)
            color = defineNodeColor(node2, Color)
            if color != undefinedColor():
                Color[node] = color
                if node in ToCheck_:
                    del ToCheck_[node]
                if node == root:
                    return
        ToCheck = ToCheck_
        
def defineNodeColor(node, Color):
    color = undefinedColor()
    if node.base == 22:
        print "node", [node], node.length, node.outs
        print "node id", hex(id(node))
    for childNode in node.outs:
        if node.base == 22:
            print "22:> child ", childNode, " color", Color[childNode]
        childColor = Color[childNode]
        if childColor == undefinedColor():
            if node.base == 22:
                print "22:> undefined color"
            return undefinedColor()
        if color != childColor and color != bothTextColor():
            if color == undefinedColor():
                color = childColor
            else:
                color = bothTextColor()
                break
    if node.base == 22:
        print "22:> result color", color
    return color

# presentation
def text1Color():
    return "blue"

def text2Color():
    return "red"

def bothTextColor():
    return "purple"

def undefinedColor():
    return "grey"


def summ(k, n, limit):
    X = [0] * limit
    Z = [0] * limit
    for y in xrange(1, limit):
        X[y] = X[y - 1] + k
        Z[y] = Z[y - 1] + n
    print X
    print Z
    count = 0
    for i in xrange(0, limit):
        for j in xrange(0, limit):
            s = X[i] + Z[j]
            if s == limit:
                count += 1
    return count

