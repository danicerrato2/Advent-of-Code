import sys

if __name__ == '__main__':

    if len(sys.argv) != 2:
        sys.exit("Error: Faltan argumentos")
    
    file_in = open(sys.argv[1], 'r')
    if file_in is None:
        sys.exit("Error: Apertura de fichero fallida")
  
    vowels = ['a','e','i','o','u']
    not_allowed_pairs = ['ab', 'cd', 'pq', 'xy']
    correct_words = 0

    word = file_in.readline()
    while word != '':
        num_vowels = 0
        double_letter = False
        incorrect_word = False
        for i in range(len(word)):
            if word[i] in vowels:
                num_vowels += 1
            if i < len(word) - 2:
                if double_letter == False and word[i] == word[i+1]:
                    double_letter = True
                if word[i:i+2] in not_allowed_pairs:
                    incorrect_word = True
                    break

        if incorrect_word == False and num_vowels >= 3 and double_letter == True:
            correct_words += 1

        word = file_in.readline()

    print("Palabras correctas: " + str(correct_words))
