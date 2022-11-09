from collections import namedtuple

collection = (10, 12, 32, 34, 34)
print(collection[1])

fruit = namedtuple("fruit", "number variety color")
guava = fruit(number=2, variety="HoneyCrisp", color="green")
print(guava.count)

names = ["user_1", "user_2", "user_3", "accomplished_user_4"]
print(
    names.count("user_1"),
)

original_list = [1, 34, 34, 12, 2, 4]
new_list = [i * 12 for i in original_list]
print(new_list)
