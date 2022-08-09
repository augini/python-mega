# Threads and Processes (Python)

## What is a process and a thread ?

Process is an instance of a program. (Python interpreter, browser tab)
Thread is an entity within a process. One process can have multiple threads inside

## Processes

### Advantages of processes

- Takes advantage of multiple CPUs and Cores

  _It enables to execute your code in multiple CPUs in parallel_

- Seperate memory space - memory is not shared between processes

  _If you have to process large data, you can process it between multiple CPUs and speed up your program_

- Great for CPU-bound processing
- New process is stated independently from other processes
- Processes are interruptable / killable
- One GIL for each process -> avoids GIL (Global Interpreter Lock) limitation

### Disadvantages of processes

- Heavyweight
- Starting a new process is slower than starting a new process
- More memory
- IPC (inter-process communication) is more complicated

## Threads

Thread is an entity within a process and one process can have multiple threads

### Advantages of threads

- All threads within a process share the same memory
- Lightweight
- Starting a thread is faster than starting a process
- Great for I/O bound tasks

### Disadvantages of threads

- Threading is limited by GIL: Only one thread at a time
- No effect for CPU bound tasks
- Not interruptable / killable
- Need to be careful with race conditions
  Race conditions occur when multiple threads want to modify a certain variable at the same time

## What is GIL (Global Interpreter Lock) ?

- A lock that allows only one thread at a time to execute in Python
- Needed in CPython because memory management is not thread safe

### Avoid with GIL

- the use of multiprocessing
- use a different, free-threaded Python implementation (JPython, IronPython)
- use Python as a wrapper for third-party libraries (C, C++) -> numpy, scipy
