# жесткие тормоза при считывании array
import readFile
import useful

def run():
    listOfLines = readFile.listFromInput()
    print listOfLines
    length = int(listOfLines[0])
    sequence = listOfLines[1].split(" ")
    search = sequenceSearch(sequence)
    print sequence
    #result = search.shortestSubsequence() + "\n"
    #result += search.longestSubsequence()
    #print result
    readFile.lineToOutput(result)

# adding lambda for comparing

class sequenceSearch:
    def __init__(self, sequence):
        self.sequence = sequence

    def shortestSubsequence(self):
        cache = {}
        comparator = lambda f, s: int(f) >= int(s)
        state = (cache, comparator)
        array = self._subsequence(self.sequence, state)
        return " ".join(array)

# if element is more than biggest element
# just adding it
# if element is less tan biggest element, we should remove biggest
# element from previous subsequence
# if length is the same or bigger, than lets return it
# if length is less than previouse subsequence is biggest
    def longestSubsequence(self):
        cache = {}
        comparator = lambda f, s: int(f) <= int(s)
        state = (cache, comparator)
        array = self._subsequence(self.sequence, state)
        return " ".join(array)
    
    def _subsequence(self, sequence, state):
        cache, comparator = state
        # cache the data
        if str(sequence) in cache:
            return cache[str(sequence)]
        s_c = list(sequence)
        print s_c
        cacheData = (sequence, cache)
        # zero state
        if len(s_c) == 1:
            return s_c
        # dynamic algorithm
        element = s_c.pop(0)
        previous = self._subsequence(s_c, state)
        prev_biggest = previous[0]
        if comparator(prev_biggest, element):
            return self._saveAndReturn([element] + previous, cacheData)
        else:
            if len(s_c) == 1:
                return self._saveAndReturn([element], cacheData)
            s_c.remove(prev_biggest)
            shorter = self._subsequence(s_c, state)
            if comparator(shorter[0], element) and len(shorter) >= (len(previous) - 1):
                return self._saveAndReturn([element] + shorter, cacheData)
            else:
                return self._saveAndReturn(previous, cacheData)

    def _saveAndReturn(self, findedArray, cacheData):
        subsequence, cache = cacheData
        key = str(subsequence)
        cache[key] = findedArray
        return findedArray
    
