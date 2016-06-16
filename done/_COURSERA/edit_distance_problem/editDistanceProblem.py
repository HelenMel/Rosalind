import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_3')))

def outputLCSRun(v, w):
    Backtrace, S = LCSBackTrace(v, w)
    maxI = (len(v) - 1)
    maxJ = (len(w) - 1)
    score = S[len(v)][len(w)]
    return score

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
def LCSBackTrace(v, w):
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
            top = S[i - 1][j] - 1
            #
            left = S[i][j - 1] - 1
            diagonal = 0
            if v[iV] == w[jW]:
                diagonal = S[i - 1][j - 1]
            else:
                diagonal = S[i - 1][j - 1] - 1
            S[i][j] = max(top, left, diagonal)
            if S[i][j] == top:
                Backtrace[iV][jW] = downB()
            elif S[i][j] == left:
                Backtrace[iV][jW] = rightB()
            elif S[i][j] == diagonal:
                Backtrace[iV][jW] = diagonalB()
    return Backtrace, S

def correctedWithSigma(S, M, N):
    for i in xrange(1, N):
        S[i][0] = -1 * i
    for j in xrange(1, M):
        S[0][j] = -1 * j
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
