# Given a list of words: ["cat", "elephant", "dog", "giraffe", "ox", "hippopotamus"].
# Iterate through the list and categorize them based on their character count:

# Words with less than 4 characters: Short words

# Words with 4 to 7 characters: Medium words

# Words with more than 7 characters: Long words
# (Challenge: Try to output this as a dictionary or exactly like the format in your second sample!)
## Implement from below line: ##

my_words = ["cat", "elephant", "dog", "giraffe", "ox", "hippopotamus"]

short_words = []
medium_words = []
long_words = []

for i in my_words:
    if len(i) < 4:
        short_words.append(i)
    elif  4 <= len(i) <= 7:
        medium_words.append(i)
    else:
        long_words.append(i)

print("Short words: ", short_words)
print("Medium words: ", medium_words)
print("Long words: ", long_words)

        
