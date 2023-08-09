"""This class uses the __nb_objects attribute to assign an id to each instance>
"""


class Base:
    """Base class.
    """

    def __init__(self, id=None, __nb_objects=0):
        """method init.
        """
        if id != None:
            self.id = id
        else:
            __nb_objects += 1
            self.id = __nb_objects


"""Instance of Base class.
"""

b1 = Base()
b1.id = b1.id + 1
print(b1.id)

