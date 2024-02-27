import sys

if __name__ == '__main__':

    if len(sys.argv) != 2:
        sys.exit("Error: Faltan argumentos\n")

    file_in = open(sys.argv[1], "r")
    if file_in is None:
        sys.exit("Error: Apertura de fichero fallida\n")

    piso = 0
    character = file_in.read(1)
    while character != '':
        if character == "(":
            piso += 1
        elif character == ")":
            piso -= 1
        character = file_in.read(1)

    print("Piso final: " + str(piso))
