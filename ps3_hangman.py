# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open('C:/Users/pinlacj/Documents/6.00.1x Files/words.txt', 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    check=False
    check2=False
    for letter in secretWord:
        check2=False
        for char in lettersGuessed:
            if char ==letter:
                check2=True
                break
        if check2==False:
            return False
    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    output=''
    for letter in secretWord:
        check=False
        for char in lettersGuessed:
            if letter==char:
                output+= str(char) + ' '
                check=True
        if check==False:
            output+= '_ '
    return output



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    start = string.ascii_lowercase
    output = ''
    for letter in start:
        check = False
        for char in lettersGuessed:
            if letter == char:
                check = True
        if check == False:
            output += letter
    return output
    
def goodGuess(char, secretWord):
    for letter in secretWord:
        if char==letter:
            return True
    return False
    
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
    lettersGuessed = []
    guesses = 8
    guess=''
    availableLetters = getAvailableLetters(lettersGuessed)
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is ' +str(len(secretWord))+ ' letters long.'
    turn=1
    while guesses!=0:
        print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        print 'You have ' + str(guesses) + ' guesses left.'
        print 'Available letters: ' + str(availableLetters),
        guess =raw_input('Please guess a letter: ').lower()
        if goodGuess(guess, availableLetters)==True:
            lettersGuessed.append(guess)   
            availableLetters = getAvailableLetters(lettersGuessed)  
            if goodGuess(lettersGuessed[turn-1], secretWord)==True:
                print 'Good guess: ' + str(getGuessedWord(secretWord, lettersGuessed))
            else:
                print 'Oops! That letter is not in my word: '+ str(getGuessedWord(secretWord, lettersGuessed))
                guesses-=1
            turn+=1
        elif goodGuess(guess, availableLetters)==False:
            print "Oops! You've already guessed that letter: " + str(getGuessedWord(secretWord, lettersGuessed))
        if isWordGuessed(secretWord, lettersGuessed)==True:
            guesses=0
    if guesses==0 and isWordGuessed(secretWord, lettersGuessed)==True:
        print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        print 'Congratulations, you won!'
    else:
        print '|||||||||||||||||||||||||'
        print 'Sorry, you ran out of guesses. The word was ' + secretWord + '.'
    






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
