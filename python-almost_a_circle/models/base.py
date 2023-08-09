class Base:
    def __init__(self, id=None,__nb_objects=0):
        if id != None:
            self.id = id
        else:
            __nb_objects += 1
            self.id = __nb_objects
x = Base()