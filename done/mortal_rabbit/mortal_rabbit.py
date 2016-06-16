import readFile

def run():
    line = readFile.lineFromInput()
    print line
    numbers = line.split();
    strn = numbers[0]
    n = int(strn)
    strk = numbers[1]
    m = int(strk)
    cache = {}
    answer = str(febonacci(n, m, cache))
    print answer
    print cache
    readFile.lineToOutput(answer)

def febonacci(n, lifespan, cache):
    if n in cache:
        return cache[n]
    if n < 0:
        return 0
    if n == 1 or n == 2:
        return 1;
    dieCurrent = die(n, lifespan, cache)
    diePrevious = die(n - 1, lifespan, cache)
    answer = febonacci(n - 1, lifespan, cache) + febonacci(n - 2, lifespan, cache) - dieCurrent - diePrevious
    cache[n] = answer
    return answer

def die(n, lifespan, cache):
    if n <= lifespan:
        return 0
    if (n - lifespan) == 1:
        return 1
    borned = born(n - lifespan, lifespan, cache)
    return borned
    
def born(n, lifespan, cache):
    if n < 0:
        return 0
    if n == 1:
        return 1
    born = febonacci(n - 2, lifespan, cache) - die(n - 1, lifespan, cache)
    return born
