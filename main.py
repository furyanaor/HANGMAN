HANGMAN_ASCII_ART = """ \\
    _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_  \\
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |
                       |___/         by: furyanaor.
"""

MAX_TRIES = 8
print(HANGMAN_ASCII_ART)

HANGMAN_PHOTOS = {
    1: """
    x-------x
    
    
    
    
    
    """,
    2: """
    x-------x
    |
    |
    |
    |
    |
    """,
    3: """
    x-------x
    |       |
    |       0
    |
    |
    |
    """,
    4: """
    x-------x
    |       |
    |       0
    |       |
    |
    |
    """,
    5: """
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |
    """,
    6: """
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
    """,
    7: """
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |
    """
}


def print_hangman(num_of_tries):
    print(HANGMAN_PHOTOS[num_of_tries])


def wrong_input_printer(old_letters_guessed):
    old_letters_guessed.sort()
    print("X")
    result = " -> ".join(old_letters_guessed)
    print(result)


def check_valid_input(letter_guessed, old_letters_guessed):
    """is_valid_input: check if input is not single eng letter
    letter_guessed: passed from user input
    type letter_guessed: string
    return: answer if true or false (and printing error num)
    rtype: bool
    """
    if len(letter_guessed) > 1:
        if not letter_guessed.isalpha():
            print("E3")
            # char?? and so many ?!
        else:
            print("E1")
            # too many letters..
        wrong_input_printer(old_letters_guessed)
        return False
    elif not letter_guessed.isalpha():
        print("E2")
        # only english letters please...
        wrong_input_printer(old_letters_guessed)
        return False
    else:
        if letter_guessed not in old_letters_guessed:
            print("your letter is:", letter_guessed.lower())
            old_letters_guessed.append(letter_guessed.lower())
            return True
        else:
            print("E4")
            # already guessed that letter, try another one!
            wrong_input_printer(old_letters_guessed)
            return False


def show_hidden_word(secret_word, old_letters_guessed):
    for i in range(len(secret_word)):
        if secret_word[i].lower() in old_letters_guessed:
            print(secret_word[i].lower(), end=" ")
        else:
            print("_", end=" ")
    print("")


def check_win(secret_word, old_letters_guessed):
    for i in secret_word:
        if i not in old_letters_guessed:
            return False
    return True


def main():

    secret_word = input("set a new word: ")
    print("the word is: ", secret_word)
    print('_ ' * len(secret_word))

    old_letters_guessed = []
    guess_number = 0

    while not check_win(secret_word, old_letters_guessed) and MAX_TRIES > guess_number:
        letter = input("Let's guess some letter: ")
        print("input letter is: ", letter)
        if check_valid_input(letter, old_letters_guessed):
            show_hidden_word(secret_word, old_letters_guessed)
            # supposed to check before it if the letter on word or not!
            guess_number += 1
            print_hangman(guess_number)

    print("****end!!!")


if __name__ == "__main__":
    main()
