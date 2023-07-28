from add_0 import add
print("add is set to: ",__name__)
a=1
b=2
if __name__ == "__main__":
    print("{} + {} = {}".format(a, b, add(a, b)))
