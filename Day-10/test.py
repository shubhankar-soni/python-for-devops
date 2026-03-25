import os

folders = input("Provide list of folder names with spaces in between: ").split()
print(folders)

for folder in folders:
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("Please provide a valid folder name " +folder+ " is not a valid directory")
        continue
    except PermissionError:
        print("No access to " +folder)
        continue

    print("Listing files for the folder====" +folder)
    for file in files:
        print(file)