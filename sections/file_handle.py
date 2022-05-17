# first approach
fruits_file = open("./files/fruits.txt")
file_content = fruits_file.read()
fruits_file.close()

# print(file_content)

# second approach
with open("./files/fruits.txt") as myfile:
  content = myfile.read()

print(content)

# write to a file
with open("./files/vegetables.txt", "w") as file:
  file.write("tomato")

# read the initial 90 character of a file
with open("fruits.txt", "r") as file:
    content = file.read()
    print(content[:90])

# find the occurances of char in a file
def get_file_content(character, filepath):
    
    with open(filepath, "r") as file:
        content = file.read()
    
    return content.count(character)