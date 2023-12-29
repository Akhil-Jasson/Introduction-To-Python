# Unlimited Positional Arguments
def add(*args):
    sum = 0
    for i in args:
        sum += i
    print(sum)


add(5, 6, 7)
add(5, 6, 7, 8)


# Returns dictionary with keyword arguments
def calculate(n, **kwargs):
    # print(kwargs)
    # for key,value in kwargs.items():
    #     print(key, value)

    # print(kwargs["add"])

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model") # While using get, when value is not present, none gets returned


my_car = Car(make="Suzuki")
