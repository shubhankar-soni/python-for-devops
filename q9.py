cities_dict = {}
file = open("sample2.txt","r")

for cities in file:
    city = cities.strip()
    if city in cities_dict:
        cities_dict[city] += 1
    else:
        cities_dict[city] = 1

print(cities_dict)

max_number = 0
max_city = ""
min_number = None
min_city = ""

for i,j in cities_dict.items():
    if j > max_number:
        max_number = j
        max_city = i
    
    if min_number is None or cities_dict[i] < min_number:
        min_number = cities_dict[i]
        min_city = i
        
print("Word with maximum occurance: ", max_city)

print("Word with minimum occurance: ")
for i in cities_dict:
    if cities_dict[i] == min_number:
        print(i)