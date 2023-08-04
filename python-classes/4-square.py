"""Class Square that defines a square by: (based on 3-square.py)
"""

class Square:
    """__init__ method to initialize the Square instance.
    """

    def __init__(self, size=0):
        """private instance attribute: size.
        """
        self.__size = size

    @property
    def size(self):
        """Getter for size property.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size property.
        Args:
            value (int): size of the square.
        Handle:
            TypeError: if size is not an integer.

            ValueError: if size is less than 0.
        """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")
    """public instance method: def area(self).
    Returns:
        the current square area.
    """

    def area(self):
        return self.__size**2
    
    def my_print(self):
        """Prints in stdout the square with the character #.
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)


                
