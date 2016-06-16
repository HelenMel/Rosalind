import readFile

def run():
    line = readFile.lineFromInput()
    groups_pairs = line.split()
    print groups_pairs
    expected_offsprings = 0.0
    group_num = 0
    for group_pairs in groups_pairs:
        expected_offsprings += expected_offsprings_in_group(group_num, int(group_pairs))
        group_num += 1
    result = str(expected_offsprings)
    print result
    readFile.lineToOutput(result)

def groupProbability(group_num):
    return probabilities()[group_num]
    
def probabilities():
    return [ 1, 1, 1, 0.75, 0.5, 0]

def expected_offsprings_in_group(group_num, group_pairs):
    offsprings_count = 2
    probability = groupProbability(group_num)
    return offsprings_count * probability * group_pairs
    
