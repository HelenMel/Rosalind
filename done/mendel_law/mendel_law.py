import readFile

def run():
    population = make_population(readFile.lineFromInput())

    rp = reproduction(population, count(population), 1)
    rProb = reccesiveProbability(rp)
    result = str(1 - rProb)
    print result
    readFile.lineToOutput(result)

def count(population):
    return population ["k"] + population ["m"] + population ["n"]

def make_population(lines):
    inputs = lines.split(" ")
    return { "k" : int(inputs[0]), "m" : int(inputs[1]), "n" : int(inputs[2]) }

def reccesiveProbability(repr):
    reprN = repr.select("n")
    reprNN = reprN.select("n")
    reprNM = reprN.select("m")

    reprM = repr.select("m")
    reprMN = reprM.select("n")
    reprMM = reprM.select("m")
    return (reprNN.prob + reprNM.prob * 0.5 + reprMN.prob * 0.5 + reprMM.prob * 0.25)

class reproduction:
    def __init__(self, population = None, total = None, prob = None):
        self.population = population
        self.total = total
        self.prob = prob

    def select(self, key):
        keyCount = self.population[key]
        newPopulation = dict(self.population)
        newPopulation[key] = keyCount - 1
        newProb = self._new_prob(key)
        return reproduction(newPopulation, self.total - 1, newProb)

    def _new_prob(self, key):
        keyCount = self.population[key]
        new_prob = float(keyCount) / float(self.total)
        return self.prob * new_prob
