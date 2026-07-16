# Given a list of ages: [12, 17, 25, 42, 8, 65, 19].
# Categorize them and print the output in the exact format below using if...elif...else statements:
# Children (0-12): [8, 12]
# Teens (13-19): [17, 19]
# Adults (20-59): [25, 42]
# Seniors (60+): [65]
## Implement from below line: ##


ages = [12, 17, 25, 42, 8, 65, 19]

child = []
teen = []
adult = []
seniors = []

for i in ages:
    if i in range(0,13):
        child.append(i)
    elif i in range(13,20):
        teen.append(i)
    elif i in range(20,60):
        adult.append(i)
    else: 
        seniors.append(i)

print("Children (0-12): ", sorted(child))
print("Teens (13-19): ", sorted(teen))
print("Adults (20-59): ", sorted(adult))
print("Seniors (60+): ", sorted(seniors))