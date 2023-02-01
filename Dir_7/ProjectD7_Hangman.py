import random
# Step 1

word_list = ["aardvark", "baboon", "camel"]

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
# Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

chosen_word = word_list[random.randint(0,len(word_list))-1]
print(chosen_word)

userSelection = input("Guess a letter: ")
userSelection = userSelection.lower()

mistakes = chosen_word.count(userSelection)
print(mistakes)

# if __name__ == '__main__':
#     main()