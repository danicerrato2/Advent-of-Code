import sys

def combine(containers, litres, total_combinations, num_containers, min_containers) -> (int, int):
    aux_containers = containers.copy()

    for container in containers:
        litres_left = litres - container
        aux_containers.remove(container)
        if litres_left > 0:
            (total_combinations, min_containers) = combine(aux_containers, litres_left, total_combinations, num_containers + 1, min_containers)
        elif litres_left == 0:
            if num_containers < min_containers:
                total_combinations = 1
                min_containers = num_containers
            elif num_containers == min_containers:
                total_combinations += 1
        litres_left += container
    return (total_combinations, min_containers)

if __name__ == '__main__':

    if len(sys.argv) != 2:
        sys.exit("Error: Faltan argumentos")
    
    file_in = open(sys.argv[1], 'r')
    if file_in is None:
        sys.exit("Error: Apertura de fichero fallida")

    containers = []

    line = file_in.readline()[:-1]
    while line != '':
        containers.append(int(line))
        line = file_in.readline()[:-1]   

    containers.sort(reverse=True)

    (total_combinations, min_containers) = combine(containers, 150, 0, 0, len(containers))

    print(total_combinations)
