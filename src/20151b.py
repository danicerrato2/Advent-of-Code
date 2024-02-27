import sys

if __name__ == '__main__':

    if len(sys.argv) != 2:
        sys.exit("Error: Faltan argumentos\n")

    file_in = open(sys.argv[1], "r")
    if file_in is None:
        sys.exit("Error: Apertura de fichero fallida\n")

    piso = 0
    pos = 0
    character = file_in.read(1)
    while character != '' and piso != -1:
        if character is '(':
            piso += 1
        elif character is ')':
            piso -= 1
        pos += 1
        character = file_in.read(1)

    if piso == -1:
        print("Position: " + str(pos))
