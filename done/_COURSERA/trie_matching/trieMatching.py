import sys, os
import copy
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_6')))

import trieGraph as tG

def trieMatching(Text, Trie, root):
    Text_ = copy.copy(Text)
    matchedIndexes = []
    i = 0
    while i < len(Text):
        match = prefixTrieMatching(Text_, Trie, root)
        if match is not None:
            matchedIndexes.append(i)
        i += 1
        Text_ = Text_[1: ]
    return matchedIndexes

def prefixTrieMatching(Text, Trie, root):
    s_i = 0
    symbol = Text[s_i]
    s_i += 1
    v = root
    while True:
        if v.isLeaf():
            return patternSpelledFromRootToLeaf(Trie, v)
        edge = tG.findEdge(v, symbol)
        if edge is not None:
            if s_i < len(Text):
                symbol = Text[s_i]
            s_i += 1
            v = edge
        else:
            return None 

def patternSpelledFromRootToLeaf(Trie, v):
    pattern = ""
    node = v
    while not node.isRoot():
        pattern += node.incomeLetter
        node = node.parent
    return pattern[::-1]