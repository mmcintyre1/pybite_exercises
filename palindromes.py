"""A palindrome is a word, phrase, number, or other sequence of characters
which reads the same backward as forward"""
import os
import urllib.request

tmp = os.getenv("TMP", "/tmp")
DICTIONARY = os.path.join(tmp, 'dictionary_m_words.txt')
urllib.request.urlretrieve('http://bit.ly/2Cbj6zn', DICTIONARY)


def load_dictionary():
    """Load dictionary (sample) and return as generator (done)"""
    with open(DICTIONARY) as f:
        return (word.lower().strip() for word in f.readlines())


def is_palindrome(word):
    """

    :param word:
    :return:
    """
    normalized_word = [letter.lower() for letter in word if letter.isalnum()]
    return normalized_word == normalized_word[::-1]


def get_longest_palindrome(words=None):
    """Given a list of words return the longest palindrome
       If called without argument use the load_dictionary helper
       to populate the words list"""
    if words is None:
        words = load_dictionary()

    palindromes = [word for word in words if is_palindrome(word)]
    print()

    return max(palindromes, key=len)


if __name__ == '__main__':
    words = load_dictionary()
    new_longest = 'A car, a man, a maraca.'
    words = list(words) + [new_longest]
    print(words[-1])
    print(get_longest_palindrome(words))
