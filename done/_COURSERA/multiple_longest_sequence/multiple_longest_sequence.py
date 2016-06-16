import sys, os
import copy
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../_common')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_3')))

import scoringMatrix as sM

def outputLCSRun(v, w, q):
    scoreTable = sM.defaultMatrix()
    Backtrace, S = LCSBackTrace(v, w, q, scoreTable)
    maxI = (len(v) - 1)
    maxJ = (len(w) - 1)
    maxZ = (len(q) - 1)
    score = S[len(v)][len(w)][len(q)]
    return outputLCS(Backtrace, v, w, q, maxI, maxJ, maxZ), score

def outputLCS(Backtrace, v, w, q, i, j, z):
    if i < 0 or j < 0 or z < 0:
        return initialOuts(i, j, z, v, w, q)
    if Backtrace[i][j][z] == I_X_X():
        out1, out2, out3 = outputLCS(Backtrace, v, w, q, i - 1, j, z)
        out1 += v[i]
        out2 += "-"
        out3 += "-"
    elif Backtrace[i][j][z] == X_I_X():
        out1, out2, out3 = outputLCS(Backtrace, v, w, q, i, j - 1, z)
        out1 += "-"
        out2 += w[j]
        out3 += "-"
    elif Backtrace[i][j][z] == X_X_I():
        out1, out2, out3 = outputLCS(Backtrace, v, w, q, i, j, z - 1)
        out1 += "-"
        out2 += "-"
        out3 += q[z]
    elif Backtrace[i][j][z] == I_I_X():
        out1, out2, out3 = outputLCS(Backtrace, v, w, q, i - 1, j - 1, z)
        out1 += v[i]
        out2 += w[j]
        out3 += "-"
    elif Backtrace[i][j][z] == I_X_I():
        out1, out2, out3 = outputLCS(Backtrace, v, w, q, i - 1, j, z - 1)
        out1 += v[i]
        out2 += "-"
        out3 += q[z]
    elif Backtrace[i][j][z] == X_I_I():
        out1, out2, out3 = outputLCS(Backtrace, v, w, q, i, j - 1, z - 1)
        out1 += "-"
        out2 += w[j]
        out3 += q[z]
    elif Backtrace[i][j][z] == I_I_I():
        out1, out2, out3 = outputLCS(Backtrace, v, w, q, i - 1, j - 1, z - 1)
        out1 += v[i]
        out2 += w[j]
        out3 += q[z]
    return out1, out2, out3

def initialOuts(i, j, z, v, w, q):
    if i == j and i == z:
        return "", "", ""
    cToInsert = max(j + 1, z + 1, i + 1)
    out1 = v[: (i + 1)] + "-" * (cToInsert - (i + 1))
    out3 = q[: (z + 1)] + "-" * (cToInsert - (z + 1))
    out2 = w[: (j + 1)] + "-" * (cToInsert - (j + 1))
    return  out1, out2, out3

# given: w and v are a strings
def LCSBackTrace(v, w, q, scoreTable):
    N = len(v) + 1
    M = len(w) + 1
    P = len(q) + 1
    R = []
    S = []
    Backtrace = emptyBacktrace(M, N, P)
    [R.append([0] * P) for y in xrange(0, M)]
    [S.append(copy.deepcopy(R)) for x in range(0, N)]
    S = correctedWithSigma(S, M, N, P)
    for i in xrange(1, N):
        iV = i - 1
        for j in xrange(1, M):
            jW = j - 1
            for z in xrange(1, P):
                zQ = z - 1
                isSame = v[iV] == w[jW] and v[iV] == q[zQ]
                S_I_X_X = S[i - 1][j][z]
                S_X_I_X = S[i][j - 1][z]
                S_X_X_I = S[i][j][z - 1]
                S_I_I_X = S[i - 1][j - 1][z]
                S_I_X_I = S[i - 1][j][z - 1]
                S_X_I_I = S[i][j - 1][z - 1]
                S_I_I_I = S[i - 1][j - 1][z - 1]
                if isSame:
                    S_I_I_I += 1
                S[i][j][z] = max(S_I_X_X, S_X_I_X, S_X_X_I, S_I_I_X, S_I_X_I, S_X_I_I, S_I_I_I)

                if S[i][j][z] == S_X_I_I:
                    Backtrace[iV][jW][zQ] = X_I_I()
                elif S[i][j][z] == S_I_X_I:
                    Backtrace[iV][jW][zQ] = I_X_I()
                elif S[i][j][z] == S_I_I_X:
                    Backtrace[iV][jW][zQ] = I_I_X()
                elif S[i][j][z] == S_X_X_I:
                    Backtrace[iV][jW][zQ] = X_X_I()
                elif S[i][j][z] == S_X_I_X:
                    Backtrace[iV][jW][zQ] = X_I_X()
                elif S[i][j][z] == S_I_X_X:
                    Backtrace[iV][jW][zQ] = I_X_X()
                elif S[i][j][z] == S_I_I_I:
                    Backtrace[iV][jW][zQ] = I_I_I()
    #print "\n".join(["\t".join(map(str, x)) for x in S])
    return Backtrace, S

def correctedWithSigma(S, M, N, R):
    for i in xrange(1, N):
        S[i][0][0] = 0 * i
    for j in xrange(1, M):
        S[0][j][0] = 0 * j
    for z in xrange(1, R):
        S[0][0][z] = 0 * z
    return S

# Backtrace presentation
def emptyBacktrace(M, N, R):
    Backtrace = []
    B1 = []
    [B1.append(["-"] * (R - 1)) for y in xrange(0, (M - 1))]
    [Backtrace.append(copy.deepcopy(B1)) for x in xrange(0, (N - 1))]
    return Backtrace

def I_X_X():
    return "| _ _"

def X_I_X():
    return "_ | _"

def X_X_I():
    return "_ _ |"

def I_I_X():
    return "| | _"

def I_X_I():
    return "| _ |"

def X_I_I():
    return "_ | |"

def I_I_I():
    return "| | |"
# def downB():
#     return "|"
#
# def rightB():
#     return "->"
#
# def diagonalB():
#     return '\\'

print outputLCSRun("CGGAACTGGT", "TGAGACGGTA", "TGCGACGGCT")
#print outputLCSRun("PLEASANTLY", "MEANLY")