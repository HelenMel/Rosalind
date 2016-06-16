import readFile
import iso_mass_table_reader

def run():
    line = readFile.lineFromInput()
    mass_table = iso_mass_table_reader.table()
    total_mass = getMassSum(line, mass_table)
    result = str(total_mass)
    print result
    readFile.lineToOutput(result)

def getMassSum(line, mass_table):
    total_mass = 0.0
    for char in line:
        if char in mass_table:
            total_mass += float(mass_table[char])
    return total_mass
    
