import random
# Remember to use the random module
# Hint: Remember to import the random module here at the top of the file. 🎲

# You are going to write a virtual coin toss program.
# It will randomly tell the user "Heads" or "Tails".
# Important, the first letter should be capitalised and
# spelt exactly like in the example e.g. Heads, not heads.

# Write the rest of your code below this line 👇
coinResult = random.randint(0, 1)

if coinResult == 0:
    print("Tails")
else:
    print("Heads")

# if __name__ == '__main__':
#     main()