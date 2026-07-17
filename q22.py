# Scenario: An API gateway logs incoming traffic. A sudden flood of 500 Internal Server Error statuses from a single IP might indicate a malicious attack or a cascading failure. Write a script to find IPs that generated more than 3 error logs (status codes starting with 5) before a specific cutoff time.
# Cutoff Time: 04:20:00

# Expected Output: ["10.0.0.42"] (Because it hit four 5xx errors before 04:20:00. The error at 04:22:15 happens after the cutoff and shouldn't be counted towards the threshold).

with open("logfile2.txt", "r") as file:
    logs = file.read().splitlines()

counts = {}
count = 0
for log in logs:
    log = log.split()

    time_stamp = log[0]
    ip_addr = log[1]
    http_method = log[2]
    api_url = log[3]
    http_code = log[4]

    if time_stamp > "04:20:00":
        continue

    if "50" in http_code:
        count += 1
        counts[ip_addr] = count

for key,value in counts.items():
    print(f"{key} appeared, {value} times.")
