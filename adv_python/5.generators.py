# we can create a generator in the following way and access its elements
import sys


def simple_generator():
    yield 1
    yield 3
    yield 3
    yield 4

# 1
# for i in simple_generator():
#     print(i)

# 2 -> generators keep the state of the function
_g = simple_generator()
# print(next(_g))
# print(next(_g))

# Since generators are an iterable object, we can pass them to methods such as sum
# print(sum(_g)) # output -> 7
# print(sorted(_g))

# we can compare the memory efficiency of generators in the folowing way.
def firstn(n):
   num = 0
   nums = []
   while num < n:
      nums.append(num)
      num +=1
   return nums

def firstn_generator(n):
   num = 0
   while num < n:
      yield num
      num +=1

firstn_ = sum(firstn(100))
firstn_g = sum(firstn_generator(100))

# print(firstn_, sys.getsizeof(firstn(1000)))
# print(firstn_g, sys.getsizeof(firstn_generator(1000)))

# ouput 
# 4950 8856
# 4950 104

def fibonacci_generator():
    n1=0
    n2=1
    c = 0
    while c < 100:
        yield n1
        n1, n2 = n2, n1 + n2
        c+=1
        

# print(sum(fibonacci_generator()))
for item in fibonacci_generator():
    print(item)