import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_6')))

import trieGraph as tG

def trieNodesFromPatterns(Patterns):
    Trie, root = trieNodesFromPatterns(Patterns)
    return Trie

def trieNodesAndRootFromPatterns(Patterns):
    nodeNumber = 0
    root = tG.TrieNode(nodeNumber, None, "-")
    Trie = []
    nodeNumber += 1
    for Pattern in Patterns:
        currentNode = root
        for symbol in Pattern:
            edge = tG.findEdge(currentNode, symbol)
            if edge is None:
                newNode = tG.TrieNode(nodeNumber, currentNode, symbol)
                Trie.append(newNode)
                currentNode.addOut(newNode)
                currentNode = newNode
                nodeNumber += 1
            else:
                currentNode = edge
    return Trie, root
