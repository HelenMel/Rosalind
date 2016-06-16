import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_2')))

import readFile
import useful
import cyclopeptideScoring as cS
import nucleotides as info

lines = readFile.listFromInput()
Peptide = lines[0]
Spectrum = map(int, lines[1].split(" "))
print Peptide, Spectrum
result = cS.linearScore(Peptide, Spectrum, info.massIntTable())
print result
readFile.lineToOutput(result)
    
