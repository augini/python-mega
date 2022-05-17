
names = ["angela", "john", "mark", "johnson", "jordan", "", " ", "y"]

formatted_names = [name.capitalize() for name in names]
print(formatted_names)

# with conditional if statements
formatted_names = [name.capitalize() for name in names if len(name) >= 2]
print(formatted_names)

# create an iterable data type
set_range = [i for i in range(0, 24, 4)]
print(set_range)

# if-else-with-list comprehensions
def format(items):
    return [x if type(x) == int else 0 for x in items]

def get_sum(items):
    return sum([float(x) for x in items])