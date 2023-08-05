#!/usr/bin/env python3
"""This module tests 8-square file if it works correctly.
"""
Square = __import__('8-square').Square
"""Created an instance of square and assigned it to a variable s.
"""
s = Square(13)
"""Prints the square and its area.
"""
print(s)
print(s.area())
