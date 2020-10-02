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
print("thק word is:", word)
print('_ ' * len(word))

letter = input("Let's geuss some letter: ")
print("your letter is:", letter.lower())
