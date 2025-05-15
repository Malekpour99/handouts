# Interview Questions

## Table of Contents
- [Interview Questions](#interview-questions)
  - [Table of Contents](#table-of-contents)
  - [Programming \& Python](#programming--python)
    - [Why python? What are its pros and cons?](#why-python-what-are-its-pros-and-cons)
    - [What is OOP?](#what-is-oop)
    - [Four Main Principles of OOP](#four-main-principles-of-oop)
      - [1. **Encapsulation**](#1-encapsulation)
      - [2. **Abstraction**](#2-abstraction)
      - [3. **Inheritance**](#3-inheritance)
      - [4. **Polymorphism**](#4-polymorphism)
    - [What are SOLID principles?](#what-are-solid-principles)
      - [**S - Single Responsibility Principle (SRP)**](#s---single-responsibility-principle-srp)
      - [**O - Open/Closed Principle (OCP)**](#o---openclosed-principle-ocp)
      - [**L - Liskov Substitution Principle (LSP)**](#l---liskov-substitution-principle-lsp)
      - [**I - Interface Segregation Principle (ISP)**](#i---interface-segregation-principle-isp)
      - [**D - Dependency Inversion Principle (DIP)**](#d---dependency-inversion-principle-dip)
    - [What is Dependency Injection?](#what-is-dependency-injection)
    - [What are different types of design patterns?](#what-are-different-types-of-design-patterns)
    - [Explain Singleton Design Pattern](#explain-singleton-design-pattern)
    - [Which SOLID Principles Does Singleton Violate?](#which-solid-principles-does-singleton-violate)
    - [Explain Factory Design Pattern](#explain-factory-design-pattern)
    - [Factory Vs. Abstract Factory Design Patterns](#factory-vs-abstract-factory-design-patterns)
    - [Explain Decorator Design Pattern](#explain-decorator-design-pattern)
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
  - [Django](#django)
    - [MVT in Django - MVT vs. MVC](#mvt-in-django---mvt-vs-mvc)
    - [Django Request-Response Lifecycle](#django-request-response-lifecycle)
  - [Database](#database)
  - [Docker \& Containerization](#docker--containerization)
  - [Network](#network)
  - [Projects](#projects)

## Programming & Python

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

### What is OOP?
**Object-Oriented Programming (OOP)** is a programming paradigm based on the concept of **"objects"**, which bundle **data (attributes)** and **behavior (methods)** together. It aims to structure software in a modular and reusable way.

OOP is used to design systems that are **scalable**, **maintainable**, and **closely modeled around real-world entities**.

---

### Four Main Principles of OOP

#### 1. **Encapsulation**
**Definition**: Encapsulation is the bundling of data and methods that operate on that data within a class, and restricting direct access to some components.

**Goal**: Hide internal state and require all interactions to occur through an object’s methods.

**Example**:
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500
# print(account.__balance) -> ❌ Raises AttributeError (encapsulation)
```

---

#### 2. **Abstraction**
**Definition**:  
Abstraction means hiding the internal implementation details and showing only the necessary parts of an object. It allows developers to work with ideas rather than specifics.

**Goal**:  
Reduce complexity by exposing only essential functionalities and hiding irrelevant details.

**Example**:
```python
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class StripeProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing ${amount} through Stripe.")

# Using abstraction
def checkout(processor: PaymentProcessor, amount):
    processor.process_payment(amount)

checkout(StripeProcessor(), 100)
# Output: Processing $100 through Stripe.
```

---

#### 3. **Inheritance**
**Definition**:
Inheritance allows a new class (child or subclass) to acquire properties and behaviors (methods) of an existing class (parent or superclass).

**Goal**:
Encourage code reuse and establish a logical hierarchy between classes.

**Example**:
```python
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

dog = Dog()
cat = Cat()

dog.speak()  # Output: Dog barks
cat.speak()  # Output: Cat meows
```

---

#### 4. **Polymorphism**

**Definition**:
Polymorphism means many forms. It allows different classes to define methods with the same name that behave differently.

**Goal**:
Write flexible code that works with objects of different types through a common interface.

**Example**:
```python
class Bird:
    def move(self):
        print("Flies in the sky")

class Fish:
    def move(self):
        print("Swims in the water")

def animal_movement(animal):
    animal.move()

bird = Bird()
fish = Fish()

animal_movement(bird)  # Output: Flies in the sky
animal_movement(fish)  # Output: Swims in the water
```

---

### What are SOLID principles?

**SOLID** is an acronym representing **five core design principles** that make software:

- More understandable
- Flexible
- Maintainable
- Scalable

|Principle | Focus                  | Goal                              |
|----------|------------------------|-----------------------------------|
|**S**ingle Responsibility Principle | Responsibility         | One class = one reason to change  |
|**O**pen/Closed Principle           | Extension              | Add behavior without changing code|
|**L**iscov Substitution Principle   | Substitutability       | Use subclass without surprises    |
|**I**nterface Segregation Principle | Interface size         | No bloated interfaces             |
|**D**ependency Inversion Principle  | Abstraction dependency | High-level code stays clean       |


#### **S - Single Responsibility Principle (SRP)**

> A class should have only one reason to change.

Every class should do **one thing** and do it well. If a class handles more than one responsibility, it becomes harder to maintain and test.

```python
class InvoicePrinter:
    def print(self, invoice):
        print(f"Printing invoice #{invoice.id}")

class InvoiceSaver:
    def save(self, invoice):
        print(f"Saving invoice #{invoice.id}")
```

#### **O - Open/Closed Principle (OCP)**

Software entities should be open for extension but closed for modification.

You should be able to add new behavior without modifying existing code.

```python
class PaymentProcessor:
    def pay(self, amount):
        raise NotImplementedError

class PayPal(PaymentProcessor):
    def pay(self, amount):
        print(f"Paid ${amount} via PayPal")

class Stripe(PaymentProcessor):
    def pay(self, amount):
        print(f"Paid ${amount} via Stripe")
```

#### **L - Liskov Substitution Principle (LSP)**

Subclasses should be replaceable for their base class without breaking the application.

If B is a subclass of A, then we should be able to use B anywhere we use A and expect it to behave correctly.

```python
class Bird:
    def fly(self):
        pass

class Sparrow(Bird):
    def fly(self):
        print("Sparrow flying")

class Ostrich(Bird):
    def fly(self):
        raise Exception("Ostriches can't fly")  # ❌ Violates LSP
# Fix: Separate behaviors into interfaces (or base classes).
```

#### **I - Interface Segregation Principle (ISP)**

Clients should not be forced to depend on methods they do not use.

Avoid bloated interfaces. Instead, use multiple, smaller, specific interfaces.

```python
class Printable:
    def print(self):
        pass

class Scannable:
    def scan(self):
        pass

class Printer(Printable):
    def print(self):
        print("Printing...")

class Scanner(Scannable):
    def scan(self):
        print("Scanning...")
```

#### **D - Dependency Inversion Principle (DIP)**

High-level modules should not depend on low-level modules. Both should depend on abstractions.

Depend on interfaces or abstract classes, not concrete implementations.

```python
class NotificationService:
    def __init__(self, sender):
        self.sender = sender

    def send(self, message):
        self.sender.send(message)

class EmailSender:
    def send(self, message):
        print(f"Email: {message}")

# Inject EmailSender (low-level) into NotificationService (high-level)
notifier = NotificationService(EmailSender())
notifier.send("Hello")
```

---

### What is Dependency Injection?

**Dependency Injection (DI)** is a **design pattern** in which an object receives (or is "injected" with) its dependencies **from the outside**, rather than creating them itself. which

- Promotes **loose coupling**
- Increases **testability**
- Improves **modularity**
- Makes code more **maintainable and reusable**

```python
# Without DI:
class EmailService:
    def send(self, to, message):
        print(f"Sending email to {to}: {message}")

class UserNotifier:
    def __init__(self):
        self.email_service = EmailService()  # tightly coupled

    def notify(self, user):
        self.email_service.send(user, "Welcome!")

# With DI:
class UserNotifier:
    def __init__(self, service):
        self.service = service  # injected from outside

    def notify(self, user):
        self.service.send(user, "Welcome!")

# Inject dependency
email_service = EmailService()
notifier = UserNotifier(email_service)
```

---

### What are different types of design patterns?
**Design patterns** are reusable solutions to common problems in software design. They represent best practices refined over time by experienced developers.

|Category   | Purpose                            | Example Patterns                   |
|-----------|------------------------------------|------------------------------------|
|Creational | Object creation logic              | Singleton, Factory, Abstract Factory,  Builder, Prototype        |
|Structural | Object composition and flexibility | Adapter, Decorator, Proxy, Facade, Composite, Bridge, Flyweight  |
|Behavioral | Communication & responsibility     | Observer, Strategy, Command, State, Chain of Responsibility, Template Method, Visitor, Interpreter, Iterator |

---

### Explain Singleton Design Pattern

The **Singleton pattern** ensures that a **class has only one instance** throughout the lifetime of an application and provides a **global point of access** to that instance.

Use cases:
- When exactly **one object** is needed to coordinate actions across the system.
- Useful for things like:
  - Database connections
  - Logging services
  - Configuration managers
  - Caching layers

---

```python
# Magic method implementation
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

# Usage
a = Singleton()
b = Singleton()

print(a is b)  # Output: True

# Decorator implementation
def singleton(cls):
    _instances = {}

    def get_instance(*args, **kwargs):
        if cls not in _instances:
            _instances[cls] = cls(*args, **kwargs)
        return _instances[cls]

    return get_instance

@singleton
class Config:
    def __init__(self):
        self.settings = {"debug": True}

config1 = Config()
config2 = Config()

print(config1 is config2)  # Output: True
```

---

### Which SOLID Principles Does Singleton Violate?

The **Singleton Pattern** ensures that a class has **only one instance** and provides a global point of access to it.

While this sounds helpful, it can **violate** multiple **SOLID principles**:
1. Single Responsibility Principle (SRP)
   - A Singleton class often has **two responsibilities**:
      1. **Core logic** (e.g., logging or config management)
      2. **Controlling its own instantiation**

      This mixes object logic with lifecycle management, making it harder to maintain and extend.

2. Open/Closed Principle (OCP)
   - Singleton tightly controls its instantiation and usage.
   - You **cannot extend** the behavior easily (e.g., switching to a mock or subclass requires modifying internal logic or breaking the pattern).

3. Dependency Inversion Principle (DIP)
   - Instead of **injecting dependencies**, classes often **directly call** the Singleton:
    ```python
    Logger.get_instance().log("error")  # tightly coupled
    ```

---

### Explain Factory Design Pattern

The **Factory Pattern** is a **creational design pattern** that provides an **interface for creating objects** in a superclass, but **allows subclasses to alter the type of objects** that will be created.
Instead of calling a class constructor directly, you use a **factory method** to get the instance.

```python
class Notification:
    def notify(self, message):
        raise NotImplementedError

class EmailNotification(Notification):
    def notify(self, message):
        print(f"Email: {message}")

class SMSNotification(Notification):
    def notify(self, message):
        print(f"SMS: {message}")

# Without Factory
notif = EmailNotification()  # tightly coupled to a concrete class
notif.notify("Hello!")

# With Factory
class NotificationFactory:
    @staticmethod
    def get_notification(method: str) -> Notification:
        if method == "email":
            return EmailNotification()
        elif method == "sms":
            return SMSNotification()
        else:
            raise ValueError("Unsupported notification method")


notif = NotificationFactory.get_notification("email")
notif.notify("Factory pattern in action!")
```

---

### Factory Vs. Abstract Factory Design Patterns

Both **Factory** and **Abstract Factory** are **creational design patterns**, but they solve different levels of object creation problems.

- Factory Method Pattern
  - Creates **one type of object** based on some input.
  - Used when the exact type of the object isn't known until runtime.
  - Example:
    ```python
    class Button:
        def click(self):
            raise NotImplementedError

    class WindowsButton(Button):
        def click(self):
            print("Windows button clicked!")

    class MacButton(Button):
        def click(self):
            print("Mac button clicked!")

    class ButtonFactory:
        @staticmethod
        def create_button(os_type):
            if os_type == "windows":
                return WindowsButton()
            elif os_type == "mac":
                return MacButton()
    ```

- Abstract Factory Pattern
  - Creates **families of related or dependent objects**.
  - Used when there are multiple products that need to work together.
  - Example:
    ```python
    # --- Abstract products
    class Button:
        def click(self): pass

    class Checkbox:
        def check(self): pass

    # --- Concrete products
    class WindowsButton(Button):
        def click(self):
            print("Windows Button")

    class WindowsCheckbox(Checkbox):
        def check(self):
            print("Windows Checkbox")

    class MacButton(Button):
        def click(self):
            print("Mac Button")

    class MacCheckbox(Checkbox):
        def check(self):
            print("Mac Checkbox")

    # --- Abstract Factory
    class GUIFactory:
        def create_button(self): pass
        def create_checkbox(self): pass

    # --- Concrete Factories
    class WindowsFactory(GUIFactory):
        def create_button(self):
            return WindowsButton()
        def create_checkbox(self):
            return WindowsCheckbox()

    class MacFactory(GUIFactory):
        def create_button(self):
            return MacButton()
        def create_checkbox(self):
            return MacCheckbox()

    # --- Client
    def render_gui(factory: GUIFactory):
        button = factory.create_button()
        checkbox = factory.create_checkbox()
        button.click()
        checkbox.check()

    # Use:
    factory = WindowsFactory()
    render_gui(factory)
    ```

---

### Explain Decorator Design Pattern

The **Decorator Pattern** is a **structural design pattern** that lets you **dynamically add behavior** or responsibilities to an object **without modifying its original code** (by wrapping around it).
It's often used to **extend functionality** in a flexible and reusable way.

```python
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
        print(f"{func.__name__} Finished")
    return wrapper

@log_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Calling say_hello
# Hello!
# say_hello Finished
```

---

### List Vs. Tuple

|Feature          | List   | Tuple |
|-----------------|--------|-------|
|Mutable          | Yes    | No    |
|Ordered          | Yes    | Yes   |
|Indexable        | Yes    | Yes   |
|Use as Dict Key  | No     | Yes   |
|Iteration Speed  | Slower | Faster|
|Memory Efficient | Less   | More  |

---

### Instance Method VS. Class Method Vs. Static Method

|Feature          | Instance Method   | Class Method | Static Method |
|-----------------|-------------------|--------------|---------------|
|Decorator        | (none)            | @classmethod | @staticmethod |
|First parameter  | self (instance)   | cls (class)  | No default first arg |
|Access instance? | Yes               | No           | No |
|Access class?    | Via self.class    | Yes          | No |
|Use case         | Instance behavior | Factory methods, alter class state | Utility/helper function |

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

|Feature | Iterator | Generator |
|--------|----------|-----------|
|Definition | Object with __iter__() and __next__() | Uses yield in a function |
|Creation | Manually (class + methods) | Using generator function or expression |
|Memory Usage | Depends on implementation | Memory-efficient (lazy eval) |
|Infinite Sequences | Yes | Yes |
|Syntax | More boilerplate | Simple, clean syntax |
|Performance | Slightly slower (custom classes) | Faster for large/lazy sequences |
|State Management | Manual | Automatic (via yield) |

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

|Feature | Mutable Objects | Immutable Objects |
|--------|-----------------|-------------------|
|Modification | Can be changed after creation | Cannot be changed after creation |
|Examples | ```list, dict, set, bytearray``` | ```int, str, tuple, frozenset``` |
|Hashability | Not hashable (cannot be used as dictionary keys) | Hashable (can be used as dictionary keys) |
|Efficiency | Typically more efficient for modifications | May require creating new objects for modifications |
|Memory | Same object in memory is modified | A new object is created for each modification |

---

### Encryption Vs. Hashing

|Feature | Encryption | Hashing |
|--------|------------|---------|
|Direction | Bi-directional (can decrypt to get original data) | One-way (cannot retrieve original data) |
|Purpose | Confidentiality (protect data from unauthorized access) | Integrity (verify data hasn't been tampered with) |
|Key | Requires a key for encryption and decryption | No key needed, only the hash function is used |
|Output Size | Output size depends on the algorithm (e.g., AES, RSA) | Output is fixed size (e.g., SHA-256 always outputs 256 bits) |
|Use Cases | Encrypting sensitive data (files, messages, etc.) | Verifying data integrity, storing passwords |
|Reversibility | Reversible (decryptable with the key) | Irreversible (cannot be undone) |

---



## Django

### MVT in Django - MVT vs. MVC

**MVC** stands for **Model-View-Controller**. It's a software design pattern used for developing user interfaces.

**MVT** stands for **Model-View-Template**, and it's Django's variant of the MVC architecture.

- **Model**:
  - Defines the data structure.
  - Interacts with the database.
  - Written in `models.py`.

- **View**:
  - Contains the business logic. (Better to decouple business logic using **services**)
  - Fetches data from the model and sends it to the template.
  - Written in `views.py`.

- **Template**:
  - Handles the presentation layer (HTML, CSS).
  - Receives data from the view and renders the final page.

| Concept        | MVC                        | Django (MVT)                |
|----------------|-----------------------------|-----------------------------|
| **Model**      | Manages the data and logic  | Same                        |
| **View**       | Handles presentation/UI     | Called a **Template** in Django |
| **Controller** | Handles user input and updates model/view | **View** in Django (handles logic) |
| **Template**   | Optional layer              | Explicit layer for HTML rendering |

User -> Controller -> Model -> View -> User

User -> Django (Controller) -> View -> Model -> Template -> User

---

### Django Request-Response Lifecycle

**Browser -> WSGI/ASGI Server (e.g., Gunicorn, Uvicorn) -> Django Middleware (Request Phase) -> URL Dispatcher (urls.py) -> View (views.py) -> Models (if needed) -> Templates (if needed) -> Django Middleware (Response Phase) -> WSGI/ASGI Server -> Browser (Rendered Response)**

**- Browser Sends a Request**
  - A user initiates an HTTP request by entering a URL or submitting a form.
  - This request is received by Django's WSGI-compatible web server (e.g., Gunicorn, uWSGI).

**- WSGI/ASGI Server Passes Request to Django**
  - The WSGI/ASGI server passes the request to Django via a callable interface defined in `wsgi.py` or `asgi.py`.
  - Django initializes necessary components to handle the request.

**- Middleware Processing (Request Phase)**
  - The request passes through **middleware** defined in `MIDDLEWARE` setting.
  - Middleware are Python classes that WWcan:
    - Modify the request.
    - Block the request.
    - Add metadata.
    - Perform authentication or logging.

**- URL Routing**
  - Django uses urls.py to match the request path with a corresponding view function.
  - It checks from top to bottom until it finds a match using path() or re_path().

**- View Execution**
  - The matched view function or class-based view (CBV) is called.
  - This view:
    - May fetch data from the model.
    - Passes data to a template.
    - Returns an HttpResponse object.

**- Template Rendering (Optional)**
  - If the view uses render(), Django:
    - Loads the template (.html file).
    - Renders it with the context data.
    - Produces HTML output.

**- Middleware Processing (Response Phase)**
  - Before the final response is returned to the browser, it passes back through middleware (in reverse order).
  - Middleware can:
    - Modify the response.
    - Add headers.
    - Compress or encrypt content.

**- Response Sent to Client**
  - Django returns the final Response object (HTML, JSON, file, etc.).
  - The WSGI/ASGI server sends it back to the client (browser or API consumer).

---

## Database

## Docker & Containerization

## Network

## Projects