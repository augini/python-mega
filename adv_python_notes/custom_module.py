import json
person = {"name": "Farrukh", "age": 24, "occupation":"Software Engineering", "website":"atabekov.com"}

personJSON = json.dumps(person, indent = 4, sort_keys=True)

# paste into a file
# with open("person.json", "w") as file:
#    json.dump(person, file, indent = 4)
   
# convert json into dictionary
# with open("person.json", "r") as file:
#    person = json.loads(file)
#    print(person["name"])

# working with custom classes 
# json module converts dictionaries to json fine, but it throws an error if we want to pass an object to json module
# we can create our own encoder to deal with it
class User():
   def __init__(self, name, age):
      self.name = name
      self.age = age

user = User("Jordan", 40)

# first option
def encode_user(obj):
   if isinstance(obj, User):
      return {"name": obj.name, "age": obj.age}
   else:
      raise TypeError("Object of type User is not JSON serializable")

userJSON = json.dumps(user, default=encode_user)

# second option
from json import JSONEncoder

class UserEncoder(JSONEncoder):
   
   def default(self, obj):
      if isinstance(obj, User):
         return {"name": obj.name, "age": obj.age}
      return JSONEncoder.default()
   
userJSON = json.dumps(user, cls = UserEncoder)

# third option
userJSON = UserEncoder().encode(user)
print(userJSON)