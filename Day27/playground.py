#Adding arguments using *args (Unlimited Arguments)



from pyexpat import model


def add(*args):
    sum = 0
    for num in args:
        sum += num
    return sum
        
# Using **kwargs (Unlimited Keyword Arguments)
print(add(5, 6, 8))

def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.seats = kwargs.get("seats")

my_car = Car(make="Nissan", model="370z")
print(my_car.make)
