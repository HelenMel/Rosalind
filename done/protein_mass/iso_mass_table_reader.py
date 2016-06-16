import readFile

def table():
    tableLines = readFile.listFromFile('iso_mass_table.txt');
    table = {}
    for line in tableLines:
        items = line.split("   ")
        table[items[0]] = items[1]
    return table
