"""Import the module Rectangle.
"""
from models.rectangle import Rectangle
"""class square inherited from Rectangle.
"""
class Square(Rectangle):
    """Square class.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """init method.
        """
        super().__init__(size, size, x, y, id)
        self.size = size
        self.x = x
        self.y = y
    """area method for square.
    """
    def area(self):
        return self.size ** 2
    """str method for square.
    """
    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
    