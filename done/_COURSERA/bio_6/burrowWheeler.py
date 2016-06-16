def BWT(Text):
    def shift(x, i):
        return x[i:] + x[:i]
    cyclicItems = [shift(Text, i) for i in xrange(0, len(Text))]
    sortedItems = sorted(cyclicItems)
    return "".join([s[-1] for s in sortedItems])
