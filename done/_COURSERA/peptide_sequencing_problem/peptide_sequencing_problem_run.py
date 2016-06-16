import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_4')))

import readFile
import useful
import peptide_sequencing_problem as core

lines = readFile.listFromInput()
spectrumVector = map(int, lines[0].split(" "))
result = core.peptideSequencingProblemRun(spectrumVector)
print result
readFile.lineToOutput(result)
