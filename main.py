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

def main():
    wellcome()
    
    word = input("set a new word: ")
    print("the word is: ", word)
    print('_ ' * len(word))
    
    old_letters_guessed = ["c", "r", "a"] # *must to be empty!
    letter = input("Let's geuss some letter: ")
    print("input letter is: ", letter)
    print(check_valid_input(letter, old_letters_guessed))
    print(check_valid_input(letter, old_letters_guessed)) #just checking!! - work!@# perfectly @!#!#@!$
    
if __name__ == "__main__":
    main()
