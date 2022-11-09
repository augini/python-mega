"""
- The difference between arguments and parameters
   - The parameters are variables that are defined inside Python functions and arguments are variables that are passed to those functions
- Positional and keyword arguments
- Variable-length arguments (**args and **kwargs)
- Container unpacking into function arguments
- Local vs globa arguments
- Parameter passing (by value or by reference)
"""

# - Positional and keyword arguments
def foo(a, b, c):
    print(a, b, c)


# Positional
foo(1, 2, 3)

# Keyword arguments
# order is not important when using keyword arguments
foo(a=1, c=4, b=2)


# - Variable-length arguments (**args and **kwargs)
def foo(a, b, *args, **kwargs):
    print(a, b, *args, **kwargs)

    # @ *args, we can really use any word, stands for packed positional arguments
    # @ **kwargs stands for key word arguments
    for arg in args:
        print(arg)
    for kwarg in kwargs:
        print(kwarg)


# - Container unpacking into function arguments
def foo(a, b, c):
    print(a, b, c)


my_list = [0, 2, 3]
foo(*my_list)

my_dict = {"a": 1, "b": 2, "c": 3}
foo(**my_dict)
