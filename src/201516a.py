import sys

if __name__ == '__main__':

    if len(sys.argv) != 2:
        sys.exit("Error: Faltan argumentos")
    
    file_in = open(sys.argv[1], 'r')
    if file_in is None:
        sys.exit("Error: Apertura de fichero fallida")

    aunts = {}
    machine_list = [('children',3),('cats',7),('samoyeds',2),
            ('pomeranians',3),('akitas',0),('vizslas',0),
            ('goldfish',5),('trees',3),('cars',2),('perfumes',1)]

    line = file_in.readline()
    while line != '':
        splited = line.split()
        aunts.update({int(splited[1][:-1]):{
            splited[2][:-1]:int(splited[3][:-1]),
            splited[4][:-1]:int(splited[5][:-1]),
            splited[6][:-1]:int(splited[7])            
            }})
        line = file_in.readline()[:-1]   

    aunts_left = {}
    for compound in machine_list:
        for aunt in aunts.items():
            if compound[0] in aunt[1].keys():
                if compound[1] == aunt[1][compound[0]]:
                    aunts_left.update({aunt[0]:aunt[1]})
            else:
                aunts_left.update({aunt[0]:aunt[1]})
        aunts = aunts_left.copy()
        aunts_left = {}

    print(aunts)
