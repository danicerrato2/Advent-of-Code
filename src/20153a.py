import sys

if __name__ == '__main__':

    if len(sys.argv) != 2:
        sys.exit("Error: Faltan argumentos")
    
    file_in = open(sys.argv[1], 'r')
    if file_in is None:
        sys.exit("Error: Apertura de fichero fallida")
   
    houses_and_visits = {}
    actual = (0,0)
    houses_and_visits[actual] = 1
    correct = False
    
    character = file_in.read(1)
    while character != '':
        if character == '<':
            actual = (actual[0], actual[1] - 1)
            correct = True
        elif character == '>':
            actual = (actual[0], actual[1] + 1)
            correct = True
        elif character == 'v':
            actual = (actual[0] + 1, actual[1])
            correct = True
        elif character == '^':
            actual = (actual[0] - 1, actual[1])
            correct = True
         
        if actual in houses_and_visits and correct == True:
            houses_and_visits[actual] += 1
        elif correct == True:
            houses_and_visits[actual] = 1
        
        character = file_in.read(1)
        correct = False
        
    print("Casas del reparto de Santa: " + str(len(houses_and_visits)))
