import sys

if __name__ == '__main__':

    if len(sys.argv) != 2:
        sys.exit("Error: Faltan argumentos")
    
    file_in = open(sys.argv[1], 'r')
    if file_in is None:
        sys.exit("Error: Apertura de fichero fallida")
   
    houses_and_visits = {}
    actual = [(0,0), (0,0)]
    houses_and_visits[actual[0]] = 2
    correct = False
    counter = 0
    
    character = file_in.read(1)
    while character != '':
        if character == '<':
            actual[counter%2] = (actual[counter%2][0], actual[counter%2][1] - 1)
            correct = True
        elif character == '>':
            actual[counter%2] = (actual[counter%2][0], actual[counter%2][1] + 1)
            correct = True
        elif character == 'v':
            actual[counter%2] = (actual[counter%2][0] + 1, actual[counter%2][1])
            correct = True
        elif character == '^':
            actual[counter%2] = (actual[counter%2][0] - 1, actual[counter%2][1])
            correct = True
         
        if actual[counter%2] in houses_and_visits and correct == True:
            houses_and_visits[actual[counter%2]] += 1
        elif correct == True:
            houses_and_visits[actual[counter%2]] = 1
        
        character = file_in.read(1)
        counter += 1
        correct = False
    
    print("Casas del reparto Robo-Santa y Santa: " + str(len(houses_and_visits)))
