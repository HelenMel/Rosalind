import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_4')))

import readFile
from bio_4 import peptide_identification as core

lines = readFile.listFromInput()
spectrumVector = map(int, lines[0].split(" "))
Proteom = lines[1]
result = core.peptideIdentificationRun(Proteom,spectrumVector)[1]
print result
readFile.lineToOutput(result)
    
