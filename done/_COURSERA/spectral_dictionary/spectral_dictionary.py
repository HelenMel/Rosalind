import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_4')))

import nucleotides as info

def sizeOfSpectralDictionaryRun(Spectrum, threshold, max_score):
    return sizeOfSpectralDictionary(Spectrum, threshold, max_score, info.massIntTable())

def sizeOfSpectralDictionary(Spectrum, threshold, max_score, massTable):
    Size = findSizeMatrix(Spectrum, max_score, massTable)
    lastS = Size[-1]
    return sum(lastS[threshold:])

def findSizeMatrix(Spectrum, max_score, massTable):
    Size = initialSizeMatrix(max_score)
    massSet = set(massTable.values())
    minMass = min(massSet)
    Spectrum_ = [0] + Spectrum
    for i in xrange(1, len(Spectrum_)):
        Si = Spectrum_[i]# should be from spectrum
        newSizeRow = []
        for t in xrange(0, max_score + 1):
            def sizeForAcid(acid, i, t):
                oldI = i - massTable[acid]
                oldT = t - Si
                if oldT == 0 and oldI == 0:
                    return 1
                if oldI <= 0 or oldT < 0 or oldT > max_score:
                    return 0
                else:
                    return Size[oldI][oldT]
            S = sum([sizeForAcid(acid, i, t) for acid in massTable.keys()])
            newSizeRow.append(S)
        Size.append(newSizeRow)
    return Size
        # sum all of items

# matrix is 2 D
def initialSizeMatrix(max_score):
    Size = [[0] * (max_score + 1)]
    Size[0][0] = 1
    return Size

fakeMassTable = { "X":4, "Z":5 }
SpectrumVector = [4,-3,-2,3,3,-4,5,-3,-1,-1,3,4,1,3]
threshold = 1; max_score = 8
#print sizeOfSpectralDictionary(SpectrumVector, threshold, max_score, fakeMassTable)