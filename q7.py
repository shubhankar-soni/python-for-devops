# Given a list of passwords:
# passwords = ["apple", "Secure123", "TOOLONGPASSWORD1", "short1", "NoNumbersHere"]
# Iterate through the list and categorize each password based on these strict rules:

# Strong: Must be between 8 and 15 characters long (inclusive) AND contain at least one number. (Hint: You might need to use a nested loop or the any() function combined with .isdigit() to check for numbers).
# Weak: Contains a number but is less than 8 characters long.
# Invalid: Is longer than 15 characters OR contains no numbers at all.
## Start Implementation below:

passwords = ["apple", "Secure123", "TOOLONGPASSWORD1", "short1", "NoNumbersHere"]

for pwd in passwords:
    has_number = False

    for char in pwd:
        if char.isdigit():
            has_number = True
            break

    if 8 <= len(pwd) <=15 and has_number:
        print(f"Strong password")

    elif len(pwd)< 8 and has_number:
        print("Weak")
    
    elif len(pwd) > 15 or not has_number:
        print("Invalid")
        

