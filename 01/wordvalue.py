from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open('./dictionary.txt') as fh:
        words = [ line.strip() for line in fh]
    return words

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    val = 0
    for char in word.upper():
        if char in LETTER_SCORES:
            val += LETTER_SCORES[char]
    return val

def max_word_value(*argv):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if len(argv)==0:
        words = load_words()
    else:
        words = argv[0]

    max_score = -1
    max_score_word = ''
    for word in words:
        val = calc_word_value(word)
        if val > max_score:
            max_score = val
            max_score_word = word
    return max_score_word


if __name__ == "__main__":
    # TEST_WORDS = ('bob','julian')
    # max_word_value(TEST_WORDS)

    word1 = 'benzalphenylhydrazone'
    word2 = 'Zyzzogeton'

    print(f"{word1}:{calc_word_value(word1)}")
    print(f"{word2}:{calc_word_value(word2)}")
