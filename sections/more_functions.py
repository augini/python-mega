# use *args for indefinite number of non keyword arguments
def string_format(*args):
    # args returns a tuple
    items = list(args)
    result = [item.upper() for item in items]
    result.sort()
    return result
    
# use **kwargs for indefinite number of keyword values
def find_sum(**kwargs):
    return sum(kwargs.values())
    
print(find_sum(a=3,b=4,c=2))
