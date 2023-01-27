# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆
# You are going to write a program that will mark a spot with an X.
# In the starting code, you will find a variable called map.
# This map contains a nested list. When map is printed this is what the nested list looks like:
# [['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]

# Write your code below this row 👇

vertical = int(position) % 10
horizontal = int(position) // 10

# Approach #1
# if units == 1:
#     row1[dozen-1] = 'X'
# elif units == 2:
#     row2[dozen-1] = 'X'
# else:
#     row3[dozen-1] = 'X'

# Approach #2
#map[vertical-1][horizontal-1] = "X"

# Approach #3
# horizontal = int(position[0])
# vertical = int(position[1])
selected_row = map[vertical-1]
selected_row[horizontal-1] = "X"

# Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

# if __name__ == '__main__':
#     main()