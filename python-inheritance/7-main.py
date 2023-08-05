#!/usr/bin/env python3
"""This module tests 7-rectangle file if it works correctly.
"""
Rectangle = __import__('7-rectangle').Rectangle
"""Created an instance of the class Rectangle and assigned it to a variable r.
"""
r = Rectangle(3, 5)
"""Prints the string representation of the instance r.
"""
print(r)
print(r.area())