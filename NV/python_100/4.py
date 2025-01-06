#!/usr/bin/python3

set1 = {1,2,3}
result = set1.union({3,4,5})
print(result)


set2 = {3,4,5,6,7}

print("OR: ")
result1 = set1 | set2
print(result1)


print("AND: ")
result1 = set1 & set2
print(result1)

set2.update(set1)
print(set2)
