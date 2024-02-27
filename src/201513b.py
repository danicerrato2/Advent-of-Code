import sys

people = set()
pairs = {}

def calculate(sitted, max_happiness) -> int :
    happiness = 0
    for i in range(len(sitted)-1):
        happiness += pairs[sitted[i]][sitted[i+1]]
        happiness += pairs[sitted[i]][sitted[i-1]]
    happiness += pairs[sitted[-1]][sitted[-2]]
    happiness += pairs[sitted[-1]][sitted[0]]
    if happiness > max_happiness:
        max_happiness = happiness
    return max_happiness

def create_table(sitted, people, max_happiness) -> int :
    if len(people) == 0:
        return calculate(sitted, max_happiness)

    aux_people = people.copy() 
    for person in people:
        aux_people.remove(person)
        sitted.append(person)
        max_happiness = create_table(sitted, aux_people, max_happiness)
        sitted.remove(person)
        aux_people.append(person)
    return max_happiness

if __name__ == '__main__':

    if len(sys.argv) != 2:
        sys.exit("Error: Faltan argumentos")
    
    file_in = open(sys.argv[1], 'r')
    if file_in is None:
        sys.exit("Error: Apertura de fichero fallida")

    line = file_in.readline()[:-2]
    while line != '':
        splited = line.split()
        people.add(splited[0])
        if splited[2] == 'lose':
            value = - int(splited[3])
        else:
            value = int(splited[3])
        if splited[0] not in pairs.keys():
            pairs.update({splited[0]:{}})    
        pairs[splited[0]].update({splited[10]:value})

        line = file_in.readline()[:-2]

    pairs.update({'Me':{}})
    for person in people:
        pairs['Me'].update({person:0})
        pairs[person].update({'Me':0})
    people.add('Me')

    people = list(people)
    people.sort()
    aux_people = people.copy()
    first = people.pop(0)
    aux_people.remove(first)
    sitted = []
    sitted.append(first)
    max_happiness = 0
    for person in people:
        aux_people.remove(person)
        sitted.append(person)
        max_happiness = create_table(sitted, aux_people, max_happiness)
        aux_people.append(person)
        sitted.remove(person)
    
    print(max_happiness)
