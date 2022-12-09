import multiprocessing
from collections import namedtuple
from pprint import pprint
import time

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


def map_users(x: Person):
    time.sleep(1)

    print(f"Processing {x.name}")

    result = {"name": x.name, "age": x.age}

    print(f"Done processing {x.name}")

    return result


if __name__ == "__main__":
    start = time.time()

    pool = multiprocessing.Pool()

    new_users = tuple(pool.map(map_users, users))

    end = time.time()

    print(f"\nTotal execution took {end-start:.2f}s\n")
    pprint(new_users)


# new_users = tuple(map(map_users, users))
