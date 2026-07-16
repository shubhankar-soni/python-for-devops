import urllib.request

url = "https://public.karat.io/content/single_url2.txt"

with urllib.request.urlopen(url) as response:
   logfile = response.read().decode("utf-8").splitlines()

urls_dict = {}

for urls in logfile:
    line = urls.strip()
    if line in urls_dict:
        urls_dict[line] += 1
    else:
        urls_dict[line] = 1


most_visited_url = ""
most_visited_url_number = 0
for key, value in urls_dict.items():
    if value > most_visited_url_number:
        most_visited_url_number = value
        most_visited_url = key

print(f"The most visited url is {most_visited_url} with {most_visited_url_number} occurances")

