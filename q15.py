with open("emails.txt","r") as file:
    emails = file.read().splitlines()

for line in emails:
    no_at = line.split("@")
    username = no_at[0]
    root_domain = no_at[1]
    domain_name = root_domain.split(".")[0]
    print("username is", username, "and domain is ", domain_name)