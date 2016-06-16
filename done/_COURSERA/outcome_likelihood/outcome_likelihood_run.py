import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_6')))

import readFile
from bio_6 import probab_hidden_path as prob
import bio_6.outcome_likelihood as core

lines = readFile.listFromInput()
x = lines[0]
alphabet = lines[2].split(" ")
states = lines[4].split(" ")
state_matrix_start = 6; state_matrix_end = state_matrix_start + len(states) + 1
state_table= prob.parseTableFromLines(lines[state_matrix_start: state_matrix_end])
x_matrix_start = state_matrix_end + 1; x_matrix_end = x_matrix_start + len(states) + 1
x_table = prob.parseTableFromLines(lines[x_matrix_start: x_matrix_end])
print x, alphabet, states
result = core.outcome_likelihood(state_table, x_table, x, states)
print result
readFile.lineToOutput(result)


    
