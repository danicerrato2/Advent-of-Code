import sys

if __name__ == '__main__':

    if len(sys.argv) != 2:
        sys.exit("Error: Faltan argumentos")
    
    file_in = open(sys.argv[1], 'r')
    if file_in is None:
        sys.exit("Error: Apertura de fichero fallida")
  
    correct_words = 0

    word = file_in.readline()
    while word != '':
        repetead_letter = False
        repetead_pair = False
        for i in range(len(word) - 2):
            if repetead_letter == False and word[i] == word[i+2]:
                repetead_letter = True
            if repetead_pair == False:
                for j in range(i+2, len(word)):
                    if word[i:i+2] == word[j:j+2]:
                        repetead_pair = True
                        break
            
        if repetead_pair == True and repetead_letter == True:
            correct_words += 1

        word = file_in.readline()

    print("Palabras correctas: " + str(correct_words))
