with open("chatlog.txt", "r") as file:
    lines = file.read().splitlines()

uniquenames = []
for line in lines:
    words = line.split(" ")
    print(words)

    for word in words:
        if word.split("@")[0] == "" and len(word) > 1:
            name = word.split("@")[1]
            while name[-1] in [",", ".", "?", "!", ":", ";", "'", '"']:
                name = name[:-1]
            
            if name not in uniquenames:
                uniquenames.append(name)

print("Names: ",  uniquenames)
        

            