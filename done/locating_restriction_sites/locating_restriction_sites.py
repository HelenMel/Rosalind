import readFile;
import useful;
import re

def run():
    DNA = readFile.FASTAline()
    comparator = Comparator(4, 12, DNA)
    result = comparator.compare()
    print result
    readFile.lineToOutput(result)


class Comparator:
    def __init__(self, min_same_len, max_same_len, s_original):
        self.min_s = min_same_len
        self.max_s = max_same_len
        self.sO = s_original
        self.result = ""
        self.count = 0

    def compare(self):
        self.result = ""
        self.count = 0
        stop = len(self.sO) - self.min_s + 1
        for i in range(0, stop):
            polindromLen = self.max_s
            if i > len(self.sO) - self.max_s:
                polindromLen = len(self.sO) - i
            self._searchPolindrome(i, polindromLen)
        print self.count
        return self.result.rstrip("\n")
        
    def _searchPolindrome(self, i, length):
        #min
        if length < self.min_s:
            return
        end = i + length
        sub_s = self.sO[i : end]
        i_sub_s = useful.invertDNA(sub_s)
        if (sub_s == i_sub_s):
            self._save(i, length)
        self._searchPolindrome(i, length - 1)

    def _save(self, i, length):
        self.count += 1
        self.result += str(i + 1) + " " + str(length) + "\n"
