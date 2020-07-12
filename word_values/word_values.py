import os
import urllib.request

TMP = os.getenv("TMP", "/tmp")
S3 = 'https://bites-data.s3.us-east-2.amazonaws.com/'
DICT = 'dictionary.txt'
DICTIONARY = os.path.join(TMP, DICT)
urllib.request.urlretrieve(f'{S3}{DICT}', DICTIONARY)

scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                 for letter in letters.split()}


def load_words():
    """Load the words dictionary (DICTIONARY constant) into a list and return it"""
    with open(DICTIONARY, 'r') as file_in:
        return [word.strip() for word in file_in.read().split() if word.strip()]


def calc_word_value(word):
    """Given a word calculate its value using the LETTER_SCORES dict"""
    score = 0
    for letter in word:
        for score_group in scrabble_scores:
            if letter.upper() in score_group[1].split(' '):
                score += score_group[0]

    return score


def max_word_value(words):
    """Given a list of words calculate the word with the maximum value and return it"""
    return max([(calc_word_value(word), word) for word in words])[1]


if __name__ == '__main__':
    words = load_words()
    assert calc_word_value('h') == 4
    print(max_word_value(words))


