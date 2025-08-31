FN = "Darius-13-100m-Fly.txt"
FOLDER = "swimdata/"


with open(FOLDER + FN) as file:
    lines = file.readlines()
    print(lines)
