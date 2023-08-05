"""This class inherits from BaseGeometry.
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
            raise ValueError("{} must be greater than 0".format(name))
        return value
    def area(self):
        """ area method.
        
        """
        return self.__width * self.__height
    def __str__(self):
        """ __str__ method.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
    



    
