import sys
import hashlib

if __name__ == '__main__':

    if len(sys.argv) != 2:
        sys.exit("Error: Faltan argumentos")
    
    file_in = open(sys.argv[1], 'r')
    if file_in is None:
        sys.exit("Error: Apertura de fichero fallida")
  
    string = file_in.read()
    string = string[:-1]

    number = 1
    found = False
    while found == False:
        to_hash = string + str(number)
        hashed = hashlib.md5(to_hash.encode())
        hashed = hashed.hexdigest()

        if hashed[0:5] == "00000" and hashed[5] >= '0' and hashed[5] <= '9':
            found = True
        else:
            number += 1

    print("Numero para el hash: " + str(number))
