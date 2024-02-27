import sys

if __name__ == '__main__':

    if len(sys.argv) != 2:
        sys.exit("Error: Faltan argumentos\n")

    file_in = open(sys.argv[1], "r")
    if file_in is None:
        sys.exit("Error: Apertura de fichero fallida\n")

    total = 0
    line = file_in.readline()
    while line != "":
        dimension = [int(n) for n in line.split('x')]

        l = dimension[0]
        w = dimension[1]
        h = dimension[2]

        base = l * w
        wall1 = w * h
        wall2 = h * l

        min_len = base
        if wall1 < min_len:
            min_len = wall1
        if wall2 < min_len:
            min_len = wall2

        total += min_len + 2*base + 2*wall1 + 2*wall2
        line = file_in.readline()

    print("Total: " + str(total) + " pies")
