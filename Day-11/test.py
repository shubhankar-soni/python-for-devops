set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

union_set = set1.union(set2)  # Union of sets
intersection_set = set1.intersection(set2)  # Intersection of sets
difference_set = set1.difference(set2)  # Difference of sets

print(union_set)
print(intersection_set)
print(difference_set)

is_subset = set1.issubset(set2)  # Checking if set1 is a subset of set2
is_superset = set1.issuperset(set2)  # Checking if set1 is a superset of set2

print(is_subset)
print(is_superset)
# my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

# for a, b in my_dict.items():
#     print(a, b)