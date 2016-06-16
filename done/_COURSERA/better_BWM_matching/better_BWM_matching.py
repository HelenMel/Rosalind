import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_6')))

import burrowWheelerTransform as bWT

# mutate Pattern!
def BWMatchingRun(LastColumn, Patterns):
    FirstColumn = firstColumn(LastColumn)
    first_occurence = build_first_occurence(FirstColumn)
    count = build_count(LastColumn)
    def matchForPattern(Pattern):
        return BWMatching(FirstColumn, LastColumn, Pattern, first_occurence, count)
    return [ matchForPattern(p) for p in Patterns ]

def firstColumn(LastColumn):
    return sorted(LastColumn)

# we should delete eventually last to first pattern
def BWMatching(FirstColumn, LastColumn, Pattern, first_occurence, count):
    top = 0
    bottom = len(LastColumn) - 1
    while top <= bottom:
        if len(Pattern) > 0:
            symbol = Pattern[-1]
            Pattern = Pattern[:-1]
            topRank = count[symbol][top] + 1
            bottomRank = count[symbol][bottom + 1]
            if topRank <= bottomRank:
                top = first_occurence[symbol] + count[symbol][top]
                bottom = first_occurence[symbol] + count[symbol][bottom + 1] - 1
            else:
                return 0
        else:
            return bottom - top + 1

def build_first_occurence(Text):
    firstOccur = {}
    for i in xrange(0, len(Text)):
        if Text[i] not in firstOccur:
            firstOccur[Text[i]] = i
    return firstOccur

def build_count(Text):
    Count = {}
    for i in xrange(1, len(Text) + 1):
        symbol = Text[i - 1]
        if symbol not in Count:
            Count[symbol] = [0] * (len(Text) + 1)
        lastCount = Count[symbol][i - 1]
        Count[symbol][i] = lastCount + 1
        for other_symbol in Text:
            if other_symbol is not symbol and other_symbol in Count:
                Count[other_symbol][i] = Count[other_symbol][i - 1]
    return Count


# to check smnpbnnaaaaa$a
