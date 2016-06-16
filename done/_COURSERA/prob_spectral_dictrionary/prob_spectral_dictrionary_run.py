import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_4')))

import readFile
import useful
import prob_spectral_dictrionary as core

lines = readFile.listFromInput()
spectrumVector = map(int, lines[0].split(" "))
threshold = int(lines[1])
max_score = int(lines[2])
print threshold, max_score
result = str(core.probabilityOfSpectralDictionaryRun(spectrumVector, threshold, max_score))
print result
readFile.lineToOutput(result)
