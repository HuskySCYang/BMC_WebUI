
number_1 = [1,3,5,7,7,9,11,13]
target_1 = list(set(number_1))
print(target_1)

number_2 = [2,4,6,8,10]
target_2 = list(set(number_2))
print(target_2)

number_2.extend(number_1)

target_2 = list(set(number_2))
print(target_2)





