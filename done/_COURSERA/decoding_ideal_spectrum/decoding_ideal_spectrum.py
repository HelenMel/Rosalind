import sys, os
import copy
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_4')))

import spectrum_graph
import directedLabelEdge as dLE
import directedGraph as dG
import nucleotides as info

def decodingIdealSpectrum(Spectrum):
    massTable = info.massIntTable()
    nodes = spectrum_graph.parseLineToNodes(Spectrum)
    edges, nodes = spectrum_graph.nodesToSpectrumGraph(nodes)
    source, sink = spectrumSourseAndSink(Spectrum, nodes)
    paths = pathsFromNodeToSink(source, sink, nodes)
    paths = addSourseToPaths(source, paths)
    for path in paths:
        Peptide = ""
        currentNode = path
        while currentNode.base != sink.base:
            nextNode = currentNode.outs[0]
            edge = dLE.edgeFromSet(currentNode.base, nextNode.base, edges)
            Peptide += edge.label
            currentNode = nextNode
        iSpectrum = idealSpectrum(Peptide, massTable)
        if isEqualSpectrums(Spectrum, iSpectrum):
            return Peptide

def isEqualSpectrums(Spectrum, IdealSpectrum):
    iSpectrumString = " ".join(map(str, IdealSpectrum[1:]))
    if Spectrum == iSpectrumString:
        return True
    return False

def idealSpectrum(Peptide, massTable):
    spectrum = []
    for i in xrange(0, len(Peptide)):
        prefix = Peptide[:i]
        suffix = Peptide[i:]
        spectrum.append(sumOfMasses(prefix, massTable))
        spectrum.append(sumOfMasses(suffix, massTable))
    return sorted(spectrum)

def sumOfMasses(String, massTable):
    return sum([massTable[x] for x in String])

def addSourseToPaths(source, paths):
    newPaths = []
    for path in paths:
        newPathNode = dG.pathNode(source)
        path.ins = [newPathNode]
        newPathNode.outs = [path]
        newPaths.append(newPathNode)
    return newPaths

def pathsFromNodeToSink(node, sink, nodes):
    if node == sink:
        pathNode = dG.pathNode(sink)
        return [pathNode]
    paths = []
    for outNode in node.outs:
        pathsStarts = pathsFromNodeToSink(outNode, sink, nodes)
        for oldPathStart in pathsStarts:
            pathNode = dG.pathNode(outNode)
            oldPathStart.ins = [outNode]
            pathNode.outs = [oldPathStart]
            paths.append(pathNode)
    return paths

def spectrumSourseAndSink(Spectrum, nodes):
    sourse = nodes[0]
    sink = nodes[-1]
    return  sourse, sink

#print idealSpectrum("GPG", info.massIntTable())
#print sumOfMasses("GPG", info.massIntTable())