# Interview Questions

## Table of Contents

- [Interview Questions](#interview-questions)
  - [Table of Contents](#table-of-contents)
  - [Python](#python)
    - [Why python? What are its pros and cons?](#why-python-what-are-its-pros-and-cons)
    - [List Vs. Tuple](#list-vs-tuple)
    - [Instance Method VS. Class Method Vs. Static Method](#instance-method-vs-class-method-vs-static-method)
    - [Explain Context Manager in Python](#explain-context-manager-in-python)
    - [Explain Generators in Python](#explain-generators-in-python)
    - [Iterators Vs. Generators in Python](#iterators-vs-generators-in-python)
    - [Shallow Copy vs Deep Copy in Python](#shallow-copy-vs-deep-copy-in-python)
    - [Python Lists \& Their Low-Level Handling](#python-lists--their-low-level-handling)
    - [Python Dictionaries and Their Low-Level Handling](#python-dictionaries-and-their-low-level-handling)
    - [How Open Addressing \& Quadric Probing Work](#how-open-addressing--quadric-probing-work)
    - [Why Can't Mutable Types Be Dictionary Keys?](#why-cant-mutable-types-be-dictionary-keys)
    - [Mutable Vs. Immutable Types in Python](#mutable-vs-immutable-types-in-python)
    - [Encryption Vs. Hashing](#encryption-vs-hashing)
    - [Sequential Execution in Python](#sequential-execution-in-python)
    - [Async Execution in Python](#async-execution-in-python)
    - [Coroutine Vs. Regular function in Python](#coroutine-vs-regular-function-in-python)

## Python

### Why python? What are its pros and cons?

- Python is my main programming language because of its **simplicity**, **readability**, and **wide ecosystem**. It allows me to write clean, maintainable code quickly, which is ideal for both prototyping and production-level applications.
- Pros of Python:

  1. **Readability & Simplicity**  
     Python’s syntax is clean and expressive, resembling pseudo-code. This makes it easier to read, debug, and onboard new team members quickly.

  2. **Large Ecosystem**  
     Python has a rich set of libraries and frameworks. For web development, I use **Django** and **FastAPI**, while for data tasks, libraries like **Pandas**, **NumPy**, and **scikit-learn** are widely used.

  3. **Vibrant Community**  
     A huge open-source community means lots of support, regular updates, and mature third-party packages.

  4. **Cross-domain Usage**  
     Python is versatile — used in web development, data science, scripting, automation, DevOps, machine learning, and more. That means my Python skills transfer across multiple domains.

  5. **Integration Capabilities**  
     Python plays well with other languages and systems via APIs, bindings, and tools like Cython or PyBind.

- Cons of Python:

  1. **Performance**  
     Being an interpreted and dynamically typed language, Python can be slower than compiled languages like C++ or Java. But this is often mitigated using tools like **C extensions** or offloading performance-heavy parts to optimized services.

  2. **Mobile Development**  
     Not ideal for mobile app development. Other languages and platforms (like Swift or Kotlin) are better suited for that domain.

  3. **Threading Limitations (GIL)**  
     The Global Interpreter Lock (GIL) can be a bottleneck in CPU-bound multi-threaded applications. However, it can be worked around using multiprocessing or by delegating heavy tasks to external services.

  4. **Runtime Errors**  
     Being dynamically typed, Python may have more runtime errors if type hints or proper testing aren’t enforced.

---

### List Vs. Tuple

| Feature          | List   | Tuple  |
| ---------------- | ------ | ------ |
| Mutable          | Yes    | No     |
| Ordered          | Yes    | Yes    |
| Indexable        | Yes    | Yes    |
| Use as Dict Key  | No     | Yes    |
| Iteration Speed  | Slower | Faster |
| Memory Efficient | Less   | More   |

---

### Instance Method VS. Class Method Vs. Static Method

| Feature          | Instance Method   | Class Method                       | Static Method           |
| ---------------- | ----------------- | ---------------------------------- | ----------------------- |
| Decorator        | (none)            | @classmethod                       | @staticmethod           |
| First parameter  | self (instance)   | cls (class)                        | No default first arg    |
| Access instance? | Yes               | No                                 | No                      |
| Access class?    | Via self.class    | Yes                                | No                      |
| Use case         | Instance behavior | Factory methods, alter class state | Utility/helper function |

---

### Explain Context Manager in Python

A **context manager** is a construct in Python that allows you to **allocate and release resources** precisely when you want to.
It is commonly used with the **`with`** statement.

- Use Cases:
  - File handling
  - Managing database connections
  - Acquiring/releasing locks
  - Managing network connections or sockets
  - Opening/closing resources like web pages or APIs
  - Temporary environment changes (e.g., mocking, config override)

```python
with <context_manager> as <var>:
    # Do something
    pass

# How context manager works internally
class MyContext:
    def __enter__(self):
        # Setup code
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Cleanup code
        pass

# Example
class ManagedFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, 'r')
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

with ManagedFile('example.txt') as f:
    print(f.read())

# turn a generator into a context manager (python's library)
from contextlib import contextmanager

@contextmanager
def open_file(name):
    f = open(name, 'r')
    try:
        yield f
    finally:
        f.close()

with open_file('example.txt') as f:
    print(f.read())
```

---

### Explain Generators in Python

A **generator** is a special type of **iterable** in Python that **yields** items one at a time using the `yield` keyword, instead of returning them all at once.

It helps you **generate values on the fly**, saving memory and improving performance, especially with large datasets.

**Benefits**:

- Memory Efficient: Only one item is loaded into memory at a time.
- Lazy Evaluation: Values are produced only when needed.
- Infinite Sequences: Perfect for streams or infinite data (e.g., Fibonacci).

**Use Cases**:

- Reading large files line by line
- Producing infinite sequences (like itertools.count)
- Streaming data processing (e.g., logs, APIs)
- Implementing pipelines (data transformations)

```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

gen = fibonacci()
for _ in range(5):
    print(next(gen))
```

---

### Iterators Vs. Generators in Python

| Feature            | Iterator                              | Generator                              |
| ------------------ | ------------------------------------- | -------------------------------------- |
| Definition         | Object with **iter**() and **next**() | Uses yield in a function               |
| Creation           | Manually (class + methods)            | Using generator function or expression |
| Memory Usage       | Depends on implementation             | Memory-efficient (lazy eval)           |
| Infinite Sequences | Yes                                   | Yes                                    |
| Syntax             | More boilerplate                      | Simple, clean syntax                   |
| Performance        | Slightly slower (custom classes)      | Faster for large/lazy sequences        |
| State Management   | Manual                                | Automatic (via yield)                  |

---

### Shallow Copy vs Deep Copy in Python

In Python, copying objects can be done in two ways: **shallow copy** and **deep copy**. The key difference between them is how they handle nested objects (objects within objects).

A **shallow copy** creates a new object, but it **does not copy nested objects**. Instead, it **references** the objects contained in the original object.

A **deep copy** creates a new object and **recursively copies all nested objects**. The new object is **completely independent** of the original object.

```python
import copy

original = [1, 2, [3, 4]]
shallow_copy = copy.copy(original)
deep_copy = copy.deepcopy(original)

# Modifying the inner list
shallow_copy[2][0] = 100

print("Original:", original)  # [1, 2, [100, 4]]
print("Shallow Copy:", shallow_copy)  # [1, 2, [100, 4]]
print("Deep Copy:", deep_copy)  # [1, 2, [3, 4]]
```

---

### Python Lists & Their Low-Level Handling

In Python, **lists** are not traditional arrays (like in languages such as C or Java). Instead, they are implemented as **dynamic arrays** (also called "resizable arrays").

Key Features:

- **Dynamic resizing**: Python lists can grow or shrink in size as elements are added or removed.
- **Homogeneous**: Lists can store elements of different data types (unlike traditional arrays in low-level languages).
- **Overhead**: Python lists store extra information to manage dynamic resizing.

At a low level, Python lists are implemented as **arrays of pointers** to the objects they store. Here's how it works:

1. **Contiguous Memory Block**:

   - Internally, Python uses a contiguous block of memory to store pointers to the objects in the list. These pointers reference the actual data objects (which can be of any type).
   - This is different from traditional C arrays, which store actual data values directly in memory.

2. **Dynamic Array**:

   - When the list exceeds its current capacity, Python **doubles** the size of the array to accommodate more elements. This dynamic resizing ensures that appending new elements remains efficient on average.
   - This resizing operation incurs a cost, but it happens relatively infrequently (amortized constant time).

3. **Memory Layout**:

   - Python lists are implemented as **arrays of references (pointers)** to objects.
   - Each element in the list holds a reference (pointer) to an object stored elsewhere in memory.
   - The actual memory layout of Python lists is managed by the **Python memory allocator** (via CPython's implementation).

4. **Why Lists Are Not Fixed-Size Arrays**:
   - Python lists are more flexible than fixed-size arrays because they can grow or shrink dynamically as items are added or removed.
   - However, this comes with the trade-off of extra memory overhead for storing object references and managing resizing.

---

### Python Dictionaries and Their Low-Level Handling

A **Python dictionary** is an **unordered** collection of key-value pairs. It is implemented using a **hash table** at a low level, which allows for efficient **O(1)** average-time complexity for lookups, insertions, and deletions.

Key Features:

- **Key-Value Pairs**: Every dictionary consists of pairs where each **key** is mapped to a corresponding **value**.
- **Unordered**: The order of the items in a dictionary is not guaranteed (prior to Python 3.7).
- **Keys Must Be Hashable**: Only immutable types (like strings, numbers, or tuples) can be used as keys in a dictionary.

Low-Level Handling of Python Dictionaries

1. At the core of Python dictionaries is a **hash table**.

   - **Hashing**: Each key is passed through a **hash function** to compute a unique index (called the **hash value**), which determines where the key-value pair will be stored.
   - **Collision Resolution**: If two keys hash to the same index (i.e., a collision), Python uses a technique called **open addressing** (specifically, **quadratic probing**) to resolve these collisions and find an available slot.

2. **Memory Layout**

   - **Dynamically Resized**: Like lists, Python dictionaries automatically resize when they grow too large. The dictionary increases in size to maintain efficiency, usually by **doubling** its size.
   - **Buckets**: Internally, a dictionary is composed of a series of "buckets" where key-value pairs are stored. The number of buckets changes as the dictionary grows, typically during resizing operations.

3. **Efficiency**

   - **Lookup Efficiency**: Dictionary lookups, insertions, and deletions are generally **O(1)** on average because the hash function allows direct access to the bucket where the key-value pair is stored.
   - **Amortized Cost of Resizing**: While resizing is an expensive operation (O(n) time), it happens less frequently and only when the dictionary exceeds its capacity, meaning the operation is **amortized O(1)**.

4. **Internal Structure**
   - Internally, Python dictionaries are structured as a **contiguous block of memory** that holds pairs of keys and values along with additional metadata for hashing and handling collisions.
   - **Key and Value Storage**: The keys and values are stored in the dictionary's memory block, and the keys are hashed to determine their storage index.
   - **Optimizations**: Python 3.6+ has optimizations that reduce the memory footprint of dictionaries by storing keys in a more compact and efficient layout.

```python
d = {"apple": 1, "banana": 2}

# Check the hash value for a key
print(hash("apple"))  # Hash value for "apple"
print(hash("banana"))  # Hash value for "banana"
```

---

### How Open Addressing & Quadric Probing Work

Open addressing is a method of handling collisions in a hash table where, instead of using a separate data structure (like a linked list) to store collided elements, the elements are stored directly in the hash table array itself.

When a collision occurs (i.e., when two keys hash to the same index), open addressing probes the array (searches for another spot) until an empty slot is found for the key.

Quadratic probing is a strategy for finding the next available slot in the hash table by using quadratic functions to calculate the next probe location.

How Quadratic Probing Works:

- Initial Hash Calculation:

  The hash function is applied to a key to get an initial index where the key should be placed.

- Collision Occurs:

  If the calculated index is already occupied (a collision), quadratic probing is used to search for the next available slot.

  The probe sequence increases quadratically as \( i \) increases, ensuring that the search space expands more rapidly after each collision.

- Probe Sequence:

$$ New Index = (h(k) + i^2) \mod N $$

Where:

- ( $h(k)$ ) is the original hash value of the key ( $k$ ).
- ( $i$ ) is the number of collisions encountered so far (starting from 1).
- ( $N$ ) is the size of the hash table (used to ensure the index stays within bounds).
- ( $i^2$ ) is the square of the number of collisions (quadratic function).

The idea is that the probe sequence grows quadratically with the number of attempts, ensuring that the search space is expanded more rapidly, reducing the chance of infinite loops and clustering.

---

### Why Can't Mutable Types Be Dictionary Keys?

1. Changing Hash Values

   The hash value of a dictionary key must remain constant. If the hash value of a key changes after it has been inserted into the dictionary, the dictionary will not be able to locate the key correctly.

   Mutable types like lists or dictionaries can have their contents modified, which would change their hash value. This would disrupt the dictionary's internal data structure and lead to errors or unexpected behavior.

2. Equality Comparisons

   If the contents of a mutable object change, it might affect how the object is compared for equality. For instance, if you modify a list used as a dictionary key, it might not be "equal" to itself based on its new state, leading to inconsistencies when looking up the key.

---

### Mutable Vs. Immutable Types in Python

| Feature      | Mutable Objects                                  | Immutable Objects                                  |
| ------------ | ------------------------------------------------ | -------------------------------------------------- |
| Modification | Can be changed after creation                    | Cannot be changed after creation                   |
| Examples     | `list, dict, set, bytearray`                     | `int, str, tuple, frozenset`                       |
| Hashability  | Not hashable (cannot be used as dictionary keys) | Hashable (can be used as dictionary keys)          |
| Efficiency   | Typically more efficient for modifications       | May require creating new objects for modifications |
| Memory       | Same object in memory is modified                | A new object is created for each modification      |

---

### Encryption Vs. Hashing

| Feature       | Encryption                                              | Hashing                                                      |
| ------------- | ------------------------------------------------------- | ------------------------------------------------------------ |
| Direction     | Bi-directional (can decrypt to get original data)       | One-way (cannot retrieve original data)                      |
| Purpose       | Confidentiality (protect data from unauthorized access) | Integrity (verify data hasn't been tampered with)            |
| Key           | Requires a key for encryption and decryption            | No key needed, only the hash function is used                |
| Output Size   | Output size depends on the algorithm (e.g., AES, RSA)   | Output is fixed size (e.g., SHA-256 always outputs 256 bits) |
| Use Cases     | Encrypting sensitive data (files, messages, etc.)       | Verifying data integrity, storing passwords                  |
| Reversibility | Reversible (decryptable with the key)                   | Irreversible (cannot be undone)                              |

---

### Sequential Execution in Python

**Sequential execution** in Python means that the program runs **line by line**, **from top to bottom**, in the **exact order** in which the statements are written—unless control flow (like conditionals or loops) changes it.

It’s the **default mode of execution** in Python and most programming languages.

---

### Async Execution in Python

**Asynchronous execution** allows a program to perform **non-blocking operations**, so it can continue doing other work **while waiting** (e.g., for I/O operations like file access, web requests, or database queries).

Instead of **waiting** for one task to finish before starting another, async execution enables **concurrent** tasks using **coroutines**.

- Key Concepts

  - `async` and `await`

    - `async def` defines an **asynchronous function** (coroutine).
    - `await` pauses execution **until** an awaitable (like another coroutine or async I/O) completes.

  - Event Loop
    - Manages and schedules coroutines.
    - Runs in a **single thread**, but switches between tasks during I/O waits.

```python
import asyncio

async def fetch_data():
    print("Start fetching...")
    await asyncio.sleep(2)  # Simulates I/O delay
    print("Done fetching!")
    return {"data": 123}

async def main():
    print("Before fetch")
    result = await fetch_data()
    print("Result:", result)

# Run the event loop
asyncio.run(main())
```

---

### Coroutine Vs. Regular function in Python

A **coroutine** is a **special function** that can be **paused** and **resumed**, allowing Python to perform **asynchronous programming** without using threads or processes.

In Python, coroutines are defined using `async def` and are executed with `await` or by scheduling them in an event loop.

| Feature       | Regular Function       | Coroutine                      |
| ------------- | ---------------------- | ------------------------------ |
| Defined with  | `def`                  | `async def`                    |
| Executes with | Direct call            | `await`, `asyncio.run()`, etc. |
| Blocking      | Yes                    | No (can pause on `await`)      |
| Return type   | Returns value directly | Returns a coroutine object     |

---
