def outputLCSRun(v, w):
    Backtrace = LCSBackTrace(v, w)
    maxI = (len(v) - 1)
    maxJ = (len(w) - 1)
    return outputLCS(Backtrace, v, maxI, maxJ)

def outputLCS(Backtrace, v, i, j):
    if i < 0 or j < 0:
        return ""
    if Backtrace[i][j] == downB():
        out = outputLCS(Backtrace, v, i - 1, j)
    elif Backtrace[i][j] == rightB():
        out = outputLCS(Backtrace, v, i, j - 1)
    else:
        out = outputLCS(Backtrace, v, i - 1, j - 1)
        out += v[i]
    return out

# given: w and v are a strings
def LCSBackTrace(v, w):
    N = len(v) + 1
    M = len(w) + 1
    S = []
    Backtrace = emptyBacktrace(M, N)
    [S.append([0] * M) for x in range(0, N)]
    for i in xrange(1, N):
        iV = i - 1
        for j in xrange(1, M):
            jW = j - 1
            isSameLetter = v[iV] == w[jW]
            top = S[i - 1][j]
            left = S[i][j - 1]
            diagonal = 0
            if isSameLetter:
                diagonal = S[i - 1][j - 1] + 1
            S[i][j] = max(top, left, diagonal)
            if S[i][j] == top:
                Backtrace[iV][jW] = downB()
            elif S[i][j] == left:
                Backtrace[iV][jW] = rightB()
            elif S[i][j] == diagonal and isSameLetter:
                Backtrace[iV][jW] = diagonalB()
    return Backtrace

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
