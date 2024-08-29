# *args: Positional Variable-Length Arguments
def add(*args):
    # print(args[1])

    sum = 0
    for n in args:
        sum += n
    return sum
# print(add(3, 5, 6, 2, 1, 7, 4, 3))


# **kwargs: Keyworded Variable-Length Arguments
def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    # print(n)


calculate(2, add=3, multiply=5)


# How to use a **kwargs dictionary safely
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="Skyline")
print(my_car.model)



#######################################################################################
# Keyword Arguments
def my_function(a, b, c):
    # Do this with a
    # Then do this with b
    # Finally do this with c
my_function(c=3, a=1, b=2) # a,b,c in any order we want as long as keyword is in front

# Arguments with Default Values
def my_function(a=1, b=2, c=3):
    my_function()
    # To modify
    my_function(b=5)
#######################################################################################

# Fixed arguments
def add(n1, n2):
    return n1 + n2
add(n1=5, n2=3)

# Unlimited Arguments
def add(*args): # '*' is required; 'args', short for arguments is a variable.
    for n in args:
        print(n)
add(n1=5, n2=3)

