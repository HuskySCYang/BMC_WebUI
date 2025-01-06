#!/usr/bin/python3
dict_1 = {"a": 1, "b": 2,"c": 3}
##get dict values
result = dict_1.values()
## get dict key"a"
print(dict_1["a"])
##get dict key "b"
print(dict_1.get("b"))
##changed dict key "c" from 3 to "gg"
dict_1["c"] = "gg"
print(dict_1.get("c"))
##changed dict key "a" from 1 to 100
dict_1.setdefault("a",100)
## changed dict key "d" to 99, if "d" not present, add key "d"
dict_1.setdefault("d",99)
print(dict_1)
print(result)

#######################################################################
dict_2 = {"e":100, "f": 33, "g": 44}

a = dict_2.keys()
c = dict_2.values()

print(a)
print(list(a))
print(c)
print(list(c))

##merge dict_1 and dict_2
dict_1.update(dict_2)
print(dict_1)

##copy dict_2 to dict_3
dict_3 = dict_2.copy()
print(dict_3)


print("e" in dict_2)
print("33" in dict_2)
