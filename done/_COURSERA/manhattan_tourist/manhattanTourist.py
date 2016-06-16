def extendDown(Down):
    first = [0] * len(Down[0])
    Down.insert(0, first)

def extendRight(Right):
    [one.insert(0, 0) for one in Right]

def ManhattanTourist(n, m, Down, Right):
    N = n + 1
    M = m + 1
    S = []
    [S.append([0] * M) for x in xrange(0, N)]
    # i - move Y axis
    for i in xrange(1, N):
        S[i][0] = S[i - 1][0] + Down[i][0]
    # j - move X axis
    for j in xrange(1, M):
        S[0][j] = S[0][j - 1] + Right[0][j]
    for i in xrange(1, N):
        for j in xrange(1, M):
            S[i][j] = max(S[i - 1][j] + Down[i][j], S[i][j - 1] + Right[i][j])
    return S[n][m]