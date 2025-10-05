# A decorator is just a function that takes a function and returns a new function 
# that adds behavior before/after (or around) the original.

import time

#Non parametric decorator
def timer(func):
    def wrapper(*args, **kwargs):
        start  = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end-start:.3f}s")
    return wrapper

@timer                 # slow_add = timer(slow_add) - replace slow_add with wrapper(wraps around the original function)
def slow_add(a,b):
    time.sleep(1)
    return a+b

slow_add(10,15)

#Parametric decorator
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hi():
    print("Hi!")

say_hi()      



def logger(func):
    callno = 0
    def wrapper(*args, **kwargs):
        nonlocal callno
        callno +=1
        print(f"Name: {func.__name__} no: {callno} args: {args} kwargs: {kwargs}")
        try:
            start = time.perf_counter()
            result = func(*args, **kwargs)
        except Exception as e:
            print(f"Exception {type(e).__name__}: {e}")
            raise
        else:
            t_elapse = time.perf_counter() - start
            print(f"Function result: {result!r} duration: {t_elapse:.8f}s")
    return wrapper


@logger
def no_calc(vals):
    return sum(vals)

no_calc([235,457,85,659,234,102,236,598,879])
        