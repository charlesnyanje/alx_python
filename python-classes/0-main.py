#!/usr/bin/env python3
"""import class Square"""
Square = __import__('0-square').Square

"""create an instance of Square"""
my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

"""handle attribute error"""
try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)
