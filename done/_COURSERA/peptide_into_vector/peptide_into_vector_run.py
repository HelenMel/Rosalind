import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_4')))

import readFile
from bio_4 import peptide_into_vector as core

lines = readFile.listFromInput()
Peptide = lines[0]
answer = core.peptideIntoVectorRun(Peptide)
result = " ".join(map(str, answer))
print result
readFile.lineToOutput(result)
    
