## Problem statement ##
# Given a list of student scores: [85, 92, 45, 67, 73, 55, 98].
# Iterate through the list and print the grade for each score based on the following criteria:
# 90 and above: "Grade A"
# 80 to 89: "Grade B"
# 70 to 79: "Grade C"
# 60 to 69: "Grade D"
# Below 60: "Fail"
## Implement from below ##

scores= [85, 92, 45, 67, 73, 55, 98]

for i in scores:
    if i >= 90:
        print("Grade A")
    elif i in range(80,90):
        print("Grade B")
    elif i in range(70,80):
        print("Grade C")
    elif i in range(60,70):
        print("Grade D")
    else:
        print("Fail")
    