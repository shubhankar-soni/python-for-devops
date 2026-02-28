import re

text = "The quick brown fox"
pattern = r"quac"

# match = re.match(pattern, text)
# if match:
#     print("Match found:", match.group())
# else:
#     print("No match")

search_in_string = re.search(pattern, text)
if search_in_string:
    print("Found out", search_in_string)
else:
    print("Didn't found", search_in_string)