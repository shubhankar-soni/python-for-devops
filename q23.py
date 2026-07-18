# HEALTHY and UNHEALTHY. To calculate overall infrastructure stability, write a script to identify which specific services are actively degraded (UNHEALTHY) at exactly 12:00:00. 
# Expected Output at 12:00:00: ["payment-service", "cart-service"] (auth-service recovered before 12:00, and payment-service didn't recover until 12:05).

with open("logfile3.txt", "r") as file:
    lines = file.read().splitlines()

status_dict = []

for line in lines:
    line = line.split()
    time_stamp = line[0]
    service_name = line[1]
    status = line[2]

    if time_stamp > "12:00:00":
        continue
    
    if status == "UNHEALTHY":
        status_dict.append(service_name)
    else:
        status_dict.remove(service_name)

print(f"services unhealthy at 12 AM: {status_dict}")
