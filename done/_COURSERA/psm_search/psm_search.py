import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_4')))

import nucleotides as info
from bio_4 import peptide_identification as pepI

def PSMSearchRun(SpectralVectors, Proteom, threshold):
    return PSMSearch(SpectralVectors, Proteom, threshold, info.massIntTable())

def PSMSearch(SpectralVectors, Proteom, threshold, massTable):
    PSMSet = []
    for spectrum in SpectralVectors:
        maxPeptide = pepI.peptideIdentification(Proteom, spectrum, massTable)
        if maxPeptide[0] >= threshold:
            PSMSet.append(maxPeptide[1])
    return PSMSet

fakeMassTable = { "X":4, "Z":5 }
SpectralVector1 = [-1,5,-4,5,3,-1,-4,5,-1,0,0,4,-1,0,1,4,4,4]
SpectralVector2 = [-4,2,-2,-4,4,-5,-1,4,-1,2,5,-3,-1,3,2,-3]
Proteom = "XXXZXZXXZXZXXXZXXZX"
#print PSMSearch([SpectralVector1, SpectralVector2], Proteom, 5, fakeMassTable)