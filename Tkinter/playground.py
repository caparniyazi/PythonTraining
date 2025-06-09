# This function accept any number of arguments.
def add(*args):
    total = 0

    for n in args:
        total += n

    return total


print(add(1, 2, 3, 4, 5))


def calculate(**kwargs):
    print(kwargs)
    for (key, value) in kwargs.items():
        print(key)
        print(value)


calculate(add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")  # Optional keyword arg
        self.model = kw.get("model")  # Optional keyword arg
        self.colour = kw.get("colour")


my_car = Car(make="Honda")
print(my_car)
print(my_car.model)
