import sys


class HashableList(list):
    def __hash__(self):
        return id(self)


x = HashableList([1, 2, 3])
y = HashableList([1, 2, 3])


our_set = {x}

# print("Is x in our_set? ", x in our_set)
# print("Is y in our_set? ", y in our_set)
# print("Are x and y equal? ", x == y)


# Our key is a tuple containing a list
my_key = (1, 2, ["a", "b"])
# print(f"Original key: {my_key}")

# Let's access the list using its index (2) and modify it
my_key[2].append("c")

# print(f"Key after change: {my_key}")


# print(hash(my_key))


d = {i: i for i in range(10)}
print(sys.dict_info(d))
