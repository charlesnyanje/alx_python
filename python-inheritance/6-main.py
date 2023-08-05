#!/usr/bin/env python3
"""This module tests 6-rectangle file if it works correctly.
"""
Rectangle = __import__('6-rectangle').Rectangle
"""Created an instance of the class Rectangle and assigned it to a variable r.
"""
r = Rectangle(3, 5)

print(r)
print(dir(r))
"""Try except block to handle exceptions.
"""
try:
    print("Rectangle: {} - {}".format(r.width, r.height))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    r2 = Rectangle(4, True)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))