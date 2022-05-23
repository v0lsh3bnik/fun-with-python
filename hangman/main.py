# v0l5h3bn1k ~ https://github.com/v0lsh3bnik/fun-with-python

# TODO : bug when guess does not match if at line 51
# TODO : add options to game (replay, exit)

import random

words = ['food', 'goat', 'love', 'death', 'child']
success_phrases = ['Well done!', 'Oh, you\'re good at this game', 'Bravo!']
error_phrases = ['No, no and no!', 'Oh, you\'re bad at this game', 'This is wrong!', 'Can you do better?',
                 'You lost sorry', 'Incorrect guess']

delimiter = '*' * 17


def main():
    global count
    global tries
    global word
    global len_word
    global guess
    global guessed
    global masked_word
    global display_word
    global final_word
    global isGuessed

    lunch_game()


def play_game_loop():
    pass


def lunch_game():
    word = random.choice(words)
    tries = 5
    len_word = len(word)
    guess = ''
    guessed = []
    masked_word = '_' * len_word
    display_word = ['_' for w in word]
    final_word = ''
    print('Welcome to the HANGMAN GAMES')
    print(f'[+] The word is a {len_word} letters long : {masked_word}. You have {tries} chances ')

    while tries > 0:

        guess = input('Please enter a letter: ').lower().strip()

        if len(guess) > 1 or len(guess) == 0:
            print(f'[-] Invalid entry')
            lunch_game()

        if guess in guessed:
            print(f'[+] You already said the letter : "{guess}", please try another letter.')
            tries -= 1
            print(tries)
        elif guess in word:
            guessed.append(guess)
            for index, letter in enumerate(word):
                if letter == guess:
                    display_word[index] = letter
            final_word = "".join(display_word)
            if final_word == word:
                print(delimiter)
                print(f'[+] {random.choice(success_phrases)}, the word is {word.upper()}')
                print(delimiter)
                break
            else:
                print(f'[+] {random.choice(success_phrases)}, {final_word}')
        elif len(guessed) == len(word):
            print(f'[+] EUREKA, the word is : {word}')
        else:
            print(f'[-] {random.choice(error_phrases)}, {guess} is not in the word.')
            tries -= 1
    else:
        print(delimiter)
        print(f'{random.choice(error_phrases)} The word was "{word}".')
        print(delimiter)


main()
