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