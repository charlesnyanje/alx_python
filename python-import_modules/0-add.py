from add_0 import add
print("0_add is set to: {}".format(__name__))
a=1
b=2
if __name__ == "__main__":
    print("{} + {} = {}".format(a, b, add(a, b)))
else:
    print("I am not a main program")