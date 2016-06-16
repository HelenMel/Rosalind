import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_2')))

import readFile
import useful
import cyclopeptideSequencing as root

lines = readFile.listFromInput()
Spectrum = map(int, lines[0].split(" "))
print Spectrum
Sequences = root.cyclopeptideSequencing(Spectrum)
# to string
SequencesS = [[str(y) for y in x] for x in Sequences]
# join	
result = " ".join(["-".join(x) for x in SequencesS])
print result
readFile.lineToOutput(result)
    
