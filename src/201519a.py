import sys

def is_to_search(substring, string) -> bool:
    if len(substring) > len(string):
        return False
    if substring == string[:len(substring)]:
        return True
    return False

def search_molecules(new_molecules, to_search, replacement, molecule) -> set:
    for i in range(len(molecule)):
        if molecule[i] == to_search[0] and is_to_search(to_search, molecule[i:]):
            new_molecule = molecule[:i] + replacement + molecule[i+len(to_search):]
            new_molecules.add(new_molecule)
    return new_molecules

if __name__ == '__main__':

    if len(sys.argv) != 2:
        sys.exit("Error: Faltan argumentos")
    
    file_in = open(sys.argv[1], 'r')
    if file_in is None:
        sys.exit("Error: Apertura de fichero fallida")

    replacements_list = {}

    line = file_in.readline()[:-1]
    while line != '':
        splited = line.split(' => ')
        if splited[0] not in replacements_list.keys():
            replacements_list.update({splited[0]:[splited[1]]})
        else:
            replacements_list[splited[0]].append(splited[1])
        line = file_in.readline()[:-1]
    
    initial_molecule = file_in.readline()[:-1]

    new_molecules = set()
    for replacements in replacements_list.items():
        for replace in replacements[1]:
            new_molecules = search_molecules(new_molecules, replacements[0], replace, initial_molecule)

    print(len(new_molecules))
