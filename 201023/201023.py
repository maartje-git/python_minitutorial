def add_and_square(a, b, c=5, d=22):
    """Add input and square them."""
    added = a + b + c + d
    squared = added ** 2
    return added, squared

x, y = add_and_square(5, 6, d=2)


def substract(a, b):
    return b - a


# splatting
a = 5
b = 6
args = [a, b]   #make a list of args
add, square = add_and_square(*args) #use * to "splat" them into the function
subt = substract(*args)

kwargs = {"c": 5, "d": 8}
kwarg = dict(c=5, d=8)  # alternative way to make a dictionary
add, square = add_and_square(*args, **kwargs)


#functions vs methods
import numpy as np
data = [1,2,3,4,5]
data_mean = np.mean(data) #function
data = np.array(data) 
data_mean = data.mean() #method to do the same

#scope

def times_by_temp(var):
    return temp * var

temp = 15

print(times_by_temp(3))

temp = 10

print(times_by_temp(3))

# importance of brackets
def say_hello():
    print("Hi there")
    return 5


