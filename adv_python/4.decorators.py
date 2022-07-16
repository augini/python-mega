# Decorators are used to extend the behaviour of the function without explicitly changing it

def start_end_wrapper(func):
   def wrapper():
      print("starting the execution")
      func()
      print("ending the execution")
   return wrapper

def print_name():
   print("My name is username")

# first way  
print_name = start_end_wrapper(print_name)
# print_name()

# second way using decorators
@start_end_wrapper
def print_name():
   print("My name is username")

# print_name()

# when the function has an argument, we also need to pass the argument to the wrapper
import functools

def start_end_wrapper_args(func):
   
   @functools.wraps(func)
   def wrapper(*args, **kwargs):
      
      print("starting the execution")
      result = func(*args, **kwargs)
      print("ending the execution")
      return result
   
   return wrapper

@start_end_wrapper_args
def add10(x):
   return x + 10

# print(add10(5))

# if we use it like this, Python might get confused about the identity of our function
# to counter this, we decorate our wrapper function with functools wrapper 

# ---------------
# we can also pass arguments to decorators

def repeat(num_times):
   def decorator_repeat(func):
      
      @functools.wraps(func)
      def wrapper(*args, **kwargs):
         for _ in range(num_times):
            result = func(*args, **kwargs)
         return result
      
      return wrapper
   
   return decorator_repeat

@repeat(2)
def greet(name):
   print(f"Hi {name}")

# greet("Alex")

# ------------------
# we can also create class decorators as such

class CountCalls():
   def __init__(self, func):
      self.func = func
      self.num_calls = 0
   
   def __call__(self, *args: any, **kwargs: any) -> any:
      self.num_calls +=1
      print(f"This is executed {self.num_calls} times")
      return self.func(*args, **kwargs)

@CountCalls
def say_hello():
   print("Hello there")
   
say_hello()