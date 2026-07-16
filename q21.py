# Goal: A cloud architecture log tracks when servers are put into MAINTENANCE mode or brought back ONLINE. Write a program to determine which servers are actively in maintenance mode at 05:00:00 AM.

with open("logfile1.txt", "r") as file:
    lines = file.read().splitlines()

server_list = []
for line in lines:
    line = line.split()
    
    time_stamp = line[0]
    status = line[1]
    servers = line[2]

    if time_stamp > "05:00:00":
        continue

    if status == "MAINTENANCE":
        server_list.append(servers)
    
    elif status == "ONLINE":
       server_list.remove(servers)

print("Servers which are under maintenance at 5AM", server_list) 
