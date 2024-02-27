import sys

if __name__ == '__main__':

    if len(sys.argv) != 2:
        sys.exit("Error: Faltan argumentos")
    
    file_in = open(sys.argv[1], 'r')
    if file_in is None:
        sys.exit("Error: Apertura de fichero fallida")

    times = 50
    number = file_in.read()[:-1]

    while times > 0:
        counter = 0
        actual = ""
        new_number = ""
        for digit in number:
            if actual != digit:
                if actual != "":
                    new_number += str(counter) + actual
                actual = digit
                counter = 1
            else:
                counter += 1
        new_number += str(counter) + actual
        number = new_number
        times -= 1

    print(len(number))
