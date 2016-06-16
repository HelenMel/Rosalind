import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_6')))

import trieGraph as tG

def modifiedSuffixTrieConstruction(Text):
    nodeNumber = 0
    root = tG.TrieNode(-100, None, "-")
    Trie = []
    for i in xrange(0, len(Text) - 1):
        currentNode = root
        for j in xrange(i, len(Text) - 1):
            symbol = Text[j]
            edge = tG.findEdge(currentNode, symbol)
            if edge is not None:
                currentNode = edge
            else:
                newNode = tG.LabeledTrieNode(j, currentNode, symbol)
                Trie.append(newNode)
                currentNode.addOut(newNode)
                currentNode = newNode
        if currentNode.isLeaf:
            newNode = tG.LabeledTrieNode(len(Text) - 1, currentNode, textEnd(), i)
            Trie.append(newNode)
            currentNode.addOut(newNode)
    # adding last node
    newNode = tG.LabeledTrieNode(len(Text) - 1, root, textEnd(), len(Text) - 1)
    Trie.append(newNode)
    root.addOut(newNode)
    return Trie, root

def textEnd():
    return "$"

#Trie, root = modifiedSuffixTrieConstruction("CCAAGCTGCT#CATGCTGGGC$")
#print Trie