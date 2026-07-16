phonebook = {}


phonebook.update({"badri": "929808876", "manoj": "8765432190", "rishabh": "7689066543"})

phonebook.update({"badri": "9000000000"})
print(phonebook)


if "badri" in phonebook:
    print("Found")
else:
    print("Not Found")