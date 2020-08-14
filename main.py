import ps3_hangman
from ps3_hangman import isWordGuessed, getGuessedWord, getAvailableLetters


def main():
    ps3_hangman.loadWords()
#
# print(isWordGuessed("test", ["t", "e", "t", "s"]))  # True
# print(isWordGuessed("test", ["t", "b", "t", "s"]))  # False
# print(getGuessedWord('apple', ['e', 'i', 'k', 'p', 'r', 's']))  # '_ pp_ e'
# print(getAvailableLetters(['e', 'i', 'k', 'p', 'r', 's']))  # abcdfghjlmnoqtuvwxyz
