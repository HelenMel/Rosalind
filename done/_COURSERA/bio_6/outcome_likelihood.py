import os
import sys
import math
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_6')))

from bio_6 import probab_hidden_path as core

def outcome_likelihood(state_table, x_table, x, states):
    state_headers, state_rows, state_matrix = state_table
    S = viterbiSAndBacktrack(state_table, x_table, x, states)
    maxS = sum(S[-1])
    return maxS

def viterbiSAndBacktrack(state_table, x_table, x, states):
    state_headers, state_rows, state_matrix = state_table
    x_headers, x_rows, x_matrix = x_table
    print state_headers, state_rows, state_matrix
    print x_headers, x_rows, x_matrix
    S = [initialS(states, x_headers[x[0]], x_rows, x_matrix)]
    for i in xrange(1, len(x)):
        emittedSymbol = x[i]
        emittedSymbolIndex = x_headers[emittedSymbol]
        S_previous = S[i - 1]
        SK = [0] * len(states)
        for k in states:
            kIndex = state_headers[k]
            def score(l):
                lIndex = state_rows[l]
                emission = x_matrix[x_rows[k]][emittedSymbolIndex]
                transition = state_matrix[lIndex][kIndex]
                prob = S_previous[lIndex] * transition * emission
                return prob
            scores = [score(l) for l in states]
            maxScore = sum([score(l) for l in states])
            SK[kIndex] = maxScore
        S.append(SK)
    return S

def initialS(states, firstSymbolIndex, x_rows, x_matrix):
    initialTransition = 1.0 / len(states)
    def initialScore(k):
        emission = x_matrix[x_rows[k]][firstSymbolIndex]
        return 1 * initialTransition * emission
    S = [0] * len(states)
    for k in states:
        S[x_rows[k]] =  initialScore(k)
    return S