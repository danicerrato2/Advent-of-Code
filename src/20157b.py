import sys

if __name__ == '__main__':

    if len(sys.argv) != 2:
        sys.exit("Error: Faltan argumentos")
    
    file_in = open(sys.argv[1], 'r')
    if file_in is None:
        sys.exit("Error: Apertura de fichero fallida")
  
    assign = []
    prepared = []
    line = file_in.readline()
    while line != '':
        splited = line.split(' -> ')
        if splited[1] == 'b\n':
            splited[0] = ['3176']
        else:
            splited[0] = splited[0].split()
        to_calculate = True
        for i in range(len(splited[0])):
            if splited[0][i][0] >= 'a' and splited[0][i][0] <= 'z':
                assign.append((splited[1][:-1], splited[0]))
                to_calculate = False
                break

        if to_calculate == True:
            prepared.append((splited[1][:-1], splited[0]))

        line = file_in.readline()

    finished = {}
    while len(assign) != 0:
        for tupla in prepared:
            value = tupla[1]
            if len(value) == 1:
                finished[tupla[0]] = value[0]
            elif len(value) == 2:
                finished[tupla[0]] = str(65535 - int(value[1]))
            elif len(value) == 3:
                if value[1] == 'AND':
                    finished[tupla[0]] = str(int(value[0]) & int(value[2]))
                elif value[1] == 'OR':
                    finished[tupla[0]] = str(int(value[0]) | int(value[2]))
                elif value[1] == 'RSHIFT':
                    finished[tupla[0]] = str(int(value[0]) >> int(value[2]))
                elif value[1] == 'LSHIFT':
                    finished[tupla[0]] = str(int(value[0]) << int(value[2]))
        prepared.clear()
       
        counter = 0
        for key in finished:
            value = finished[key]
            for tupla in assign:
                if key in tupla[1]:
                    tupla[1][tupla[1].index(key)] = value
                to_calculate = True
                for i in range(len(tupla[1])):
                    if tupla[1][i][0] >= 'a' and tupla[1][i][0] <= 'z':
                        to_calculate = False

                if to_calculate == True:
                    prepared.append(tupla)
                    assign.remove(tupla)

    for tupla in prepared:
        value = tupla[1]
        if len(value) == 1:
            finished[tupla[0]] = value[0]
        elif len(value) == 2:
            finished[tupla[0]] = str(65535 - int(value[1]))
        elif len(value) == 3:
            if value[1] == 'AND':
                finished[tupla[0]] = str(int(value[0]) & int(value[2]))
            elif value[1] == 'OR':
                finished[tupla[0]] = str(int(value[0]) | int(value[2]))
            elif value[1] == 'RSHIFT':
                finished[tupla[0]] = str(int(value[0]) >> int(value[2]))
            elif value[1] == 'LSHIFT':
                finished[tupla[0]] = str(int(value[0]) << int(value[2]))

    print(finished['a'])
