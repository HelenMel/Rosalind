import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_4')))

import nucleotides as info
import peptide_into_vector as pepV

def peptideIdentificationRun(Proteom, spectrumVector):
    return peptideIdentification(Proteom, spectrumVector, info.massIntTable())

def peptideIdentification(Proteom, spectrumVector, massTable):
    validSubPeptides = findSubPeptideWithSpectrumLength(len(spectrumVector), massTable,Proteom)
    if len(validSubPeptides) == 0:
        return -1, ""
    peptideScores = [weightForPeptideInSpectrumVector(spectrumVector, massTable, x) for x in validSubPeptides]
    maxPeptide = max(peptideScores, key=lambda x: x[0])
    return maxPeptide

def findSubPeptideWithSpectrumLength(spectrumLength, massTable, Proteom):
    subPeptides = []
    for start in xrange(0, len(Proteom)):
        end = start + 1
        while end < len(Proteom):
            peptide = Proteom[start: end]
            length = len(pepV.peptideIntoVector(peptide, massTable))
            if length == spectrumLength:
                subPeptides.append(peptide)
            if length >= spectrumLength:
                break
            end += 1
    return subPeptides

def weightForPeptideInSpectrumVector(spectrumVector, massTable, Peptide):
    score = 0
    index = -1
    for i in xrange(0, len(Peptide)):
        index = index + massTable[Peptide[i]]
        score += spectrumVector[index]
    return score, Peptide

fakeMassTable = { "X":4, "Z":5 }
SpectrumVector = [0,0,0,4,-2,-3,-1,-7,6,5,3,2,1,9,3,-8,0,3,1,2,1,8]
Proteom = "XZZXZXXXZXZZXZXXZ"
#print peptideIdentification(Proteom, SpectrumVector, fakeMassTable)