# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
passGen = []

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
mode = input(f"Would you like the complex version of the password (Y) or (N)?\n")

sizeLetters = len(letters)
sizeNumbers = len(numbers)
sizeSymbols = len(symbols)
sizePassword = nr_numbers + nr_symbols + nr_letters

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
for i in range(0, nr_letters):
    randomPos = random.randint(0, sizeLetters-1)
    passGen.append(letters[randomPos])

for j in range(0, nr_symbols):
    randomPos = random.randint(0, sizeSymbols-1)
    passGen.append(symbols[randomPos])

for k in range(0, nr_numbers):
    randomPos = random.randint(0, sizeNumbers-1)
    passGen.append(numbers[randomPos])

if mode == 'N' or mode == 'n':
    passGen = ''.join(passGen)
else:
    random.shuffle(passGen)
    passGen = ''.join(passGen)
    # i = nr_letters
    # j = nr_symbols
    # k = nr_numbers
    # for l in range(0, sizePassword):
    #     branch = random.randint(0, 2)
    #     print("Branch",branch)
    #     if branch == 0 or i != 0:
    #         randomPos = random.randint(0, sizeLetters - 1)
    #         passGen.append(letters[randomPos])
    #         i = i - 1
    #         print(i)
    #     elif branch == 1 or j != 0:
    #         randomPos = random.randint(0, sizeSymbols - 1)
    #         passGen.append(symbols[randomPos])
    #         j = j - 1
    #         print(j)
    #     elif branch == 2 or k != 0:
    #         randomPos = random.randint(0, sizeNumbers - 1)
    #         passGen.append(numbers[randomPos])
    #         k = k - 1
    #         print(k)


        print(l)


print(passGen)

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# if __name__ == '__main__':
#     main()