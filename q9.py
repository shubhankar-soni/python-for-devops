file = open("sample2.txt", "r")

cities = {}
max_number = 0
min_number = 0

for line in file:
    city = line.strip()
    if city != "":
        if city in cities:
            cities[city] += 1
        else:
            cities[city] = 1

max_number = max(cities, key=cities.get)
min_number = min(cities, key=cities.get)
print(max_number)
