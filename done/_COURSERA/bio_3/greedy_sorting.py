import copy

def parsePermutation(line):
    withoutBraces = line.translate(None, '()')
    parts = withoutBraces.split(" ")
    perm = []
    for numS in parts:
        numb = int(numS[1:])
        if numS[0] == '-':
            numb = -numb
        perm.append(numb)
    return perm

def permutationToString(perm):
    result = "("
    def numToString(num):
        start = "+"
        if num < 0:
            start = "-"
        start += str(abs(num))
        return start
    result += " ".join([numToString(n) for n in perm])
    result += ")"
    return result

def greedySorting(Permutation):
    approxReversalDistance = 0
    steps = [Permutation]
    for kIndex in xrange(0, len(Permutation)):
        prevStep = steps[-1]
        if not isSorted(kIndex, prevStep):
            newStep = sortingReversalPermutation(kIndex, prevStep)
            approxReversalDistance += 1
            steps.append(newStep); prevStep = newStep
        if isReversed(kIndex, prevStep):
            newStep = sortingReversalPermutation(kIndex, prevStep)
            approxReversalDistance += 1
            steps.append(newStep)
    print approxReversalDistance
    return steps

def isSorted(kIndex, permutation):
    k = kIndex + 1
    if abs(permutation[kIndex]) == k:
        return True
    return False

def isReversed(kIndex, permutation):
    return permutation[kIndex] < 0

def sortingReversalPermutation(kIndex, permutation):
    new_permutation = permutation[:kIndex]
    changes = []
    k = kIndex + 1
    index = kIndex
    while True:
        changes.append(-permutation[index])
        if index >= len(permutation):
            print "smth wrong"
        if abs(permutation[index]) == k:
            break
        index += 1
    new_permutation += changes[::-1]
    new_permutation += permutation[index + 1:]
    return new_permutation

def numberOfBreakpoints(Permutation):
    breakpoints = 0
    toCompare = [0] + Permutation + [len(Permutation) + 1]
    for kIndex in xrange(1, len(toCompare)):
        if toCompare[kIndex]!= toCompare[kIndex - 1] + 1:
            breakpoints += 1
    return breakpoints
