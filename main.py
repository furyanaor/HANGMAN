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

print("Let's geuss some letter: ")
letter = input()
print("your letter is: ", letter)
# num = int(input())
# print("num is:", num)
# blocks = 0
# for i in range(3):
#     blocks += num % 10
#     num //= 10
# print(blocks)
# block_per_pig = int(blocks / 3)
# print(block_per_pig)
# print(blocks % 3)
# print(not bool(blocks % 3))
