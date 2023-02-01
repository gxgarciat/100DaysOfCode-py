import random
# Step 1

word_list = ["aardvark", "baboon", "camel"]

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
print(chosen_word)

userSelection = input("Guess a letter: ")
userSelection = userSelection.lower()

userGuess = chosen_word.count(userSelection)
print(userGuess,hangmanpics[0],hangmanpics[4])

# if __name__ == '__main__':
#     main()