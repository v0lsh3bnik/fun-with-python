import random
import time

words = ['food', 'goat', 'love', 'death', 'child']

def main():
    global count
    global tries
    global word
    global len_word
    global guessed
    global isGuessed

    lunch_game()


def play_game_loop():
    pass


def lunch_game():
    word = random.choice(words)
    tries = 5
    len_word = len(word)
    guessed = []
    print('Welcome to the HANGMAN GAMES')
    print(f'[+] The selected word contains {len_word} letters, you have {tries} chances.')

    while tries > 0:
        guess = input('Please enter a letter: ')
        if guess in guessed:
            print(f'[+] You already said the letter : "{guess}", please try another letter.')
            tries -= 1
            print(tries)
        elif guess in word:
            print(f'[+] Correct guess, it contains {word.count(guess), guess} in the word.')
            guessed.append(guess)
        elif len(guessed) == len(word):
            print(f'[+] EUREKA, the word is : {word}')
        else:
            print(f'[-] Incorrect guess, {guess} is not in the word.')
            tries -= 1
            print(tries)
    else:
        print(f'You lost ... sorry! The word was "{word}".')

    print(guessed)
    # print(arr_word)


main()
