import re

bio = "My Name is Shubhankar Soni, and I am SE, and my fave color is red, and i live in india"
bionew = bio.strip()
splitstr= r","

strresult = re.split(splitstr, bionew)
print(strresult)