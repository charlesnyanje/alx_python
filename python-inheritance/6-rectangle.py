"""This module contains the BaseGeometry class.
"""
class Rectangle:
    """ Rectangle class.
    """
    def __init__(self, width, height):
        """ __init__ method.
        """
        self.__width = width
        self.__height = height
    def integer_validator(self, name, value):
        """ integer_validator method.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))
        return value
s = Rectangle(2, 4)