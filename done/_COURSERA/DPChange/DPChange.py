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