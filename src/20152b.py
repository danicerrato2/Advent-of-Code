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

        min1 = l
        min2 = w
        if h < l:
            min1 = h
            if l < w:
                min2 = l
        elif h < w:
            min2 = h

        total += 2*min1 + 2*min2 + l*w*h
        line = file_in.readline()

    print("Total: " + str(total) + " pies")
