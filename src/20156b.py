import sys

if __name__ == '__main__':

    if len(sys.argv) != 2:
        sys.exit("Error: Faltan argumentos")
    
    file_in = open(sys.argv[1], 'r')
    if file_in is None:
        sys.exit("Error: Apertura de fichero fallida")
  
    grid = []
    for i in range(0,1000):
        grid.append([])
        for j in range(0,1000):
            grid[i].append(0)

    command = file_in.readline()
    while command != '':
        splited_command = command.split()
        if splited_command[0] == 'turn': 
            initial = [int(n) for n in splited_command[2].split(',')]
            final = [int(n) for n in splited_command[4].split(',')]
            if splited_command[1] == 'on':
                turn_to = 1
            elif splited_command[1] == 'off':
                turn_to = -1
            for i in range(initial[0], final[0] + 1):
                for j in range(initial[1], final[1] + 1):
                    grid[i][j] += turn_to
                    if grid[i][j] == -1:
                        grid[i][j] = 0
        elif splited_command[0] == 'toggle': 
            initial = [int(n) for n in splited_command[1].split(',')]
            final = [int(n) for n in splited_command[3].split(',')]
            for i in range(initial[0], final[0] + 1):
                for j in range(initial[1], final[1] + 1):
                    grid[i][j] += 2

        command = file_in.readline()

    counter = 0
    for i in range(1000):
        for j in range(1000):
            counter += grid[i][j]

    print("Grid's bright: " + str(counter))
