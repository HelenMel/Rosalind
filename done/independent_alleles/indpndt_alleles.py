import math
import readFile

def run():
    values = readFile.lineFromInput().split();
    k = int(values[0])
    N = int(values[1])
    total = pow(2, k)
    probability = 0.25
    result = str(eventOccuredAtLeast(N, total, probability))
    print result
    readFile.lineToOutput(result)

def eventOccuredAtLeast(atLeast, total, probability):
    sumOfProbabilities = 0
    for i in range(atLeast, total + 1):
        sumOfProbabilities += occurrenceProbability(i, total, probability)
    return sumOfProbabilities
    
def occurrenceProbability(occur, total, probability):
    C = combination(occur, total)
    eP = eventProbability(probability, occur)
    eQ = oppositeEventProbability(probability, occur, total)
    return C * eP * eQ

def combination(occur, total):
    return math.factorial(total) / (math.factorial(occur) * math.factorial(total - occur))    

def eventProbability(probability, occur):
    return pow(probability, occur)

def oppositeEventProbability(probability, occur, total):
    q = 1 -  probability
    return pow(q, total - occur)
