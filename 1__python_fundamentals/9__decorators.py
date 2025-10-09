# A decorator is just a function that takes a function and returns a new function 
# that adds behavior before/after (or around) the original.

import functools
import time 
from functools import wraps

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
    @functools.wraps(func)
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

# Write a decorator to check whether the arguments to a function is of the right types
# write a simple sum function for three variables, test types of each argument input into the function
# If any argument doesn't match the expected types, raise a TypeError

def ensure_types(*vartypes):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i, (arg, expected_type) in enumerate(zip(args, vartypes)):
                if not isinstance(arg, expected_type):
                    raise TypeError(
                        f"Argument {i+1} expects {expected_type} types, but it got {type(arg)}"
                    )
            result =  func(*args, **kwargs)
            print(result)
            return result
        return wrapper
    return decorator

@ensure_types((int, float), (int, float), (int, float))
def add(a, b, c):
    print(f"Adding {a}, {b}, and {c}...")
    res = a+b+c
    return res 

add(10, 2.5, 2)


# Create a decorator @validate_range(min1, max1, min2, max2, ...) that ensures each positional argument passed to a function falls within a specific numerical range.
# If any argument is outside its allowed range, raise a ValueError.

# ✅ Requirements:
    # The decorator should take 2 values per argument: a minimum and a maximum.
    # It should check only positional arguments (*args), not **kwargs (yet).
    # Raise an exception with a descriptive error message if a value is out of range.




def validate_range(*valrange):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            grouped = []
            # slicing -> sequence[start : stop : step] | valrange[::2]  - all even indices, valrange[1::2] - all odd indices
            # list(zip([0, 10, -5], [100, 20, 5])) -> [(0, 100), (10, 20), (-5, 5)]
            grouped = list(zip(valrange[::2], valrange[1::2]))
            print(grouped)
            for i, (arg, exprange) in enumerate(zip(args, grouped)):
                print(f"index {i} arg: {arg} exprange: {exprange}")
                if not ( exprange[0] <= arg <= exprange [1]):
                    raise ValueError(
                        f"The {i} value is not in the range {exprange[0]} and {exprange[1]}, error: {arg}"
                    )
                else:
                    print(f"Value at {i}:{arg} passed.")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@validate_range(0, 100, 10, 20, -5, 5)
def process_scores(math, physics, chemistry):
    print("All scores are valid.")
    return math + physics + chemistry

process_scores(50, 15, 0)      # ✅ OK
# process_scores(101, 15, 0)     # ❌ Raises ValueError


# You will build a decorator @validate_user_records that checks if user records passed to a function are:
# Correctly structured tuples With fields that match expected types And values that fall within allowed ranges
# If validation fails for any record, the decorator should:
#     Skip it
#     Log an error with the reason (e.g., wrong type, out of range)
#     Allow valid records to continue to the function

# 🧾 Requirements:
    # Each record is a tuple: (name: str, age: int, score: float)
    # The decorator should: Unpack each tuple

# Check:
#     Name is a non-empty string
#     Age is in range 18–99
#     Score is in range 0–100
#     Use enumerate() to track which record failed
#     Use zip() to structure unpacked data
#     Return only valid records to the function

# 🌟 Bonus Ideas (Optional):
#     Add support for keyword arguments: @validate_user_records(strict=True)
#     Convert each valid tuple to a dict for easier use later
#     Log errors to a file or return them separately

records = [
    ("Alice", 25, 88.5),
    ("", 21, 90.0),          # invalid: empty name
    ("Bob", 17, 75.0),       # invalid: age too low
    ("Carol", 23, 105.0),    # invalid: score too high
    ("Dave", 34, 67.0)       # valid
]


def validate_user_records(func):
    reclist = []
    validity = []
    validrecords = []
    @wraps(func)
    def wrapper(*args, **kwargs):
        indexed = list(enumerate(*args,start=1))
        for i in indexed:
            rec = [a for x in i for a in (x if isinstance(x, tuple) else [x])]
            reclist.append(rec)
        print(reclist)

        for id in reclist:
            errorlist = []
            tempvalid = []
            tempvalid.append(id[0])
            errorlist.append(id[0])
            if id[1] == "":
                errorlist.append(f"Name is empty")
                tempvalid.append("Err")
                # raise ValueError(
                #     f"Name is empty."
                # )
            else: 
                tempvalid.append(id[1])
                errorlist.append("No error")
            if (18 >= id[2] >= 99):
                errorlist.append(f"Age out of range 18 - 99 --> {id[2]}")
                tempvalid.append("Err")
                # tempvalid.append(f"Age out of range 18 - 99 --> {id[2]}")
                # raise ValueError(
                #     f"Age is out of range [18,99] --> {id[2]}"
                # )
            else:
                tempvalid.append(id[2])
                errorlist.append("No error")
            if (id[3] <= 0 or id[3] >= 100):
                errorlist.append(f"Score out of range 0 - 100 --> {id[3]}")
                tempvalid.append("Err")
                # tempvalid.append(f"Score out of range 0 - 100 --> {id[3]}")
                # raise ValueError(
                #     f"Score is out of range [0,100] --> {id[3]}"
                # )
            else:
                tempvalid.append(id[3])
                errorlist.append("No error")
            
            errorlist.append({
                "id": id[0],
                "name": tempvalid[0],
                "age": tempvalid[1],
                "score": tempvalid[2],
            })
            if not "Err" in tempvalid:
                validrecords.append(tempvalid)           

        print(validrecords)
        # for item in validity
        return validrecords
    return wrapper



@validate_user_records
def process_users(valid_users):
    # Expecting only valid records
    print(f"Processing {len(valid_users)} valid users...")
    # Do something with valid_users...


process_users(records)