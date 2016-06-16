import sys, os
import copy
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bio_6')))

import best_BWM_matching as bBM
import suffixArray as sA
import burrowWheeler as bW

def multipleApproximatePatternsMatching(Text, Patterns, d):
    assert isinstance(d, int)
    Text_ = Text + "$"
    LastColumn = bW.BWT(Text_)
    FirstColumn = bBM.firstColumn(LastColumn)
    compressionIndex = 5
    first_occurence = bBM.build_first_occurence(FirstColumn)
    partial_suffix = sA.partialSuffixArray(Text_, compressionIndex)
    partial_count = bBM.build_partial_count(LastColumn, compressionIndex)
    args = (FirstColumn, LastColumn, first_occurence, partial_count, partial_suffix, compressionIndex)
    IndexList = []
    for Pattern in Patterns:
        partlyMatches = seedsDetection(args, Pattern, d)
        if partlyMatches is not None:
            for matchIndex in partlyMatches:
                fullMatchIndex = seedsExtension(matchIndex, d, Text, Pattern)
                if fullMatchIndex is not None:
                    IndexList.append(str(fullMatchIndex))
    return sorted(IndexList)

# it can be too slow
def seedsExtension(matchIndex, d, Text, Pattern):
    relevantTextPart = Text[matchIndex: matchIndex + len(Pattern)]
    mismatch = 0
    for i in xrange(0, len(Pattern)):
        if Pattern[i] != relevantTextPart[i]:
            mismatch += 1
        if mismatch > d:
            return None
    return matchIndex

def seedsDetection(args, Pattern, d):
    FirstColumn = args[0]
    LastColumn = args[1]
    first_occurence = args[2]
    partial_count = args[3]
    partial_suffix = args[4]
    k = args[5]
    partsLength = len(Pattern) / (d + 1)
    parts = breakPatternToParts(Pattern, d + 1)
    matches = set()
    for i in xrange(0, len(parts)):
        part = parts[i]
        top, bottom = bBM.BWMatching(FirstColumn, LastColumn, part, first_occurence, partial_count, k)
        # check if at least one match exist
        if top <= bottom:
            for firstColumIndex in xrange(top, bottom + 1):
                partGlobalIndex = bBM.recover_index_from_partial_suffix_array(partial_suffix, firstColumIndex, LastColumn, partial_count, first_occurence, k)
                partLocalIndex = i * partsLength
                startPatternIndex = partGlobalIndex - partLocalIndex
                matches.add(startPatternIndex)
    if len(matches) > 0:
        return matches
    return None

def breakPatternToParts(Pattern, partsCount):
    partLength = len(Pattern) / (partsCount)
    Pattern_ = copy.copy(Pattern)
    parts = []
    for partI in xrange(0, partsCount - 1):
        parts.append(Pattern_[:partLength])
        Pattern_ = Pattern_[partLength:]
    parts.append(Pattern_)
    return parts