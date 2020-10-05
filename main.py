
def wellcome():
    HANGMAN_ASCII_ART = """ \\
        _    _
       | |  | |
       | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
       |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_  \\
       | |  | | (_| | | | | (_| | | | | | | (_| | | | |
       |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                            __/ |
                           |___/
    """
    
    MAX_TRIES = 6
    print(HANGMAN_ASCII_ART)


def worng_input_printer(old_letters_guessed):
    old_letters_guessed.sort()
    print("X")
    result = " -> ".join(old_letters_guessed)
    print(result)


def check_valid_input(letter_guessed, old_letters_guessed):
    """is_valid_input: check if input is not singl eng letter
    letter_gussed: passed from user input
    type letter_gussed: string
    return: answer if true or false (and printing error num)
    rtype: bool
    """
    if len(letter_guessed) > 1:
        if not letter_guessed.isalpha():
            print("E3") #charcters?? and so many ?!
        else:
            print("E1") #too many letters..
        worng_input_printer(old_letters_guessed)
        return False
    elif not letter_guessed.isalpha():
        print("E2") #only english letters please...
        worng_input_printer(old_letters_guessed)
        return False
    else:
        if letter_guessed not in old_letters_guessed:
            print("your letter is:", letter_guessed.lower())
            old_letters_guessed.append(letter_guessed.lower())
            return True
        else:
            print("E4") #allready guessed that letter, try another one!
            worng_input_printer(old_letters_guessed)
            return False


def show_hidden_word(secret_word, old_letters_guessed):
    for i in range(len(secret_word)):
        if secret_word[i].lower() in old_letters_guessed:
            print(secret_word[i].lower(), end =" ")
        else:
            print("_", end =" ")
    print("")



def check_win(secret_word, old_letters_guessed):
    for i in secret_word:
        if i not in old_letters_guessed:
            return False
    return True

def main():
    wellcome()
    
    secret_word = input("set a new word: ")
    print("the word is: ", secret_word)
    print('_ ' * len(secret_word))
    
    old_letters_guessed = ["c", "r", "a"] # *must to be empty!
    while check_win(secret_word, old_letters_guessed) != True:
        letter = input("Let's geuss some letter: ")
        print("input letter is: ", letter)
        if check_valid_input(letter, old_letters_guessed) == True:
            show_hidden_word(secret_word, old_letters_guessed)
    print("****end!!!")
    
if __name__ == "__main__":
    main()
