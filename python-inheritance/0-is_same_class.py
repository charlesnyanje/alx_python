def is_same_class(obj, a_class):
    if type(obj) is a_class:
        return True
    elif obj is not a_class:
        return False
is_same_class(1, 2)