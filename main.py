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

def check_valid_input(letter_guessed, old_letters_guessed):
    """is_valid_input: check if input is not singl eng letter
    letter_gussed: passed from user input
    type letter_gussed: string
    return: answer if true or false (and printing error num)
    rtype: bool
    """
    if len(letter_guessed) > 1:
        if not letter_guessed.isalpha():
            print("E3")
        else:
            print("E1")
        return False
    elif not letter_guessed.isalpha():
        print("E2")
        return False
    else:
        if letter_guessed not in old_letters_guessed:
            print("your letter is:", letter_guessed.lower())
            old_letters_guessed.append(letter_guessed)
            return True
        else:
            print("E4")
            return False

def main():
    
    word = input("set a new word: ")
    print("the word is:", word)
    print('_ ' * len(word))
    
    old_letters_guessed = []
    letter = input("Let's geuss some letter: ")
    print(check_valid_input(letter, old_letters_guessed))
    print(check_valid_input(letter, old_letters_guessed)) #just checking!! - work!@# perfectly @!#!#@!$
    
if __name__ == "__main__":
    main()
