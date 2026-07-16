# -	Create a file sample1.txt in your local with the below content:
# Apple
#  Banana
# Apple
#  Orange
# Banana
# Apple

# 1.	Print the total content of the file.
# 2.	Print each line by removing extra spaces at the beginning and ending of the line
# 3.	Print the number of lines in the file.
# 4.	Print the number of times each fruit appears in the file, as shown below:
# Apple -> 3
# Banana -> 2
# Orange -> 1

# with open("sample1.txt", "r") as file:
#     print(file.read())


# with open("sample1.txt", "r") as file:
#     for fruit in file:
#         print(fruit.strip())


# nu_of_lines = 0
# with open("sample1.txt", "r") as file:
#     for line in file:
#         nu_of_lines = nu_of_lines + 1

# print(nu_of_lines)


fruit_count = {}
with open("sample1.txt", "r") as file:
    for line in file:
       fruit = line.strip()
       if fruit != "":
            if fruit in fruit_count:
                fruit_count[fruit] = fruit_count[fruit] + 1
                print(fruit_count[fruit])
            else:
                fruit_count[fruit] = 1

print(fruit_count) 