HANGMAN_ASCII_ART = """\\   _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \\
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |
                       |___/
"""

MAX_TRIES = 6
print(HANGMAN_ASCII_ART)

word = input("set a new word: ")
print("the word is:", word)
print('_ ' * len(word))

letter = input("Let's geuss some letter: ")
if len(letter) > 1:
    if not letter.isalpha():
        print("E3")
    else:
        print("E1")
elif not letter.isalpha():
    print("E2")    
else:
    print("your letter is:", letter.lower())
