import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_3')))

import scoringMatrix as sM

def outputLCSRun(v, w):
    scoreTable = sM.defaultMatrix()
    Backtrace, S = LCSBackTrace(v, w, scoreTable)
    maxI = (len(v) - 1)
    maxJ = (len(w) - 1)
    score = S[len(v)][len(w)]
    return outputLCS(Backtrace, v, w, maxI, maxJ), score

def outputLCS(Backtrace, v, w, i, j):
    if i < 0 or j < 0:
        return initialOuts(i, j, v, w)
    if Backtrace[i][j] == downB():
        out1, out2 = outputLCS(Backtrace, v, w, i - 1, j)
        out1 += v[i]
        out2 += "-"
    elif Backtrace[i][j] == rightB():
        out1, out2 = outputLCS(Backtrace, v, w, i, j - 1)
        out1 += "-"
        out2 += w[j]
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
            # what it top letter? its a sigma!
            top = S[i - 1][j] + sM.sigma()
            #
            left = S[i][j - 1] + sM.sigma()
            diagonal = S[i - 1][j - 1] + scoreTable[v[iV]][w[jW]]
            S[i][j] = max(top, left, diagonal)
            if S[i][j] == top:
                Backtrace[iV][jW] = downB()
            elif S[i][j] == left:
                Backtrace[iV][jW] = rightB()
            elif S[i][j] == diagonal:
                Backtrace[iV][jW] = diagonalB()
    #print "\n".join(["\t".join(map(str, x)) for x in S])
    return Backtrace, S

def correctedWithSigma(S, M, N):
    for i in xrange(1, N):
        S[i][0] = sM.sigma() * i
    for j in xrange(1, M):
        S[0][j] = sM.sigma() * j
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

#print outputLCSRun("PLEASANTLY", "MEANLY")