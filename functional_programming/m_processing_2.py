import multiprocessing
import time


def print_multiplication(number):
    time.sleep(1)
    return number**2


if __name__ == "__main__":
    start = time.time()

    p = multiprocessing.Process(target=print_multiplication, args=[10])
    p.start()
    p.join()

    end = time.time()

    print(f"\nTotal execution took {end-start:.2f}s\n")
