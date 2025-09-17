# The exercise given below shows how args and kwargs can be used
# args is a tuple, positional arguments
# kwargs (keyword arguments) is a dictionary {'a':4, 'b':5}
# args and kwargs let the function accept any no of positional arguments and keyword arguments 

def super_sum(*args, **kwargs):
    total = sum(args)                   #get the sum of positional arguments
    total += sum(kwargs.values())       #get the sum of "values" in keyword arguments
    return total

print(super_sum(1, 2, 3, a=4, b=5))    #positional argument must appear before keyword arguments
print(super_sum(10, b=20))