#printing a combination of two digits from 00 to 99
def comb2():
    for i in range(0, 99):
        print("{:02d}".format(i), end=", ")
    print("99")
comb2()