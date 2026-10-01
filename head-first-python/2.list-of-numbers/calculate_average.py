import os

FOLDER = "../swimdata/"


# input: 1:27.95 - minut:second:one hundredth of a second
def calculate_time(time_str: str):
    parts = time_str.replace(".", ":").split(":")

    if len(parts) == 2:
        parts.insert(0, "0")

    minutes, seconds, centiseconds = map(int, parts)
    return (minutes * 60000) + (seconds * 1000) + (centiseconds * 10)


# gets the milliseconds and outputs 1:27.95
def format_time(milliseconds: int):
    # divmod returns (quotient, remainder) as a tuple
    minutes, milliseconds = divmod(milliseconds, 60000)
    seconds, milliseconds = divmod(milliseconds, 1000)

    # Get the tens of milliseconds (centiseconds)
    centiseconds = milliseconds // 10

    return f"{minutes}:{seconds:02}.{centiseconds:02}"


def get_average(times: list):
    # Take each of the times and convert them to a number from
    # the “mins:secs.hundredths” format.
    total = 0
    for time in times:
        total += calculate_time(time)
    average = total // len(times)

    # Calculate the average time, then convert it back to the
    # “mins:secs.hundredths” format (for display purposes).
    average_formatted = format_time(average)
    return average_formatted


def get_metadata(fn: str):
    records = fn.removesuffix(".txt").split("-")
    swimmer, age, distance, type = records
    return swimmer, age, distance, type


def open_files(folder):
    # Display the variables from Task #1, then the list of
    # times, and the calculated average from Task #2.

    for filename in os.listdir(folder):
        with open(folder + filename) as file:
            lines = file.readlines()
            # Break the first line apart by “,” to produce a list of times.
            average = get_average(lines[0].strip().split(","))

        swimmer, age, distance, type = get_metadata(filename)
        print(swimmer, age, distance, type, ":", average)


open_files(FOLDER)
