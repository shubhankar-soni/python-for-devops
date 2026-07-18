with open("logfile4.txt", "r") as file:
    lines = file.read().splitlines()

pods = set()

for line in lines:
    line = line.split()

    if not line:
        continue

    time_stamp = line[0]
    pod_name = line[1]
    status = line[2]

    if time_stamp > "08:03:00":
        continue
    
    if "RUNNING" in status:
        pods.add(pod_name)
    
    else:
        pods.discard(pod_name)
print(f"Pods running before 8:03am are: {pods}")
