import readFile

def run():
    line = readFile.lineFromInput()
    print line
    numbers = line.split();
    strn = numbers[0]
    n = int(strn)
    strk = numbers[1]
    k = int(strk)
    cache = {}
    answer = str(febonacci(n, k, cache))
    print answer
    readFile.lineToOutput(answer)

def febonacci(n, step, cache):
    if n in cache:
        return cache[n]
    if n == 1 or n == 2:
        return 1;
    answer = febonacci(n - 1, step, cache) + febonacci(n - 2, step, cache) * step
    cache[n] = answer
    return answer
