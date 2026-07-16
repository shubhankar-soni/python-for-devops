with open("logfilenames.txt","r") as file:
    lines = file.read().splitlines()

for line in lines:
    url = line.strip()
    file_name = url.split("/")[-1]
    print(file_name)
    extension = file_name.split(".")[-1]
    print("Filename ", file_name, "and extension is ", extension)