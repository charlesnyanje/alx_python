"""This class inherits from Rectangle.
"""
class Square:
    """ Square class.
    """
    def __init__(self, size):
        self.__size = size
    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        return value
    def area(self):
        return self.__size * self.__size
    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)