#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

from data import DICTIONARY, LETTER_SCORES, POUCH
import random
from collections import Counter
from itertools import permutations


NUM_LETTERS = 7

# re-use from challenge 01
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# re-use from challenge 01
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


def permuation_of_letters(letters):
    possible_words = list()
    for i in range(len(letters)):
        possible_words.extend(list(permutations(letters,i+1)))
    return possible_words

def find_max_score(letters):
    possible_words = permuation_of_letters(letters)

    best_score = 0
    best_word  = ''
    for chars in possible_words:
        word = ''.join(chars)
        if word.lower() in DICTIONARY:
            word_score = calc_word_value(word)
            if word_score > best_score:
                best_score = word_score
                best_word  = word
    return best_score, best_word



def validate_input(word, letters):

    if word.lower() not in DICTIONARY:
        return False

    cnt_words = Counter()
    cnt_letters = Counter()

    for letter in word:
        cnt_words[letter] += 1

    for letter in letters:
        cnt_letters[letter] += 1

    for letter in cnt_words:
        if letter not in cnt_letters or  cnt_words[letter] > cnt_letters[letter]:
            return False

    return True

def main():
    letters = [random.choice(POUCH) for i in range(0,7)]
    print(letters)

    while(True):
        user_word = input()

        if validate_input(user_word, letters):
            print(f'your score:{calc_word_value(user_word)}')
            best_score, best_word = find_max_score(letters)
            print(f'best score:{best_score} for {best_word}')
            return




if __name__ == "__main__":
    main()
