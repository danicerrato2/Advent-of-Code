import sys

replacements_list = {}
replaces = []
molecules = set()

def calculate_steps(molecule, min_steps, steps) -> int:
    if molecule == 'e':
        if min_steps > steps:
            min_steps = steps
        print(min_steps)
        return min_steps

    stack = ''

    for i in range(len(molecule)):
        stack += molecule[i]
        for replace in replaces:
            if len(replace) <= len(stack) and replace == stack[-len(replace):]:
                new_molecule = stack[:-len(replace)] + replacements_list[replace] + molecule[i+1:]
                if new_molecule not in molecules and steps < min_steps:
                    molecules.add(new_molecule)
                    min_steps = calculate_steps(new_molecule, min_steps, steps+1)
    return min_steps

if __name__ == '__main__':

    if len(sys.argv) != 2:
        sys.exit("Error: Faltan argumentos")

    file_in = open(sys.argv[1], 'r')
    if file_in is None:
        sys.exit("Error: Apertura de fichero fallida")

    line = file_in.readline()[:-1]
    while line != '':
        splited = line.split(' => ')
        replacements_list.update({splited[1]:splited[0]})
        replaces.append(splited[1])
        line = file_in.readline()[:-1]

    initial_molecule = file_in.readline()[:-1]
    replaces.sort(key=len, reverse=True)

    num_steps = calculate_steps(initial_molecule, len(initial_molecule), 0)

    print(num_steps)
