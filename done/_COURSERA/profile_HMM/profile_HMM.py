import sys, os
import collections
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_6')))

import directedGraph as dG
import directedWeightGraph as dWG

Nodes = collections.namedtuple('Nodes', 'matches inserts deletes end start')

def profileHMM(threshold, alphabet, Alignment):
    profile_, alignmentSize, columsToRemove = makeProfileFromAlignment(Alignment, alphabet, threshold)
    connections, nodes = makeAlignmentGraph(alignmentSize)
    paths = []; letters = { }
    for line in Alignment:
        path = alignmentPath(line, columsToRemove, nodes, letters)
        paths.append(path)
    TransitionMatrix = transitionWithPathsAndGraph(connections, nodes, paths)
    EmmiterMatrix = emmitionWithLettersAndGraph(nodes, alphabet, letters)
    return TransitionMatrix, EmmiterMatrix

def makeProfileFromAlignment(alignment, alphabet, threshold):
    N = len(alignment[0])
    M = len(alignment)
    alphabet_ = alphabet + [insertionS()]
    alphabetD = dict(zip(alphabet_, xrange(0, len(alphabet_))))
    ProfilePerColumn = []
    columsToRemove = set()
    for i in xrange(0, N):
        Profile = [0.0] * len(alphabet_)
        for line in alignment:
            symbolIndex = alphabetD[line[i]]
            Profile[symbolIndex] += 1
        # remove '-' from profile count
        Profile = [x / M for x in Profile]

        insertionFraction = Profile.pop(alphabetD[insertionS()])
        if insertionFraction <= threshold:
            ProfilePerColumn.append(Profile)
        else:
            columsToRemove.add(i)
    newLength = N - len(columsToRemove)
    return ProfilePerColumn, newLength, columsToRemove

def alignmentFromFractions(alignment, columsToRemove):
    filteredAlinment = []
    for line in alignment:
        filteredLine = "".join([char for idx, char in enumerate(line) if idx not in columsToRemove])
        filteredAlinment.append(filteredLine)
    return filteredAlinment

def alignmentPath(line, columsToRemove, nodes, letters):
    deletionItems = nodes.deletes
    matchItems = nodes.matches
    insertionItems = nodes.inserts
    start = nodes.start
    path = [start]; filteredIndex = 1;
    for idx, char in enumerate(line):
        # change it to return path!
        if idx in columsToRemove:
            if char != insertionS():
                # append insertion. What is the index? next?
                nodeName = insertionItems[filteredIndex - 1]
                path.append(nodeName)
                if nodeName not in letters:
                    letters[nodeName] = []
                letters[nodeName].append(char)
            continue
        if char == insertionS():
            path.append(deletionItems[filteredIndex])
        else:
            nodeName = matchItems[filteredIndex]
            path.append(nodeName)
            if nodeName not in letters:
                letters[nodeName] = []
            letters[nodeName].append(char)
        filteredIndex += 1
    return path

def emmitionWithLettersAndGraph(nodes, alphabet, letters):
    headRow = rowHeadWithNodes(nodes)
    EmitionMatrix = generateEmitionMatrix(headRow, letters, alphabet)
    return emittionMatrixToPrettyTable(EmitionMatrix, headRow, alphabet)

def generateEmitionMatrix(headRow, letters, alphabet):
    EmitionMatrix = []
    alphabetD = dict(zip(alphabet, xrange(0, len(alphabet))))
    for node in headRow:
        Emmition = [0] * len(alphabet)
        if node not in letters:
            EmitionMatrix.append(Emmition)
            continue
        lettersOccurence = letters[node]
        c = collections.Counter(lettersOccurence).most_common()
        for element, count in c:
            indexOfElement = alphabetD[element]
            Emmition[indexOfElement] = float(count) / len(lettersOccurence)
        EmitionMatrix.append(Emmition)
    return EmitionMatrix

def emittionMatrixToPrettyTable(EmitionMatrix, headRow, alphabet):
    lines = ["\t" + "\t".join(alphabet)]
    for i in xrange(0, len(headRow)):
        line = [headRow[i].base]
        def xToString(x):
            if x == 0:
                return str(0)
            return str(round(x, 3))
        line = line + [ xToString(x) for x in EmitionMatrix[i]]
        lines.append("\t".join(line))
    return "\n".join(lines)

def transitionWithPathsAndGraph(connections, nodes, paths):
    end = nodes.end
    for path in paths:
        for idx, node in enumerate(path):
            if idx == (len(path) - 1):
                nextNode = end
            else:
                nextNode = path[idx + 1]
            edge = dWG.weightFromSet(node, nextNode, connections)
            edge.weight += 1
    headRow = rowHeadWithNodes(nodes)
    Transitions = generateTransitionTable(headRow, connections)
    return transitionMatrixAndHeadToPrettyTable(headRow, Transitions)

