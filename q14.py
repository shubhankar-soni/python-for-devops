import urllib.request

url = "https://public.karat.io/content/referrals_4.txt"

with urllib.request.urlopen(url) as response:
   logfile = response.read().decode("utf-8").splitlines()

for line in logfile[:2]:
   remove_protocol = line.split("://")[1]
   remove_slash = remove_protocol.split("/")[0]
   print(remove_slash)
   parts = remove_slash.split(".")
   last_two = parts[-2] + "." + parts[-1]

   print(f'"{line}" -> ["{remove_slash}", "{last_two}"]')