import string
from words import choose_word
from images import IMAGES




def is_word_guessed(secret_word, letters_guessed):

    count = 0
    for i in letters_guessed:
        if (i in secret_word):
            count += 1
    if (count == len(secret_word)):
        return True
    return False


def get_guessed_word(secret_word, letters_guessed):

    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    return guessed_word


def get_available_letters(letters_guessed):

    global letters_left
    for i in letters_guessed:
        if (i in letters_left):
            letters_left = letters_left.replace(i, "#")
    return letters_left


def ifValid(check_letter):
    if (check_letter.isalpha() == False or len(check_letter) > 1):
        print("Please try again\n")
        return False
    return True


def hangman(secret_word):

    print("Welcome to Hangman!")
    print("The  word is {} letters long.".format(str(len(secret_word))), end='\n\n')

    letters_guessed = []
    remaining_lives = 8;
    wrong_input_count = 0

    while (remaining_lives > 0):
        available_letters = get_available_letters(letters_guessed)
        print("Available letters: {} ".format(available_letters))
        guess = input("Please guess a letter: ")
        letter = guess.lower()
        if (ifValid(letter) == False):
            continue

        if letter in secret_word:
            letters_guessed.append(letter)
            print("Good guess: {} ".format(get_guessed_word(secret_word, letters_guessed)))
            if is_word_guessed(secret_word, letters_guessed) == True:
                print("\n * * Congratulations, you won! * * ", end='\n\n')
                exit()
        else:
            remaining_lives -= 1
            if (remaining_lives == 0):
                print(IMAGES[wrong_input_count], "\n")
                print("Oops! That letter is not in my word: {} \nRemaining Lives: {}".format(
                    get_guessed_word(secret_word, letters_guessed), remaining_lives))
                print(f"The word was: '{secret_word}'")
                exit();
            print("Oops! Wrong choice: {} \nRemaining Lives: {}".format(
                get_guessed_word(secret_word, letters_guessed), remaining_lives))
            letters_guessed.append(letter)
            print(IMAGES[wrong_input_count], "\n")
            wrong_input_count += 1



secret_word = choose_word()
letters_left = " ".join(string.ascii_lowercase)
hangman(secret_word)