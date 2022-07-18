## What are Python Generators?

> Python Generator functions allow you to declare a function that behaves likes an iterator, allowing programmers to make an iterator in a fast, easy, and clean way. An iterator is an object that can be iterated or looped upon. It is used to abstract a container of data to make it behave like an iterable object. Examples of iterable objects that are used more commonly include lists, dictionaries, and strings.

Iterators and generators are typically used to handle a large stream of data theoretically even an infinite stream of data.

These large streams of data cannot be stored in memory at once, to handle this we can use generators to handle only one item at a time.

## Difference Between Generator Functions and Regular Functions

- The main difference between a regular function and generator functions is that the state of generator functions are **maintained through the use of the keyword yield** and works much like using return, but the difference is that yield saves the state of the function.

- The next time the function is called, execution continues from where it left off, with the same variable values it had before yielding, whereas the return statement terminates the function completely.

- Another difference is that generator functions don’t even run a function, it only creates and returns a generator object.

- Lastly, the code in generator functions only execute when next() is called on the generator object.

## Infinite Fibonacci series

```python
def fibonacci_generator():
    n1=0
    n2=1
    while True:
        yield n1
        n1, n2 = n2, n1 + n2

sequence= fibonacci_generator()

print(next(sequence))
print(next(sequence))
print(next(sequence))
print(next(sequence))
print(next(sequence))

# Output
0
1
1
2
3
```

## Reference

[Basics of Python Generators](https://towardsdatascience.com/basics-of-python-generators-a47b3cab1a23)
