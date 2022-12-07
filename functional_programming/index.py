from collections import namedtuple
from pprint import pprint
from functools import reduce
from datetime import date
from collections import defaultdict

Person = namedtuple("Person", "name, age, job, salary, relationship, hometown")

users = (
    Person("user_1", 24, "coder", 2600, "married", "Khorezm"),
    Person("user_2", 26, "manager", 2800, "single", "Shovot"),
    Person("developer", 30, "developer", 3800, "divorced", "Xonqa"),
    Person("martian", 34, "devops engineer", 4000, "widow", "Tashkent"),
    Person("user_24", 26, "security engineer", 3800, "single", "Shovot"),
    Person("user_10", 30, "accountant", 3000, "married", "Xonqa"),
    Person("jupiter", 40, "designer", 4800, "married", "Tashkent"),
)


def check_relationship(user: Person):
    return user.relationship == "married"


# filter method
married_users = tuple(filter(check_relationship, users))
dev_users = filter(lambda x: x.job == "developer", users)

# map method
mapped_users = tuple(
    map(lambda x: "great" if x.relationship == "married" else "not so great", users)
)

# reduce method
numbers = [1, 2, 3, 4]
_sum = reduce(lambda x, y: x * y, numbers)


def calculate_salary(x, y):
    if isinstance(x, tuple):
        return x.salary + y.salary
    else:
        return x + y.salary


def group_by_relationship(acc, item):
    acc[item.relationship].append(item.name)
    return acc


user_total_ages = reduce(calculate_salary, users)

user_grouped_by_relationships = reduce(
    group_by_relationship,
    users,
    {"married": [], "divorced": [], "single": [], "widow": []},
)

# second approach with defaultdict
user_grouped_by_relationships = reduce(group_by_relationship, users, defaultdict(list))
print(user_grouped_by_relationships)

# pprint(married_users)
list_comprehension = [user for user in range(1, 10)]
