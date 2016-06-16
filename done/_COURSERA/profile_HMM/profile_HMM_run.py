import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_6')))

import readFile
import useful
import profile_HMM as core

lines = readFile.listFromInput()
threshold = float(lines[0])
alphabet = lines[2].split(" ")
Alignment = lines[4:]
TransitionMatrix, EmmiterMatrix = core.profileHMM(threshold, alphabet, Alignment)
result = "\n".join([TransitionMatrix, "--------", EmmiterMatrix])
print result
readFile.lineToOutput(result)
    
