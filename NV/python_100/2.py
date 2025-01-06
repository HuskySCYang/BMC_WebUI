#!/usr/bin/python3
def uppercase_text(text):
    return text.upper()

result = uppercase_text("Hello, world!!")
print(result)

'''
>>> A="Hollo world!!"
>>> B = A.uppercase()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'uppercase'
>>> B = uppercase(A)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'uppercase' is not defined
>>> B = upper(A)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'upper' is not defined. Did you mean: 'super'?
>>> B = A.upper()
>>> print(B)
HOLLO WORLD!!
>>> 

'''
