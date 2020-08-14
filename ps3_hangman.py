# Hangman game
import random
import string

WORDLIST_FILENAME = "words.txt"

# helper code
# -----------------------------------
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters. Depending on the size of the word list, this function may take a while to finish.
    """
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings). Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code
# -----------------------------------
# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    """
    letters_guessed = []

    for letter in secretWord:
        if letter in lettersGuessed:
            letters_guessed.append(letter)
        else:
            return False
    return len(lettersGuessed) != 0


def getGuessedWord(secretWord, lettersGuessed):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    """
    word_guessed = []

    for letter in secretWord:
        if letter in lettersGuessed:
            word_guessed.append(letter)
        else:
            word_guessed.append("_")

    return ' '.join(word_guessed)


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    available_letters = list(string.ascii_lowercase)
    for letter in lettersGuessed:
        available_letters.remove(letter)
    return ''.join(available_letters)


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    guesses = 8
    letters_guessed = []
    is_game_over = False

    print("Welcome to the game, Hangman!")
    print("I'm thinking of a word" + " " + str(len(secretWord)) + " " + "letters long")

    while not is_game_over:
        print("You have " + str(guesses) + " guesses left")
        guesses -= 1
        print("Available letters: " + getAvailableLetters(letters_guessed))
        guess = input("Please guess a letter: ")

        if guess in secretWord:
            letters_guessed.append(guess)
            print("Good guess: " + getGuessedWord(secretWord, letters_guessed))
        else:
            print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, letters_guessed))

        if isWordGuessed(secretWord, letters_guessed):
            print("Congratulations. You won")
            is_game_over = True
        elif guesses == 0:
            print("Sorry, you ran out of guesses. The word was " + secretWord)
            is_game_over = True



secret_word = chooseWord(wordlist).lower()
hangman(secret_word)
