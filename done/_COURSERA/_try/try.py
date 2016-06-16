def DPChange(money, Coins):
    MinNumCoins = [money] * (money + 1)
    MinNumCoins[0] = 0
    for m in xrange(1, (money + 1)):
        for i in xrange(0, len(Coins)):
            coin_i = Coins[i]
            if m >= coin_i:
                if MinNumCoins[m - coin_i] + 1 < MinNumCoins[m]:
                    MinNumCoins[m] = MinNumCoins[m - coin_i] + 1
    return MinNumCoins[money]


def ManhattanTourist(n, m, Down, Right):
    N = n + 1
    M = m + 1
    S = [[0] * N] * M
    for i in xrange(1, len(N)):
        S[i][0] = S[i - 1][0] + Down[i][0]
    for j in xrange(1, len(M)):
        S[0][j] = S[0][j - 1] + Right[0][j]
    for i in xrange(1, len(N)):
        for j in xrange(1, len(M)):
            S[i][j] = max(S[i - 1][j] + Down[i][j], S[i][j - 1] + Right[i][j])
    return S[n][m]

# given strings v and w
def LCSBacktrack(v, w):
    N = len(v) + 1
    M = len(w) + 1
    S = [0 * N]  