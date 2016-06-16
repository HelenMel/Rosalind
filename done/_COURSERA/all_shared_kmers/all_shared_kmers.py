import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio3')))

import reverseComplement as rC

def presentPairs(Pairs):
    def toString(pair):
        return "(" + str(pair[0]) + ", " + str(pair[1]) + ")"
    return "\n".join(map(toString, Pairs))

def allSharedKMers(String1, String2, k):
    dK = stringToKMerDictionary(String1, k)
    Pairs = []
    for j in xrange(0, len(String2) - k + 1):
        subK = String2[j: j + k]
        if subK in dK:
            matchIndexes = dK[subK]
            for i in matchIndexes:
                Pairs.append((i, j))
    return Pairs

def stringToKMerDictionary(String1, k):
    dK = {}
    for i in xrange(0, len(String1) - k + 1):
        def insertSubK(subString, i):
            if subString in dK:
                dK[subString].append(i)
            else:
                dK[subString] = [i]
        subK = String1[i: i + k]
        insertSubK(subK, i)
        reverseK = rC.reverse_complement(subK)
        insertSubK(reverseK, i)
    return dK


#print len(allSharedKMers("TCTTGCAGCTCGTCA", "GTACTTTCAGAATCA", 3))