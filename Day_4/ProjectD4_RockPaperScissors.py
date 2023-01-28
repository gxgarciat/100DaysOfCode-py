# Import the random module here
import random

# Implement the game Rock Paper Scissors

# Write your code below this line 👇

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
options = [rock, paper, scissors]

userSelection = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

computerChoice = random.randint(0, 2)
print(f"{options[userSelection]} \n Computer chose: \n {options[computerChoice]}")

if userSelection == computerChoice:
    print("It's a draw.")


# if __name__ == '__main__':
#     main()