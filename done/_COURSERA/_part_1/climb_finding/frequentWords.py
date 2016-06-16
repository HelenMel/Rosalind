import readFile
import useful
import numberToPattern

def run():
    listOfLines = readFile.listFromInput()
    print listOfLines
    text = listOfLines[0]
    k = int(listOfLines[1])
    result = frequentWords(text, k)
    print result
    readFile.lineToOutput(result)

def frequencyArray(text, k):
    patterns = [0] * (pow(4,k))
    lastElement = len(text) - k + 1
    for i in range(0, lastElement):
        pattern = text[i : i + k]
        index = numberToPattern.patternToNumber(pattern)
        patterns[index] = patterns[index] + 1
    return patterns

def frequentWords(text, k):
    patterns = {}
    lastElement = len(text) - k + 1
    for i in range(0, lastElement):
        end = i + k
        pattern = text[i : end]
        value =0;
        if pattern in patterns:
            value = patterns[pattern]
        patterns[pattern] = value + 1
    max_value = max(patterns.values())
    most_frequent_line = ""
    for (pattern, count) in patterns.items():
        if count == max_value:
            most_frequent_line += pattern + " "
    return most_frequent_line
        
def patternCount(text, pattern):
    count = 0
    lastElement = len(text) - len(pattern) + 1
    for i in range(0, lastElement):
        end = i + len(pattern)
        if text[i: end] == pattern:
            count += 1
    return count
