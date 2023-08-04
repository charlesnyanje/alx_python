class Square:
    """Square class with a private attribute - size.
    Args:  
            size (int): size of the square.

    Raises:

            TypeError: if size is not an integer.
     """

    def __init__(self, size=0):
        """_summary_

        Args:
            size (int, optional): _description_. Defaults to 0.
        """
        self.__size = size


square = Square()
