import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_2')))

import readFile
import useful
import generateTSpectrum as root

lines = readFile.listFromInput()
Peptide = lines[0]
result = " ".join(map(str,root.generateSpectrum(Peptide)))
print result
readFile.lineToOutput(result)
    
