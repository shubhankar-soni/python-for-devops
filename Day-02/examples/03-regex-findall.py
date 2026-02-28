import re

text = "The quick brown fox"
pattern = r"brew"

search = re.search(pattern, text)
if search:
    print("++++++++",search)
    print("Pattern found:", search.group())
else:
    print("++++++++",search)
    print("Pattern not found")
