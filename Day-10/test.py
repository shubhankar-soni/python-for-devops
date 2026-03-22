import os

folders = input("Provide list of folder names with spaces in between: ").split()
print(folders)

for folder in folders:
    files = os.listdir(folder)    
    print(files)