import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_3')))

import scoringMatrix as sM

sigma = 10
epsilon = 1

def outputLCSRun(v, w):
    scoreTable = sM.defaultMatrix()
    mbacktrace, ubacktrace, lbacktrace, S = LCSBackTrace(v, w, scoreTable)
    maxI = (len(v) - 1)
    maxJ = (len(w) - 1)
    score = S[len(v)][len(w)]
    return outputLCS(mbacktrace, ubacktrace, lbacktrace, v, w, maxI, maxJ, mbacktrace), score

def outputLCS(mb, ub, lb, v, w, i, j, currentb):
    if i < 0 or j < 0:
        return initialOuts(i, j, v, w)
    if currentb[i][j] == downB():
        if currentb == mb:
            out1, out2 = outputLCS(mb, ub, lb, v, w, i, j, lb)
        else:
            out1, out2 = outputLCS(mb, ub, lb, v, w, i - 1, j, lb)
            out1 += v[i]
            out2 += "-"
    elif currentb[i][j] == rightB():
        if currentb == mb:
            out1, out2 = outputLCS(mb, ub, lb, v, w, i, j, ub)
        else:
            out1, out2 = outputLCS(mb, ub, lb, v, w, i, j - 1, ub)
            out1 += "-"
            out2 += w[j]
    else:
        if currentb == ub:
            out1, out2 = outputLCS(mb, ub, lb, v, w, i, j - 1, mb)
            out1 += "-"
            out2 += w[j]
        elif currentb == lb:
            out1, out2 = outputLCS(mb, ub, lb, v, w, i - 1, j, mb)
            out1 += v[i]
            out2 += "-"
        else:
            out1, out2 = outputLCS(mb, ub, lb, v, w, i - 1, j - 1, mb)
            out2 += w[j]
            out1 += v[i]
    return out1, out2

def initialOuts(i, j, v, w):
    if i == j:
        return "", ""
    if i >= 0:
        cToInsert = i + 1
        out2 = "-" * cToInsert
        return v[:cToInsert], out2
    if j >= 0:
        cToInsert = j + 1
        out1 = "-" * cToInsert
        return  out1, w[:cToInsert]
    return "", ""

# given: w and v are a strings
def LCSBackTrace(v, w, scoreTable):
    N = len(v) + 1
    M = len(w) + 1
    middle = []; upper = []; lower = []
    [middle.append([0] * M) for x in range(0, N)]
    middle = correctedMiddle(middle, M, N)
    [upper.append([0] * M) for x in range(0, N)]
    upper = correctedUpper(upper, M, N)
    [lower.append([0] * M) for x in range(0, N)]
    lower = correctedLower(lower, M, N)
    mbacktrace = emptyBacktrace(M, N)
    ubacktrace = emptyBacktrace(M, N)
    lbacktrace = emptyBacktrace(M, N)
    for i in xrange(1, N):
        iV = i - 1
        for j in xrange(1, M):
            jW = j - 1
            # lower special case
            updateLowerMatrix(lower, middle, lbacktrace, i, j, iV, jW)
            # upper special case
            updateUpperMatrix(upper, middle, ubacktrace, i, j, iV, jW)
            # middle
            top = lower[i][j]
            left = upper[i][j]
            diagonal = middle[i - 1][j - 1] + scoreTable[v[iV]][w[jW]]

            middle[i][j] = max(top, left, diagonal)

            if middle[i][j] == diagonal:
                mbacktrace[iV][jW] = diagonalB()
            elif middle[i][j] == top:
                mbacktrace[iV][jW] = downB()
            elif middle[i][j] == left:
                mbacktrace[iV][jW] = rightB()
    #print "\n".join(["\t".join(map(str, x)) for x in middle])
    return mbacktrace, ubacktrace, lbacktrace, middle

def updateLowerMatrix(lower, middle, lbacktrace, i, j, iV, jW):
    ltop = lower[i - 1][j] - epsilon
    lmiddle = middle[i - 1][j] - sigma
    lower[i][j] = max(ltop, lmiddle)
    if lower[i][j] == ltop:
        lbacktrace[iV][jW] = downB()
    elif lower[i][j] == lmiddle:
        lbacktrace[iV][jW] = diagonalB()

def updateUpperMatrix(upper, middle, ubacktrace, i, j, iV, jW):
    uright = upper[i][j - 1] - epsilon
    umiddle = middle[i][j - 1] - sigma
    upper[i][j] = max(uright, umiddle)
    if upper[i][j] == uright:
        ubacktrace[iV][jW] = rightB()
    elif upper[i][j] == umiddle:
        ubacktrace[iV][jW] = diagonalB()

def correctedUpper(S, M, N):
    for i in xrange(1, N):
        S[i][0] = float("-inf")
    for j in xrange(1, M):
        S[0][j] = - sigma - epsilon * (i - 1)
    return S

def correctedLower(S, M, N):
    for i in xrange(1, N):
        S[i][0] = - sigma - epsilon * (i - 1)
    for j in xrange(1, M):
        S[0][j] = float("-inf")
    return S

def correctedMiddle(S, M, N):
    """

    :rtype: matrix of integers
    """
    for i in xrange(1, N):
        S[i][0] = - sigma - epsilon * (i - 1)
    for j in xrange(1, M):
        S[0][j] = - sigma - epsilon * (j - 1)
    return S

# Backtrace presentation
def emptyBacktrace(M, N):
    Backtrace = []
    [Backtrace.append(["-"] * (M - 1)) for x in xrange(0, (N - 1))]
    return Backtrace

def downB():
    return "|"

def rightB():
    return "->"

def diagonalB():
    return '\\'

print outputLCSRun("", "")

