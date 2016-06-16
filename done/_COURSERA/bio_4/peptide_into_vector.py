import sys, os
import copy
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_4')))

import nucleotides as info

def peptideIntoVectorRun(Peptide):
    return peptideIntoVector(Peptide, info.massIntTable())

def peptideIntoVector(Peptide, massTable):
    vector = []
    for acid in Peptide:
        acidVector = [0] * massTable[acid]
        acidVector[-1] = 1
        vector += acidVector
    return vector

def vectorIntoPeptideRun(vectorPeptide):
    return vectorIntoPeptide(vectorPeptide, info.massIntTable())

def vectorIntoPeptide(vectorPeptide, massTable):
    vPeptide = copy.copy(vectorPeptide)
    Peptide = ""
    acidVector = []
    while len(vPeptide) > 0:
        item = vPeptide.pop()
        if item == 1:
            acid = acidFromVector(acidVector, massTable)
            if acid is not None:
                Peptide += acid
            acidVector = []
        acidVector.append(item)
    acid = acidFromVector(acidVector, massTable)
    if acid is not None:
        Peptide += acid
    return Peptide[::-1]

def acidFromVector(acidVector, massTable):
    acids = [k for k,v in massTable.items() if v == len(acidVector)]
    if len(acids) > 0:
        return acids[0]
    else:
        print "smth wrong"
        return None