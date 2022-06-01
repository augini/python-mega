name = input("Enter your name: ")
surname = input("Enter your surname: ")
when = "today"

message = "Hello %s %s" % (name, surname)
message_formatted = f"Hello {name} {surname}"
print(message)

# another way to format stringgs
name = "John"
surname = "Smith"
 
message_new_format = "Your name is {}. Your surname is {}".format(name, surname)
print(message_new_format)
