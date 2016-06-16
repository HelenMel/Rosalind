def suffixArray(Text):
    sArrayWithIndexes = [(x, Text[x:]) for x in xrange(0, len(Text))]
    sArrayWithIndexes = sorted(sArrayWithIndexes, key = lambda x: x[1])
    return [x[0] for x in sArrayWithIndexes]

def partialSuffixArray(Text, k):
    fullArray = suffixArray(Text)
    partial = {}
    for i in xrange(0, len(fullArray)):
        value = fullArray[i]
        if value % k == 0:
            partial[i] = value
    return partial