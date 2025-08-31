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


# BUILD FAILED (OS X 15.6.1 using python-build 2.6.7)

# Inspect or clean up the working tree at /var/folders/qm/pv_s72v97_q5h461g2mlr9d80000gn/T/python-build.20250831141400.5675
# Results logged to /var/folders/qm/pv_s72v97_q5h461g2mlr9d80000gn/T/python-build.20250831141400.5675.log

# Last 10 log lines:
#       __locale_localeconv in _localemodule.o
#       __locale_localeconv in _localemodule.o
#       __locale_localeconv in _localemodule.o
#       __locale_localeconv in _localemodule.o
#   "_libintl_textdomain", referenced from:
#       __locale_textdomain in _localemodule.o
# ld: symbol(s) not found for architecture x86_64
# clang: error: linker command failed with exit code 1 (use -v to see invocation)
# make: *** [Programs/_freeze_module] Error 1
# make: *** Waiting for unfinished jobs....
