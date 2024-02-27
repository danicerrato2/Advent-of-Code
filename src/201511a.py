import sys
import string

alphabet = list(string.ascii_lowercase)

def next_password(password):
    if len(password) == 1:
        if password[0] == 'z':
            return ""
        return 

    password = list(password)
    if password[-1] == 'z':
        password = next_password(password[:-1]) + 'a'
    else:
        alpha_index = alphabet.index(password[-1])
        password[-1] = alphabet[alpha_index+1]
    password = ''.join(password)
    return password

if __name__ == '__main__':

    if len(sys.argv) != 2:
        sys.exit("Error: Faltan argumentos")
    
    file_in = open(sys.argv[1], 'r')
    if file_in is None:
        sys.exit("Error: Apertura de fichero fallida")

    is_correct = False
    password = file_in.read()[:-1]
    while is_correct != True:
        password = next_password(password)
        if password == "":
            sys.exit("Password limit reached")
        i = 0
        pair_counter = 0
        pair_flag = False
        while i < len(password) - 2:
            if password[i] == 'i' or password[i] == 'l' or password[i] == 'o':
                is_correct = False
                break
            alpha_index = alphabet.index(password[i])
            if alpha_index < len(alphabet)-2:
                if password[i+1] == alphabet[alpha_index+1] and password[i+2] == alphabet[alpha_index+2]:
                    if password[i] == 'g' or password[i] == 'j' or password[i] == 'm':
                        is_correct = False
                        break
                    is_correct = True
            if pair_flag == False and pair_counter < 2 and password[i] == password[i+1]:
                pair_counter += 1
                pair_flag = True
            elif pair_flag == True:
                pair_flag = False
            i += 1
        if pair_counter < 2 and password[-2] == password[-1]:
            if password[-2] != password[-3] or password[-3] == password[-4]:
                pair_counter += 1 
        
        if is_correct == True and pair_counter < 2:
            is_correct = False

    print(password)
