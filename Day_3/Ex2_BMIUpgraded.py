# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
# It should tell them the interpretation of their BMI based on the BMI value.
# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.

# Write your code below this line 👇

BMI = round(weight / height**2,1)
print(BMI)
if BMI < 18.5:
    a = "are underweight"
if BMI > 35:
    a = "are clinically obese"
if (BMI > 18.5) and (BMI < 35):
    if BMI < 25:
        a = "have a normal weight"
    else:
        if (BMI > 25) and (BMI < 30):
            a = "are slightly overweight"
        else:
            a = "are obese"

print(f"Your BMI is: {BMI}, you {a}.")

# if __name__ == '__main__':
#     main()