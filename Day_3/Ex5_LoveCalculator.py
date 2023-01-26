# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆


# For Love Scores less than 10 or greater than 90, the message should be:
# "Your score is **x**, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:
# "Your score is **y**, you are alright together."
# Otherwise, the message will just be their score. e.g.:
# "Your score is **z**."


# Write your code below this line 👇

lowerName1 = name1.lower()
lowerName2 = name2.lower()

couplesName = (lowerName1+lowerName2).replace(" ", "")

dozen = couplesName.count('t') + couplesName.count('r') + couplesName.count('u') + couplesName.count('e')
unit = couplesName.count('l') + couplesName.count('o') + couplesName.count('v') + couplesName.count('e')

score = dozen*10 + unit

if (score < 10) or (score > 90):
    results = ", you go together like coke and mentos."
elif (score < 50) and (score > 40):
    results = ", you are alright together."
else:
    results = "."
print(f"Your score is {score}{results}")

# if __name__ == '__main__':
#     main()