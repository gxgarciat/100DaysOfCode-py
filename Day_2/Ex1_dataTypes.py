# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

# Write a program that adds the digits in a 2 digit number
# e.g. if the input was 35, then the output should be 3 + 5 = 8

####################################
#Write your code below this line 👇


# Option 1 - by using subscripting & type casting
doz = int(two_digit_number[0])
unit = int(two_digit_number[1])

print(doz+unit)

two_digit_number = int(two_digit_number)

# Option 2 - by using modulo & type casting
doz = int(two_digit_number / 10)
unit = two_digit_number % 10

print(doz+unit)

# if __name__ == '__main__':
#     main()