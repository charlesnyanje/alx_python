#!/usr/bin/env python3
"""This module tests 4-base_geometry file if it works correctly.
"""
BaseGeometry = __import__('4-base_geometry').BaseGeometry
"""Created an instance of the class BaseGeometry and assigned it to a variable bg.
"""
bg = BaseGeometry()
"""Handled the exception when area() is not implemented.
"""
try:
    print(bg.area())
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))