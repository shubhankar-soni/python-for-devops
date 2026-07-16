# # Given a list of numbers from 1 to 20: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20].
# Iterate through the list and print:
# "Fizz" if the number is divisible by 3.
# "Buzz" if the number is divisible by 4.
# "FizzBuzz" if the number is divisible by BOTH 3 and 4 (e.g., 12).
# The number itself if it is divisible by neither.
## Implement from below: ##

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for i in my_list:
    if i % 3 == 0 and i % 4 == 0:
        print("FizzBuzz")    
    elif i % 3 == 0 :
        print("Fizz")
    elif i % 4 == 0 :
        print("Buzz")
    else:
        print(i)

