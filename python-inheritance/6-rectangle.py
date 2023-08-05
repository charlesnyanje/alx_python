from exports import BaseGeometry
"""This module contains the BaseGeometry class.
"""
class Rectangle(BaseGeometry):
    """ Rectangle class.
    """
    def __init__(self, width, height):
        """ __init__ method.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
    def area(self):
        """ area method.
        """
        return self.__width * self.__height
    def __str__(self):
        """ __str__ method.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)