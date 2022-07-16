
# Exceptions
from email import message


try:
   container = [23,1,3,4,23] 
   print(container[35])
except Exception as e:
   print(e)

# 2
try:
   a = 5 / 10
   b = a + "10"
except ZeroDivisionError as e:
   print(e)
except TypeError as e:
   print(e)
else:
   print("no exceptions found")
finally:
   print("cleaning up")
   
   
# we can create our own exception classes as such

# for example, value is too low exception

class ValueTooLarge(Exception):
   pass

class ValueTooSmall(Exception):
   def __init__(self, message, value):
      self.message = message
      self.value = value

def test_value(a):
   if a > 100:
      raise ValueTooLarge("Value is too large")
   if a < 10:
      raise ValueTooSmall("Value is too low", a)
   
try:
   test_value(120)
except Exception as e:
   print(e)
   
try:
   test_value(5)
except ValueTooSmall as e:
   print(e.message)
   print(e.value)