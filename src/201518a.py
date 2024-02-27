import sys

def update_light(lights, x, y) -> bool:
    max_table = len(lights)
    counter_on = 0
    
    for i in range(x-1, x+2):
        if i >= 0 and i < max_table:
            for j in range(y-1, y+2):
                if j >= 0 and j < max_table:
                    if (x != i or y != j) and lights[i][j] == '#':
                        counter_on += 1
    
    if lights[x][y] == '#':
        if counter_on == 2 or counter_on == 3:
            return True
    else:
        if counter_on == 3:
            return True
    return False


def next_step(lights) -> list():
    updated_lights = []

    for i in range(len(lights)):
        row = []
        for j in range(len(lights)):
            is_on = update_light(lights, i, j)
            if is_on == True:
                row.append('#')
            else:
                row.append('.')
        updated_lights.append(row)
    return updated_lights

if __name__ == '__main__':

    if len(sys.argv) != 2:
        sys.exit("Error: Faltan argumentos")
    
    file_in = open(sys.argv[1], 'r')
    if file_in is None:
        sys.exit("Error: Apertura de fichero fallida")

    lights = []
    steps = 100

    line = file_in.readline()[:-1]
    while line != '':
        row = [letter for letter in line]
        lights.append(row)
        line = file_in.readline()[:-1]   

    while steps > 0:
        lights = next_step(lights)
        steps -= 1
    
    lights_on = 0
    for i in range(len(lights)):
        for j in range(len(lights)):
            if lights[i][j] == '#':
                lights_on += 1

    print(lights_on)
