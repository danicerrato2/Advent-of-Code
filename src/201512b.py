import sys
import json

def calculate(data, total) -> int:
    if data.__class__.__name__ == 'int':
        total += data
    elif data.__class__.__name__ == 'list':
        for item in data:
            total = calculate(item, total)
    elif data.__class__.__name__ == 'dict':
        if 'red' not in data.values():
            for item in data.values():
                total = calculate(item, total)
    return total


if __name__ == '__main__':

    if len(sys.argv) != 2:
        sys.exit("Error: Faltan argumentos")
    
    file_in = open(sys.argv[1], 'r')
    if file_in is None:
        sys.exit("Error: Apertura de fichero fallida")

    data = json.load(file_in)
    
    total = calculate(data, 0)

    print(total)
