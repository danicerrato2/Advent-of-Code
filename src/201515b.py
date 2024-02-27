import sys

qualities = {}
quantities = {}
ingredients = []

def calculate(max_puntuation) -> int:
    actual = [0,0,0,0,0]
    
    for ingredient in qualities.keys():
        for i in range(5):
            actual[i] += qualities[ingredient][i] * quantities[ingredient]

    puntuation = 1
    for i in range(4):
        if actual[i] < 0:
            return max_puntuation
        puntuation *= actual[i]
    
    if actual[4] == 500 and max_puntuation < puntuation:
        return puntuation
    return max_puntuation

def generate_variations(max_teaspoons, max_puntuation) -> int:
    if len(ingredients) == 0:
        total = 0
        for value in quantities.values():
            total += value
        if total != 100:
            return max_puntuation
        return calculate(max_puntuation)

    ingredient = ingredients.pop(-1)
    quantities[ingredient] = max_teaspoons
    while quantities[ingredient] >= 0:
        teaspoons_left = max_teaspoons - quantities[ingredient]
        max_puntuation = generate_variations(teaspoons_left, max_puntuation)
        quantities[ingredient] -= 1

    quantities[ingredient] = 0
    ingredients.append(ingredient)
    return max_puntuation

if __name__ == '__main__':

    if len(sys.argv) != 2:
        sys.exit("Error: Faltan argumentos")
    
    file_in = open(sys.argv[1], 'r')
    if file_in is None:
        sys.exit("Error: Apertura de fichero fallida")

    line = file_in.readline()[:-1]
    while line != '':
        splited = line.split()
        qualities.update({splited[0][:-1]:[int(splited[2][:-1]), int(splited[4][:-1]), int(splited[6][:-1]), int(splited[8][:-1]), int(splited[10])]})
        quantities.update({splited[0][:-1]:0})
        ingredients.append(splited[0][:-1])
        line = file_in.readline()[:-1]
        
    max_puntuation = generate_variations(100, 0)

    print(max_puntuation)