def transitionMatrixAndHeadToPrettyTable(headRow, Transitions):
    lines = ["\t" + "\t".join([x.base for x in headRow])]
    for i in xrange(0, len(headRow)):
        line = [headRow[i].base]
        def xToString(x):
            if x == 0:
                return str(0)
            return str(round(x, 3))
        line = line + [ xToString(x) for x in Transitions[i]]
        lines.append("\t".join(line))
    return "\n".join(lines)

def generateTransitionTable(headRow, connections):
    TransitionMatrix = []
    for i in xrange(0, len(headRow)):
        sumI = 0.0; TransitionTableRow = [0] * len(headRow); startNode = headRow[i]
        for j in xrange(0, len(headRow)):
            endNode = headRow[j]
            edge = dWG.NodsWeight(startNode, endNode, -1.0)
            if edge in connections:
                weight = dWG.weightFromSet(startNode, endNode, connections).weight
                TransitionTableRow[j] = weight; sumI += weight
        if sumI > 0:
            TransitionTableRow = [x / sumI for x in TransitionTableRow]
        TransitionMatrix.append(TransitionTableRow)
    return TransitionMatrix

def rowHeadWithNodes(nodes):
    deletionItems_ = nodes.deletes
    matchItems_ = nodes.matches
    insertionItems_ = nodes.inserts
    start = nodes.start
    end = nodes.end
    headRow = [start, insertionItems_[0]]
    for i in xrange(1, len(matchItems_)):
        headRow.append(matchItems_[i])
        headRow.append(deletionItems_[i])
        headRow.append(insertionItems_[i])
    headRow.append(end)
    return headRow

def makeAlignmentGraph(alingmentSize):
    insertionItems = []
    deletionItems = []
    matchItems = []
    end = dG.Node("E")
    start = dG.Node("S")
    for i in xrange(0, alingmentSize + 1):
        insertionItems.append(insertionNode(i))
        deletionItems.append(deletionNode(i))
        matchItems.append(matchNode(i))
    nodes = Nodes(matches = matchItems, inserts = insertionItems, deletes = deletionItems, end = end, start = start)
    connections = set()
    connections.add(dWG.NodsWeight(insertionItems[0], matchItems[1], 0.0))
    connections.add(dWG.NodsWeight(insertionItems[0], deletionItems[1], 0.0))
    connections.add(dWG.NodsWeight(insertionItems[0], insertionItems[0], 0.0))

    for i in xrange(1, alingmentSize):
        connections = connections | newEdges(i, matchItems[i], nodes)
        connections = connections | newEdges(i, insertionItems[i], nodes)
        connections = connections | newEdges(i, deletionItems[i], nodes)

    connections.add(dWG.NodsWeight(matchItems[alingmentSize], insertionItems[alingmentSize], 0.0))
    connections.add(dWG.NodsWeight(insertionItems[alingmentSize], insertionItems[alingmentSize], 0.0))
    connections.add(dWG.NodsWeight(deletionItems[alingmentSize], insertionItems[alingmentSize], 0.0))

    # add end
    connections.add(dWG.NodsWeight(matchItems[-1], end, 0.0))
    connections.add(dWG.NodsWeight(insertionItems[-1], end, 0.0))
    connections.add(dWG.NodsWeight(deletionItems[-1], end, 0.0))

    # add start
    connections.add(dWG.NodsWeight(start, matchItems[1], 0.0))
    connections.add(dWG.NodsWeight(start, deletionItems[1], 0.0))
    connections.add(dWG.NodsWeight(start, insertionItems[0], 0.0))

    return connections, nodes

def newEdges(i, node, nodes):
    deletionItems = nodes.deletes; matchItems = nodes.matches; insertionItems = nodes.inserts
    connections = set()
    connections.add(dWG.NodsWeight(node, deletionItems[i + 1], 0.0))
    connections.add(dWG.NodsWeight(node, matchItems[i + 1], 0.0))
    connections.add(dWG.NodsWeight(node, insertionItems[i], 0.0))
    return connections

def insertionS():
    return "-"

def insertionNode(i):
    str_i = str(i)
    return dG.Node("I" + str_i)

def deletionNode(i):
    str_i = str(i)
    return dG.Node("D" + str_i)

def matchNode(i):
    str_i = str(i)
    return dG.Node("M" + str_i)

#connections, nodes = makeAlignmentGraph(2)

