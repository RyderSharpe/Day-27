# *args
def add(*args):
    print(args[0])
    total = 0
    for n in args:
        total += n
    return total

print(add(1,2,3,4,5,6,7,8,9,10))


## **kwargs
def calculate(n, **kwargs):
    print(kwargs)
    # print(type(kwargs))
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    # print(kwargs["add"])

    # (n == 2) + 3 = 5
    n += kwargs["add"]
    # (n == 5) *= 5 = 25
    n *= kwargs["multiply"]
    print(n)
calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kw):
        # self.make = kw["make"]
        # self.model = kw["model"]

        # or kw.get(""). 'get' will return 'none' if the key for is missing in the 'my_car'
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make = "Nissan")
print(my_car.make)
print(my_car.model)
