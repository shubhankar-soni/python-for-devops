import re

# text = "The quick brown fox"
# pattern = r"brown"

# search = re.search(pattern, text)
# if search:
#     print("Pattern found:", search.group())
# else:
#     print("Pattern not found")

new_text = "My name is brown and my favorite color is brown too."
newpattern = r"brown"

searchnew = re.search(newpattern, new_text)
if searchnew:
    print("I found it!!!",searchnew.group(0))
else:
    print("Noooo")