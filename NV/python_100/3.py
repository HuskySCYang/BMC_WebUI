#!/usr/bin/python3

def multiply(a,b):
    return a*b
result = multiply(3,multiply(2,4))
print(result)



list1 = [1,2,3]
list2 = list1
print(list1)
print(list2)
list2.append(4)
list2.extend(list1)
print(list1)
print(list2)
