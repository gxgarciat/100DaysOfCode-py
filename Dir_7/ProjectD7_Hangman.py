import random
# Step 1

word_list = ["aardvark", "baboon", "camel"]
alphabet = 'abcdefghijklmnopqrstuvwxyz'

hangmanpics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
# Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

chosen_word = word_list[random.randint(0,len(word_list))-1]

print("***",chosen_word)

wordToGuess = "_"

for i in range(0,len(chosen_word)):
    wordToGuess = wordToGuess + "_"

print(f"Your word contains {len(chosen_word)} letters in total:")
print()
print(wordToGuess)
print()

i = 0 # To count mistakes
attemptsLeft = 7
shownWord = ""
guessedLetters = ""

while attemptsLeft != 0: #in range(0,len(hangmanpics)):
    userSelection = input("Guess a letter: ")
    userSelection = userSelection.lower()

    while alphabet.count(userSelection) == 0:
        print("You already tried that letter before.")
        userSelection = input("Guess a letter: ")

    alphabet = alphabet.replace(userSelection,'')

    userGuess = chosen_word.count(userSelection)
    if userGuess == 0:
        attemptsLeft = attemptsLeft - 1
        print(f"You have {attemptsLeft} mistakes left.")
        print(hangmanpics[-attemptsLeft-1])

        if attemptsLeft == 0:
            print("Game over.")
    else:
        guessedLetters = guessedLetters + userSelection
        print(guessedLetters)

        for letter in chosen_word:
            if letter != userSelection:
                shownWord = shownWord + "_"
            else:
                shownWord = shownWord + letter
        for letter in guessedLetters:
            if letter != userSelection:
                print("Here")
            else:
                i = i + 1
                if i == len(chosen_word):
                    print("there",i)
                    # while True:
                        # break()
                while False:
                     # if i == len(chosen_word):
                         # break
        print(shownWord)
        shownWord = ""

# if __name__ == '__main__':
#     main()