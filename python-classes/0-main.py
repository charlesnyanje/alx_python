#!/usr/bin/env python3
Square = __import__('0-square').Square
"""import class Square"""

my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)
"""create an instance of Square"""

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)
"""handle attribute error"""
