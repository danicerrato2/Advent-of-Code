import sys

if __name__ == '__main__':

    if len(sys.argv) != 2:
        sys.exit("Error: Faltan argumentos")
    
    file_in = open(sys.argv[1], 'r')
    if file_in is None:
        sys.exit("Error: Apertura de fichero fallida")

    reindeers = {}
    aux_reindeers = {}
    goal_distance = 2503
    max_distance = 0

    line = file_in.readline()[:-2]
    while line != '':
        splited = line.split()
        reindeers.update({splited[0]: [int(splited[3]), int(splited[6]), int(splited[13]), 0]})
        aux_reindeers.update({splited[0]: [int(splited[3]), int(splited[6]), int(splited[13]), 0]})
        line = file_in.readline()[:-2]

    active = []
    resting = []
    for deer in reindeers.keys():
        active.append(deer)
    
    while goal_distance > 0:
        for deer in reindeers.keys():
            if deer in resting:
                aux_reindeers[deer][2] -= 1
                if aux_reindeers[deer][2] == 0:
                    aux_reindeers[deer][2] = reindeers[deer][2]
                    resting.remove(deer)
                    active.append(deer)
            else:
                aux_reindeers[deer][3] += reindeers[deer][0]
                aux_reindeers[deer][1] -= 1
                if aux_reindeers[deer][1] == 0:
                    aux_reindeers[deer][1] = reindeers[deer][1]
                    resting.append(deer)
                    active.remove(deer)
                if max_distance < aux_reindeers[deer][3]:
                    max_distance = aux_reindeers[deer][3]
        for deer in aux_reindeers.keys():
            if aux_reindeers[deer][3] == max_distance:
                reindeers[deer][3] += 1
        goal_distance -= 1
    
    max_points = 0
    for deer_points in reindeers.values():
        if deer_points[3] > max_points:
            max_points = deer_points[3]

    print(max_points)
