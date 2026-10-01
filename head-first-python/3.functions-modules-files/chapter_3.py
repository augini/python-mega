import swimclub
import os

FN = "Darius-13-100m-Fly.txt"
darius_swim_data = swimclub.read_swim_data(FN)


def calculate_average():
    swim_files = os.listdir(swimclub.FOLDER)

    for n, s in enumerate(swim_files, 1):
        print(n, "Processing:", s)
        swimclub.read_swim_data(s)


calculate_average()
