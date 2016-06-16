import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_3')))

import scoringMatrix as sM

def outputLCSRun(v, w):
    scoreTable = sM.PAM250Matrix()
    Backtrace, S = LCSBackTrace(v, w, scoreTable)
    i, j, score = findMaxElementsCoordinate(S)
    return outputLCS(Backtrace, v, w, i - 1, j - 1), score

def findMaxElementsCoordinate(S):
    lastRowIndex = len(S) - 1
    indexJ = -1
    maxScore = - sys.maxint
    for j in xrange(0, len(S[0])):
        if S[lastRowIndex][j] > maxScore:
            maxScore = S[lastRowIndex][j]
            indexJ = j
    return lastRowIndex, indexJ, maxScore

def outputLCS(Backtrace, v, w, i, j):
    if j < 0:
        return "", ""
    if Backtrace[i][j] == downB():
        out1, out2 = outputLCS(Backtrace, v, w, i - 1, j)
        out1 += v[i]
        out2 += "-"
    elif Backtrace[i][j] == rightB():
        out1, out2 = outputLCS(Backtrace, v, w, i, j - 1)
        out1 += "-"
        out2 += w[j]
    elif Backtrace[i][j] == startB() and j > 0:
        return "", ""
    else:
        out1, out2 = outputLCS(Backtrace, v, w, i - 1, j - 1)
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
    S = []
    Backtrace = emptyBacktrace(M, N)
    [S.append([0] * M) for x in range(0, N)]
    S = correctedWithSigma(S, M, N)
    for i in xrange(1, N):
        iV = i - 1
        for j in xrange(1, M):
            jW = j - 1
            top = S[i - 1][j] - 2
            #
            left = S[i][j - 1] - 2
            if v[iV] == w[jW]:
                diagonal = S[i - 1][j - 1] + 1
            else:
                diagonal = S[i - 1][j - 1] - 2
            jump = False
            if j == 0:
                S[i][j] = max(0, top, left, diagonal)
                jump = True
            else:
                S[i][j] = max(top, left, diagonal)

            if S[i][j] == 0 and jump == True:
                Backtrace[iV][jW] = startB()
            elif S[i][j] == top:
                Backtrace[iV][jW] = downB()
            elif S[i][j] == left:
                Backtrace[iV][jW] = rightB()
            elif S[i][j] == diagonal:
                Backtrace[iV][jW] = diagonalB()
    print "\n".join(["\t".join(map(str, x)) for x in S])
    return Backtrace, S

def correctedWithSigma(S, M, N):
    for i in xrange(1, N):
        S[i][0] = 0 * i
    for j in xrange(1, M):
        S[0][j] = -2 * j
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

def startB():
    return 's'
