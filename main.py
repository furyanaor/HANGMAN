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

MAX_TRIES = 7
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
    """print_hangman: just printing the correct img by number of tries index
    :param num_of_tries: passed number of bad guesses while trying failed
    :type: int
    """
    print(HANGMAN_PHOTOS[num_of_tries])


def wrong_input_printer(old_letters_guessed):
    """wrong_input_printer: printing the guessed letters list when wrong guess
    :param old_letters_guessed: list of strings that collect all the old guesses
    :type: list
    """
    old_letters_guessed.sort()
    print("X")
    result = " -> ".join(old_letters_guessed)
    print(result)


def check_valid_input(letter_guessed):
    """is_valid_input: check if input is a single english letter
    :param letter_guessed: passed from user input
    :type: str
    :return: answer if true or false (and printing the error number)
    :rtype: bool
    """
    if len(letter_guessed) > 1:
        if letter_guessed.isalpha():
            print("E1, too many letters..")
        else:
            print("E3, char?? and so many ?!")
        return False
    elif not letter_guessed.isalpha():
        print("E2, only english letters please...")
        return False
    return True


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """try_update_letter_guessed: check if letter is fine return true
    (or false with printing of the correct guessed)
    and add it to the old guessed list
    :param letter_guessed: passed from user input
    :type: str
    :param old_letters_guessed: list of strings that collect all the old guesses
    :type: list
    :return: answer if true or false (and printing the error number)
    :rtype: bool
    """
    if check_valid_input(letter_guessed):
        if letter_guessed not in old_letters_guessed:
            print("your letter is:", letter_guessed.lower())
            old_letters_guessed.append(letter_guessed.lower())
            return True
        else:
            print("E4, already guessed that letter, try another one!")
    wrong_input_printer(old_letters_guessed)
    return False


def show_hidden_word(secret_word, old_letters_guessed):
    """show_hidden_word: printing the hidden word
    with the correct guessed letters
    :param secret_word: passed from main to compare with the current guess
    :type: str
    :param old_letters_guessed: list of strings that collect all the old guesses
    :type: list
    """
    for i in range(len(secret_word)):
        if secret_word[i].lower() in old_letters_guessed:
            print(secret_word[i].lower(), end=" ")
        else:
            print("_", end=" ")
    print("")


def check_win(secret_word, old_letters_guessed):
    """check_win: check if any letter on the secret word
    is all ready guessed so return true
    :param secret_word: passed from main to compare with the current guess
    :type: str
    :param old_letters_guessed: list of strings that collect all the old guesses
    :type: list
    :return: true if secret word exposed, else - return false
    :rtype: bool
    """
    for i in secret_word:
        if i not in old_letters_guessed:
            return False
    return True


def choose_word(file_path, index):
    """choose_word: pick a word from file by index
    :param file_path: passed from user input
    :type: str
    :param index: passed from user input
    :type: int
    :return: the number of words with no duplicate
    and the chosen word string by index
    :rtype: tuple
    """
    words_file = open(file_path, "r")
    words_list = words_file.readline().split(" ")
    words_list_filtered = []
    for word in words_list:
        if word not in words_list_filtered:
            words_list_filtered.append(word)
    result = (len(words_list_filtered), words_list[index % len(words_list)-1])
    return result


def main():
    secret_word_path = r"c:\t1.txt"
    secret_word_index = int(input("please choose word 1-14: "))
    secret_word = choose_word(secret_word_path, secret_word_index)
    secret_word = secret_word[1]

    old_letters_guessed = []
    show_hidden_word(secret_word, old_letters_guessed)

    guess_number = 0

    while not check_win(secret_word, old_letters_guessed) and MAX_TRIES > guess_number:
        letter = input("Let's guess some letter: ")
        if try_update_letter_guessed(letter, old_letters_guessed):
            if letter in secret_word:
                show_hidden_word(secret_word, old_letters_guessed)
            else:
                guess_number += 1
                print_hangman(guess_number)

    if MAX_TRIES > guess_number:
        print("~Win!~")
    else:
        print("~Loss -_- ...~")
    print("****end!!!")


if __name__ == "__main__":
    main()
