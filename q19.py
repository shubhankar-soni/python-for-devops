# Problem 1: Meeting Room Occupancy Status
# Goal: You are given a badge-swipe log for a conference room. Employees can either ENTER or EXIT the room. Write a program to find out which employees are still inside the room at exactly 13:00:00 (1 PM). Log file: conferenceroomlogs.txt

with open("conferenceroomlogs.txt", "r") as file:
    lines = file.read().splitlines()

members = []
for line in lines:
    line = line.split()
    timings = line[0]
    status = line[1]
    name = line[2]

    if timings > "13:00:00" : 
        continue
    
    if status == "ENTER":
        members.append(name)
    elif status == "EXIT":
        members.remove(name)

print(members)