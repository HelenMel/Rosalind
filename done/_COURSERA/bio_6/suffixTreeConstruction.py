import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_6')))

import trieGraph as tG
import suffixTrieConstruction as sTC

def modifiedSuffixTreeConstruction(Text):
    Tree, root = modifiedSuffixTreeConstructionWithRoot(Text)
    return Tree

def modifiedSuffixTreeConstructionWithRoot(Text):
    Trie, root = sTC.modifiedSuffixTrieConstruction(Text)
    paths = maximalNonBranchingPath(Trie, root)
    newTrie = set()
    for path in paths:
        start = path[0]
        end = path[-1]
        if start.base == 22:
            print "22> as path start", path
        if end.base == 22:
            print "22> as path end", path
        if start in newTrie:
            start.outs += end.outs
        else:
            start.outs = end.outs
        for out in end.outs:
            out.parent = start
        start.label = end.label
        start.length = len(path)
        newTrie.add(start)
    return newTrie, root

def nodeStringFromText(node, Text):
    i = node.base
    return Text[i: i + node.length]

def maximalNonBranchingPath(Trie, root):
    paths = []
    Nodes = [root] + Trie
    for node in Nodes:
        if not node.isOneOut():
            if len(node.outs) > 0:
                for edge in node.outs:
                    NonBranchingPath = [edge]
                    w = edge
                    while w.isOneOut():
                        NonBranchingPath.append(w.outs[0])
                        w = w.outs[0]
                    paths.append(NonBranchingPath)
    return paths