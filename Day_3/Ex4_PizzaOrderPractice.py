# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.
# Based on a user's order, work out their final bill.
# Small Pizza: $15 Medium Pizza: $20 Large Pizza: $25
# Pepperoni for Small Pizza: +$2 Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1

# Write your code below this line 👇

pizzaSmall = 15
pizzaMedium = 20
pizzaLarge = 25
pepperoni = 0
cheeseExtra = 0

if add_pepperoni == 'Y':
    if size == 'S':
        pepperoni = 2
    else:
        pepperoni = 3
if extra_cheese == 'Y':
    cheeseExtra = 1

if size == 'S':
    if add_pepperoni == 'N' and extra_cheese == 'N':
        print(f"Your final bill is:  ${pizzaSmall}")
    else:
        finalBill = pizzaSmall + pepperoni + cheeseExtra
        print(f"Your final bill is: ${finalBill}")
elif size == 'M':
    if add_pepperoni == 'N' and extra_cheese == 'N':
        print(f"Your final bill is: ${pizzaMedium}")
    else:
        finalBill = pizzaMedium + pepperoni + cheeseExtra
        print(f"Your final bill is: ${finalBill}")
else:
    finalBill = pizzaLarge + pepperoni + cheeseExtra
    print(f"Your final bill is: ${finalBill}")

# if __name__ == '__main__':
#     main()