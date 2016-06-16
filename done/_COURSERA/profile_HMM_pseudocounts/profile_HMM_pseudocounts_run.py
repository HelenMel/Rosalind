import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_6')))

import readFile
import useful
import profile_HMM_pseudocounts as core

lines = readFile.listFromInput()
threshold, theta = map(float, lines[0].split(" "))
alphabet = lines[2].split(" ")
Alignment = lines[4:]
TransitionMatrix, EmmiterMatrix = core.profileHMM(threshold, alphabet, Alignment, theta)
result = "\n".join([TransitionMatrix, "--------", EmmiterMatrix])
print result
readFile.lineToOutput(result)

