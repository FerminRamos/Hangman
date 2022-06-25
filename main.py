# Hangman Python Project
import time


def validateInput(location, inputVal):
    alphabet = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                'y', 'z'}

    if location == "menuOpt":
        if inputVal == 'l' or inputVal == 'w' or inputVal == 'a':
            return True
        else:
            return False
    elif location == "letter":
        for letter in alphabet:
            if inputVal == letter:
                return True
        return False
    elif location == "word" or location == "startWord":
        if len(inputVal) < 1:
            return False
        for char in inputVal:
            hasValidChar = False
            for letter in alphabet:
                if letter == char:
                    hasValidChar = True
                    break
            if not hasValidChar:
                return False
        return True
    else:
        return "<<input option cannot be validated>>"


def initializeProgressWord(length):
    word = []
    i = 0
    while i < length:
        word.append("_")
        i += 1
    return " ".join(word)


def updateEncodedWord(letter, encodedWord, correctWord):
    encodedWord = encodedWord.split(" ")

    i = 0
    wordSize = len(correctWord)
    while i < wordSize:
        if encodedWord[i] == "_" and correctWord[i] == letter:
            encodedWord[i] = letter
        i += 1
    return " ".join(encodedWord)


def solvedWord(encodedWord, correctWord):
    encodedWord = "".join(encodedWord.split())  # Removes spaces between letters
    if encodedWord == correctWord:
        return True
    return False


def containsLetter(letter, word):
    for l in word:
        if l == letter:
            return True
    return False


def drawHangman(roundNum, encodedWord):
    print("\n\n\n")
    if roundNum == 0:
        print("--------")
        print("|      |")
        print("|")
        print("|")
        print("|")
        print("---")
    elif roundNum == 1:
        print("--------")
        print("|      |")
        print("|      O")
        print("|")
        print("|")
        print("---")
    elif roundNum == 2:
        print("--------")
        print("|      |")
        print("|      O")
        print("|      |")
        print("|")
        print("---")
    elif roundNum == 3:
        print("--------")
        print("|      |")
        print("|      O")
        print("|     /|")
        print("|")
        print("---")
    elif roundNum == 4:
        print("--------")
        print("|      |")
        print("|      O")
        print("|     /|\\")
        print("|")
        print("---")
    elif roundNum == 5:
        print("--------")
        print("|      |")
        print("|      O")
        print("|     /|\\")
        print("|     /")
        print("---")
    else:
        print("--------")
        print("|      |")
        print("|      O")
        print("|     /|\\")
        print("|     / \\")
        print("---")
    print("    " + encodedWord)


correctWord = input("Enter Guessing Word: ")
validInput = validateInput("startWord", correctWord)
while not validInput:  # Infinite Loop, until valid input
    print("Contains Invalid Char! - Enter New Word.")
    correctWord = input("Enter Guessing Word: ")
    validInput = validateInput("startWord", correctWord)
encodedWord = initializeProgressWord(len(correctWord))

remainingLetters = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                    'y', 'z'}

SLEEP_CONSTANT = 2
hasCompletedWord = False
totalAttempts = 6
attemptNum = 0

while attemptNum < totalAttempts and not hasCompletedWord:
    drawHangman(attemptNum, encodedWord)  # Draw initial board
    guessOpt = input("[l] Guess Letter      [w] Guess Word      [a] Alphabet\n")

    validInput = validateInput("menuOpt", guessOpt)
    while not validInput:  # Infinite Loop, until valid input
        print("Invalid Option! - Guess again.")
        guessOpt = input("[l] Guess Letter      [w] Guess Word      [a] Alphabet\n")
        validInput = validateInput("menuOpt", guessOpt)

    if guessOpt != 'a':
        if guessOpt == 'l':  # Letter Guess
            guess = input(" >> Letter: ")
            validInput = validateInput("letter", guess)

            while not validInput:  # Infinite Loop, until valid input
                print("  Invalid Character - Try Again.")
                guess = input(" >> Letter: ")
                validInput = validateInput("letter", guess)

            letterFound = False
            for letter in remainingLetters:
                if guess == letter and containsLetter(letter, correctWord):
                    remainingLetters.remove(letter)
                    encodedWord = updateEncodedWord(letter, encodedWord, correctWord)
                    letterFound = True
                    print("Correct!")
                    time.sleep(SLEEP_CONSTANT)
                    break
            if not letterFound:
                attemptNum += 1
                print("\nWrong Guess!")
                time.sleep(SLEEP_CONSTANT)

        else:  # Word Guess
            guess = input(" >> Word: ")
            validInput = validateInput("word", guess)

            while not validInput:  # Infinite Loop, until valid input
                print("  Word Contains Invalid Character - Try Again.")
                guess = input(" >> Word: ")
                validInput = validateInput("word", guess)

            if guess == correctWord:
                encodedWord = correctWord
                drawHangman(attemptNum, encodedWord)
                print("Correct!")
                time.sleep(SLEEP_CONSTANT)
            else:
                attemptNum += 1
                print("\nWrong Guess!")
                time.sleep(SLEEP_CONSTANT)

        # Check if word is complete
        hasCompletedWord = solvedWord(encodedWord, correctWord)
        if hasCompletedWord:
            drawHangman(attemptNum, encodedWord)
            print("CONGRATUlATIONS!")

        # Check if out of attempts
        if attemptNum == totalAttempts:
            drawHangman(attemptNum, encodedWord)
            print("Sorry out of attempts!")
            print("Correct Word - " + correctWord)

    else:  # Alphabet (no Guess)
        print(remainingLetters)
        time.sleep(3)
