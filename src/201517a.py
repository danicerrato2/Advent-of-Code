import sys

def combine(containers, litres, total_combinations) -> int:
    aux_containers = containers.copy()

    for container in containers:
        litres_left = litres - container
        aux_containers.remove(container)
        if litres_left > 0:
            total_combinations = combine(aux_containers, litres_left, total_combinations)
        elif litres_left == 0:
            total_combinations += 1
        litres_left += container
    return total_combinations

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

    total_combinations = combine(containers, 150, 0)

    print(total_combinations)
