import sys
import time
from english_words import get_english_words_set
import random


def get_all_words():
    allwords = get_english_words_set(['web2'], alpha=True)
    words = [w.upper() for w in allwords if len(w) == 5]
    return words


def get_hidden_word():
    words = get_all_words()
    return random.choice(words)


def slow_print(blocks):
    to_print = ''
    for block in blocks:
        to_print += block
        sys.stdout.write(f'\r{to_print}')
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write('\n')


def check_word(hidden_word):
    allwords = get_all_words()
    attempt = 6
    while attempt > 0:
        guess = input("Guess: ").upper()
        if guess not in allwords or len(guess) != 5:
            print("INVALID GUESS MORON!")
        elif guess == hidden_word:
            print(f"You got it in {attempt} tries!")
            slow_print('🟩🟩🟩🟩🟩')
            break
        else:
            attempt -= 1
            blocks = ""
            for char, word in zip(hidden_word, guess):
                if word in hidden_word and word in char:
                    blocks += "🟩"
                    # print(word + " 🟩 ")
                elif word in hidden_word:
                    blocks += "🟨"
                    # print(word + " 🟨 ")
                else:
                    blocks += "⬛"
                    # print(word + " ⬛ ")
            slow_print(blocks)
    if attempt <= 0:
        print("YOU DIED!")
        print(f"The correct word was: {hidden_word}")


werd = get_hidden_word()
check_word(werd)
