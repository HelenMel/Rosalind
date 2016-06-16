import sys, os
import time
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_3')))

import scoringMatrix as sM

sigma = 5

def outputLCSRun(v, w):
    scoreTable = sM.defaultMatrix()

def middle_edge_run(v, w):
   start_time = time.time()
   scoreTable = sM.defaultMatrix()
   answer = middle_edge(v, w, 0, len(v), 0, len(w), scoreTable)
   print("--- %s seconds ---" % (time.time() - start_time))
   return answer

def middle_edge(v, w, top, bottom, left, right, scoreTable):
    maxILenght = float("-inf")
    maxMiddlePoint = (-1, -1);
    nextPoint = (-1, -1)
    middle = (left + right) / 2

    v_ = v[top:bottom]
    wL = w[left:middle]
    wR = w[middle:right]
    Sleft = LCSBackTrace(v_,  wL, scoreTable)
    Sright = LCSBackTrace(v_[::-1], wR[::-1], scoreTable)

    for i in xrange(0, len(v_)):
        opI = (len(v_))  - i
        point = pointToGlobalCoordinate(i, middle, top)
        symbol = scoreTable[v[point[0]]][w[point[1]]] # scoreTable[vS[-1]][wS[-1]]
        sinkLength, nI, nJ = from_sink(Sright, opI, i, middle, symbol)
        length = from_sourse(i, Sleft) + sinkLength
        if length > maxILenght:
            maxILenght = length;
            maxMiddlePoint = point
            nextPoint = pointToGlobalCoordinate(nI, nJ, top)

    return maxMiddlePoint, nextPoint, maxILenght

def pointToGlobalCoordinate(i, j, top):
    return ((i + top), j)

def from_sourse(i, S):
    score = S[i][-1]
    return score

def from_sink(S, opI, i, middle, symbol):
    maxI = opI; maxJ = -1
    score = S[maxI][-1]
    nextI = 0
    nextJ = middle + 1
    if score == S[maxI - 1][maxJ - 1] + symbol:
        nextI = i + 1; nextJ = middle + 1
    elif score == S[maxI][maxJ - 1] - sigma:
        nextI = i; nextJ = middle + 1
    elif score == S[maxI - 1][maxJ] - sigma:
        nextI = i + 1; nextJ = middle
    else:
        assert False

    return score, nextI, nextJ

# given: w and v are a strings
def LCSBackTrace(v, w, scoreTable):
    N = len(v) + 1
    M = len(w) + 1
    S = []
    [S.append([0] * M) for x in range(0, N)]
    S = correctedWithSigma(S, M, N)
    for i in xrange(1, N):
        iV = i - 1
        for j in xrange(1, M):
            jW = j - 1
            # what it top letter? its a sigma!
            top = S[i - 1][j] - sigma
            left = S[i][j - 1] - sigma
            diagonal = S[i - 1][j - 1] + scoreTable[v[iV]][w[jW]]
            S[i][j] = max(top, left, diagonal)
    return S

def correctedWithSigma(S, M, N):
    for i in xrange(1, N):
        S[i][0] = - sigma * i
    for j in xrange(1, M):
        S[0][j] = - sigma * j
    return S