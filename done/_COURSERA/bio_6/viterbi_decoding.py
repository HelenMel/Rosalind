import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_6')))

from bio_6 import probab_hidden_path as core

#should uncomment all

def viterbi_decoding(state_table, x_table, x, states):
    state_headers, state_rows, state_matrix = state_table
    S, Backtrack = viterbiSAndBacktrack(state_table, x_table, x, states)
    maxSink = ""; maxS = 0
    for k in states:
        kIndex = state_rows[k]
        Sk = S[-1][kIndex]
        if Sk > maxS:
            maxS = Sk; maxSink = k
    print maxS
    path = pathForBacktrack(Backtrack, maxSink, state_rows, len(x))
    return path

def viterbiSAndBacktrack(state_table, x_table, x, states):
    state_headers, state_rows, state_matrix = state_table
    x_headers, x_rows, x_matrix = x_table
    print state_headers, state_rows, state_matrix
    print x_headers, x_rows, x_matrix
    S = [initialS(states, x_headers[x[0]], x_rows, x_matrix, state_matrix, state_headers)]
    Backtrack = [initialBacktrack(states, x_rows, S[0])]
    for i in xrange(1, len(x)):
        emittedSymbol = x[i]
        emittedSymbolIndex = x_headers[emittedSymbol]
        S_previous = S[i - 1]
        SK = [0] * len(states)
        BacktrackK = [" "] * len(states)
        for k in states:
            kIndex = state_headers[k]
            def score(l):
                lIndex = state_rows[l]
                emission =  x_matrix[x_rows[l]][emittedSymbolIndex]
                transition = state_matrix[lIndex][kIndex]
                prob = S_previous[lIndex] * transition * emission
                return prob, l
            maxScore, maxL = max([score(l) for l in states], key=lambda x: x[0])
            SK[kIndex] = maxScore
            BacktrackK[kIndex] = maxL
        S.append(SK)
        Backtrack.append(BacktrackK)
    return S, Backtrack

def initialS(states, firstSymbolIndex, x_rows, x_matrix, state_matrix, state_headers):
    #initialTransition = 1.0 / len(states)
    def initialScore(k):
        emission = x_matrix[x_rows[k]][firstSymbolIndex]
        initialTransition = state_matrix[state_headers[k]][firstSymbolIndex]
        return 1 * initialTransition * emission
    S = [0] * len(states)
    for k in states:
        S[x_rows[k]] = initialScore(k)
    return S

def initialBacktrack(states, x_rows, initS):
    maxSink = ""; maxS = 0
    for k in states:
        kIndex = x_rows[k]
        Sk = initS[kIndex]
        if Sk > maxS:
            maxS = Sk; maxSink = k
    return [maxSink] * len(states)


def pathForBacktrack(Backtrack, sink, state_rows, xCount):
    nextIndex = state_rows[sink]
    path = []
    next = None
    symbolIndex = xCount - 1
    while symbolIndex >= 0:
        next = Backtrack[symbolIndex][nextIndex]
        path.append(next)
        nextIndex = state_rows[next]
        symbolIndex -= 1
    return path[::-1]