import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_2')))

import readFile
import useful
import convolutionCyclopeptideSequencing as root

lines = readFile.listFromInput()
M = int(lines[0])
N = int(lines[1])
Spectrum = sorted(map(int, lines[2].split(" ")))
print Spectrum
LeaderPeptide = root.convolutionCyclopeptideSequencing(M, N, Spectrum)
result = "-".join(map(str, LeaderPeptide[0]))
print result
readFile.lineToOutput(result)
    
