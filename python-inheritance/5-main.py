#!/usr/bin/env python3
"""This module tests 5-base_geometry file if it works correctly.
"""
BaseGeometry = __import__('5-base_geometry').BaseGeometry
"""Created an instance of the class BaseGeometry and assigned it to a variable bg.
"""
bg = BaseGeometry()
"""Called integer_validator() method with the following parameters:
    - "my_int" and 12
    - "width" and 89.
"""
bg.integer_validator("my_int", 12)
bg.integer_validator("width", 89)
"""Try except block to handle the exception when area() is not implemented.
"""
try:
    bg.integer_validator("name", "John")
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("age", 0)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("distance", -4)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
