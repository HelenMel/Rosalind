import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_6')))

import readFile
import useful
import HMM_sequence_alignment as core
import bio_6.viterbi_decoding as vD
from bio_6 import probab_hidden_path as prob

lines = readFile.listFromInput()
x = lines[0]
threshold, theta = map(float, lines[2].split(" "))
alphabet = lines[4].split(" ")
Alignment = lines[6:]
TransitionMatrix, EmmiterMatrix, states = core.profileHMM(threshold, alphabet, Alignment, theta)

state_table = prob.parseTableFromLines(TransitionMatrix)
x_table = prob.parseTableFromLines(EmmiterMatrix)

path = vD.viterbi_decoding(state_table, x_table, x, states)
result = " ".join(core.fulfillWithPath(path))
print result
readFile.lineToOutput(result)
    
