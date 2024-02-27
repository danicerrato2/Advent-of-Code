import sys

if __name__ == '__main__':

    if len(sys.argv) != 2:
        sys.exit("Error: Faltan argumentos")
    
    file_in = open(sys.argv[1], 'r')
    if file_in is None:
        sys.exit("Error: Apertura de fichero fallida")

    reindeers = {}
    goal_distance = 2503
    max_distance = 0

    line = file_in.readline()[:-2]
    while line != '':
        splited = line.split()
        reindeers.update({splited[0]: [int(splited[3]), int(splited[6]), int(splited[13])]})
        line = file_in.readline()[:-2]
        
    for deer in reindeers.values():
        aux_goal = goal_distance
        distance = 0
        while aux_goal > 0:
            if aux_goal >= deer[1]:
                distance += deer[0] * deer[1]
                aux_goal -= deer[1]
            else:
                distance += deer[0] * aux_goal
                break
            if aux_goal >= deer[2]:
                aux_goal -= deer[2]
            else:
                break
        if distance > max_distance:
            max_distance = distance

    print(max_distance)
