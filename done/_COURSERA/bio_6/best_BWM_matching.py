import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_6')))

import burrowWheelerTransform as bWT
import suffixArray as sA
import burrowWheeler as bW

# mutate Pattern!

def bestBWMatchingRun(Text, Patterns):
    Text_ = Text + "$"
    LastColumn = bW.BWT(Text_)
    FirstColumn = firstColumn(LastColumn)
    compressionIndex = 100
    first_occurence = build_first_occurence(FirstColumn)
    partial_suffix = sA.partialSuffixArray(Text_, compressionIndex)
    partial_count = build_partial_count(LastColumn, compressionIndex)

    def matchIndexesForPattern(Pattern, IndexList):
        top, bottom = BWMatching(FirstColumn, LastColumn, Pattern, first_occurence, partial_count, compressionIndex)
        for firstColumIndex in xrange(top, bottom + 1):
            index = recover_index_from_partial_suffix_array(partial_suffix, firstColumIndex, LastColumn, partial_count, first_occurence, compressionIndex)
            IndexList.append(str(index))
    IndexList = []
    for Pattern in Patterns:
        matchIndexesForPattern(Pattern, IndexList)
    return sorted(IndexList)

def firstColumn(LastColumn):
    return sorted(LastColumn)

# we should delete eventually last to first pattern
def BWMatching(FirstColumn, LastColumn, Pattern, first_occurence, partial_count, k):
    top = 0
    bottom = len(LastColumn) - 1
    while top <= bottom:
        if len(Pattern) > 0:
            symbol = Pattern[-1]
            Pattern = Pattern[:-1]
            topRank = recover_count_at_index(partial_count, k, LastColumn, top, symbol) + 1
            bottomRank = recover_count_at_index(partial_count, k, LastColumn, bottom + 1, symbol)
            if topRank <= bottomRank:
                top = first_occurence[symbol] + topRank - 1
                bottom = first_occurence[symbol] + bottomRank - 1
            else:
                return 0, -1
        else:
            return top, bottom

def build_first_occurence(FirstColumn):
    firstOccur = {}
    for i in xrange(0, len(FirstColumn)):
        if FirstColumn[i] not in firstOccur:
            firstOccur[FirstColumn[i]] = i
    return firstOccur

def build_count(LastColumn):
    Count = {}
    for i in xrange(1, len(LastColumn) + 1):
        symbol = LastColumn[i - 1]
        if symbol not in Count:
            Count[symbol] = [0] * (len(LastColumn) + 1)
        lastCount = Count[symbol][i - 1]
        Count[symbol][i] = lastCount + 1
        for other_symbol in LastColumn:
            if other_symbol is not symbol and other_symbol in Count:
                Count[other_symbol][i] = Count[other_symbol][i - 1]
    return Count

def build_partial_count(LastColumn, k):
    count = build_count(LastColumn)
    def f(x): return
    partialCount = {}
    for symbol, list in count.items():
        partialList = [x for i, x in enumerate(list) if i % k  == 0]
        partialCount[symbol] = partialList
    return partialCount

def recover_count_at_index(partial_count, k, LastColumn, index, symbol):
    nearestCompressedIndex = (index / k)
    occurence = partial_count[symbol][nearestCompressedIndex]
    for i in xrange(nearestCompressedIndex * k, index):
        if LastColumn[i] == symbol:
            occurence += 1
    return occurence

def recover_index_from_partial_suffix_array(partial, index, LastColumn, partial_count, first_occurence, k):
    if index in partial:
        return partial[index]
    diff = 0
    nearestIndex = -1
    currentIndex = index
    while True:
        diff += 1
        # TODO: replace with valid getting index function
        symbol = LastColumn[currentIndex]
        currentIndex = first_occurence[symbol] + recover_count_at_index(partial_count, k, LastColumn, currentIndex, symbol)
        if currentIndex in partial:
            nearestIndex = partial[currentIndex]
            break
    return nearestIndex + diff

# to check smnpbnnaaaaa$a
#print bestBWMatchingRun("AATCGGGTTCAATCGGGGT", ["ATCG", "GGGT"])
LastColumn = "smnpbnnaaaaa$a"
#partialCount = build_partial_count(LastColumn, 5)
#print recover_count_at_index(partialCount, 5, LastColumn, 3, "p")