HANGMAN_ASCII_ART ="""\\   _    _
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

print("set a new word:")
word = input()
print("thw word is:", word)
print('_ ' * len(word))

print("Let's geuss some letter: ")
letter = input()
print("your letter is: ", letter.lower())
