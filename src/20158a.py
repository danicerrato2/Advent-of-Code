import sys

if __name__ == '__main__':

    if len(sys.argv) != 2:
        sys.exit("Error: Faltan argumentos")
    
    file_in = open(sys.argv[1], 'r')
    if file_in is None:
        sys.exit("Error: Apertura de fichero fallida")
 
    code_string_size = 0
    memory_string_size = 0
    line = file_in.readline()[:-1]
    while line != '':
        code_string_size += len(line)
        i = 0
        while i < len(line):
            if line[i] != '"' and line[i] != '\\':
                memory_string_size += 1
            elif line[i:i+2] == '\\x':
                i += 2
            elif line[i:i+2] == '\\"' or line[i:i+2] == '\\\\':
                memory_string_size += 1
                i += 1
            i += 1
        line = file_in.readline()[:-1]

    diff_string_sizes = code_string_size - memory_string_size

    print("Difference between string sizes: " + str(diff_string_sizes))
