numbers = [4,5,2,4,6,5,4,5,5]

counts = {}

for i in numbers:
    if i in counts:
        counts[i] += 1
    else:
        counts[i] = 1

print(counts)
max_num = 0
numb = ""

for key,value in counts.items():
    if value > max_num:
        max_num = value
        numb = key

print(numb, "appears", max_num, "times")
    
