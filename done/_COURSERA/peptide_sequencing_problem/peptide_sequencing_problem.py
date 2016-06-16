import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_4')))

import directedGraph as dG
import nucleotides as info
import peptide_into_vector as pepV

def peptideSequencingProblemRun(spectrumVector):
    return peptideSequencingProblem(spectrumVector, info.massIntTable())

def peptideSequencingProblem(spectrumVector, massTable):
    massSet = set(massTable.values())
    minMass = min(massSet)
    orderedNodes = spectrumToGraph(len(spectrumVector), massTable)
    Weights = weightsFromSpectrum(spectrumVector, orderedNodes)
    S, Backtrace = backtraceOrderedNodes(orderedNodes, Weights, minMass)
    source = orderedNodes[0]
    path = pathFormBacktrace(Backtrace, source, orderedNodes)
    peptideVector = pathToPeptideVector(path, len(spectrumVector))
    Peptide = pepV.vectorIntoPeptide(peptideVector, massTable)
    return Peptide

def pathToPeptideVector(path, spectrumLength):
    peptideVector = [0] * (spectrumLength + 1)
    for node in path:
        peptideVector[node.base] = 1
    return peptideVector[1:]


def spectrumToGraph(spectrumLength, massTable):
    massSet = set(massTable.values())
    minMass = min(massSet)
    nodes = []
    for i in xrange(0, spectrumLength + 1):
        # node base got its index in spectrum and in Weight array
        node = dG.Node(i)
        nodes.append(node)
        if i >= minMass:
            for mass in massSet:
                j = i - mass
                if j >= 0:
                    startNode = nodes[j]
                    # do we need out?
                    node.addIn(startNode)
    return nodes

def weightsFromSpectrum(spectrumVector, nodes):
    Weights = { 0 : 0 }
    for node in nodes:
        if node.base == 0:
            continue
        Weights[node.base] = spectrumVector[node.base - 1]
    return Weights

def backtraceOrderedNodes(orderedNodes, Weights, minMass):
    Backtrace = orderedNodes[:minMass]
    S = [float('-inf')] * minMass
    S[0] = 0
    for i in xrange(minMass, len(orderedNodes)):
        node = orderedNodes[i]
        def nodeWeight(nodeIn, node):
            index = nodeIn.base
            w = Weights[node.base]
            Sn = S[index] + w
            return (nodeIn, Sn)
        Distances = [nodeWeight(n, node) for n in node.ins]
        maxNode = max(Distances, key=lambda x: x[1])
        Backtrace.append((maxNode[0]))
        S.append(maxNode[1])
    print S
    print Backtrace
    return S, Backtrace

def pathFormBacktrace(Backtrace, source, ordered):
    nextIndex = -1
    nextNode = None
    path = [ ordered[-1] ]
    while nextNode != source:
        nextNode = Backtrace[nextIndex]
        path.insert(0, nextNode)
        nextIndex = nextNode.base
    return path

fakeMassTable = { "X":4, "Z":5 }
SpectrumVector = [0,0,0,4,-2,-3,-1,-7,6,5,3,2,1,9,3,-8,0,3,1,2,1,8]
#print spectrumToGraph(SpectrumVector, fakeMassTable)
print peptideSequencingProblem(SpectrumVector, fakeMassTable)