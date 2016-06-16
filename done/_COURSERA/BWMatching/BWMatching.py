import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_6')))

import burrowWheelerTransform as bWT

# mutate Pattern!
def BWMatchingRun(LastColumn, Patterns):
    FirstColumn = firstColumn(LastColumn)
    LastToFirst = lastToFirst(FirstColumn, LastColumn)
    def matchForPattern(Pattern):
        return BWMatching(FirstColumn, LastColumn, Pattern, LastToFirst) 
    return [ matchForPattern(p) for p in Patterns ]

def firstColumn(LastColumn):
    return sorted(LastColumn)

def lastToFirst(FirstColumn, LastColumn):
    numFirst = bWT.textToNumerated(FirstColumn)
    numLast = bWT.textToNumerated(LastColumn)
    LastToFirst = []
    [LastToFirst.append(numFirst.index(x)) for x in numLast]
    return LastToFirst

def BWMatching(FirstColumn, LastColumn, Pattern, LastToFirst):
    top = 0
    bottom = len(LastColumn) - 1
    while top <= bottom:
        if len(Pattern) > 0:
            symbol = Pattern[-1]
            Pattern = Pattern[:-1]
            topIndex = -1; bottomIndex = -1
            for i in xrange(top, bottom + 1):
                if LastColumn[i] == symbol:
                    if topIndex == -1:
                        topIndex = i
                    bottomIndex = i
            # there is no such symbol
            if topIndex == -1:
                return 0
            top = LastToFirst[topIndex]
            bottom = LastToFirst[bottomIndex]
        else:
            return bottom - top + 1

# to check smnpbnnaaaaa$a
