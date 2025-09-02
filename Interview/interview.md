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
    - [Sequential Execution in Python](#sequential-execution-in-python)
    - [Async Execution in Python](#async-execution-in-python)
    - [Coroutine Vs. Regular function in Python](#coroutine-vs-regular-function-in-python)
  - [Backend](#backend)
    - [Authentication Vs. Authorization](#authentication-vs-authorization)
    - [Stateful Vs. Stateless](#stateful-vs-stateless)
    - [MVT in Django - MVT vs. MVC](#mvt-in-django---mvt-vs-mvc)
    - [Django Request-Response Lifecycle](#django-request-response-lifecycle)
    - [N + 1 Problem](#n--1-problem)
    - [Select-Related \& Prefetch-Related in Django](#select-related--prefetch-related-in-django)
    - [When would you prefer prefetch_related over select_related, even if a JOIN is possible?](#when-would-you-prefer-prefetch_related-over-select_related-even-if-a-join-is-possible)
  - [Database](#database)
    - [CAP Theorem (Brewer's theorem)](#cap-theorem-brewers-theorem)
    - [Trade-offs (CA, CP, AP)](#trade-offs-ca-cp-ap)
    - [ACID](#acid)
    - [BASE](#base)
    - [ACID Vs. BASE](#acid-vs-base)
    - [Choosing a Database](#choosing-a-database)
    - [Isolation Levels](#isolation-levels)
    - [Primary Indexing Vs. Secondary Indexing](#primary-indexing-vs-secondary-indexing)
  - [Docker \& Containerization](#docker--containerization)
    - [Image Vs. Container](#image-vs-container)
    - [Custom Image (Dockerfile) Best Practices](#custom-image-dockerfile-best-practices)
    - [Multi-Staging](#multi-staging)
    - [CMD Vs. RUN](#cmd-vs-run)
    - [Entrypoint](#entrypoint)
    - [Docker Vs. VM](#docker-vs-vm)
    - [How Docker Containers Are Isolated from Each Other?](#how-docker-containers-are-isolated-from-each-other)
  - [Git](#git)
    - [What does actually a git commit stores in itself?](#what-does-actually-a-git-commit-stores-in-itself)
    - [Merge Vs. Rebase](#merge-vs-rebase)
    - [Cherry-Pick](#cherry-pick)
  - [Network](#network)
    - [TCP Vs. UDP](#tcp-vs-udp)
    - [3-Way Handshake](#3-way-handshake)
    - [4-Way Handshake](#4-way-handshake)
    - [TLS Handshake](#tls-handshake)
    - [What happens when you type-in "www.google.com" in your browser?](#what-happens-when-you-type-in-wwwgooglecom-in-your-browser)
    - [HTTP Request Methods](#http-request-methods)
  - [Algorithms \& Data-structures](#algorithms--data-structures)
  - [Design Systems](#design-systems)
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

| Principle                           | Focus                  | Goal                               |
| ----------------------------------- | ---------------------- | ---------------------------------- |
| **S**ingle Responsibility Principle | Responsibility         | One class = one reason to change   |
| **O**pen/Closed Principle           | Extension              | Add behavior without changing code |
| **L**iscov Substitution Principle   | Substitutability       | Use subclass without surprises     |
| **I**nterface Segregation Principle | Interface size         | No bloated interfaces              |
| **D**ependency Inversion Principle  | Abstraction dependency | High-level code stays clean        |

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

| Category   | Purpose                            | Example Patterns                                                                                             |
| ---------- | ---------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| Creational | Object creation logic              | Singleton, Factory, Abstract Factory, Builder, Prototype                                                     |
| Structural | Object composition and flexibility | Adapter, Decorator, Proxy, Facade, Composite, Bridge, Flyweight                                              |
| Behavioral | Communication & responsibility     | Observer, Strategy, Command, State, Chain of Responsibility, Template Method, Visitor, Interpreter, Iterator |

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

## Backend

### Authentication Vs. Authorization

**Authentication**: The process of verifying who the user is. It’s about **identity verification**.

**Authorization**: The process of verifying what the authenticated user can do. It’s about **permissions and access control**. Usually happens after authentication.

### Stateful Vs. Stateless

| Aspect            | Stateless                           | Stateful                                       |
| ----------------- | ----------------------------------- | ---------------------------------------------- |
| **Server Memory** | Doesn’t store client state          | Stores client state (sessions, context)        |
| **Scaling**       | Easy (any server can serve request) | Harder (needs sticky sessions or shared state) |
| **Failure**       | Recover easily (no session loss)    | Session loss if server crashes                 |
| **Example**       | REST API, DNS, HTTP itself          | WebSockets, FTP, server-side sessions          |

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

| Concept        | MVC                                       | Django (MVT)                       |
| -------------- | ----------------------------------------- | ---------------------------------- |
| **Model**      | Manages the data and logic                | Same                               |
| **View**       | Handles presentation/UI                   | Called a **Template** in Django    |
| **Controller** | Handles user input and updates model/view | **View** in Django (handles logic) |
| **Template**   | Optional layer                            | Explicit layer for HTML rendering  |

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

### N + 1 Problem

The N+1 problem happens when you run 1 query to fetch a list of records (N records), and then for each record, you run an additional query to fetch related data.

- Total queries = 1 (initial fetch) + N (per record) = N+1 queries.
- This quickly becomes inefficient at scale, especially with large datasets.

In Django

- Use `select_related` for **one-to-one** or **foreign key** relationships.
- Use `prefetch_related` for **many-to-many** or **reverse** relationships.

In Go (GORM)

- Use **eager loading** (`Preload`).

### Select-Related & Prefetch-Related in Django

`select_related` in Django:

- Purpose: Optimizes access to single-valued relationships (ForeignKey, OneToOneField).
- Mechanism: Generates a **SQL JOIN** to fetch related objects in the same query.
- Type of JOIN: Django uses **INNER JOIN** by default, but it switches to **LEFT OUTER JOIN** if the relation is **nullable** (so you don’t lose rows when the related object doesn’t exist).

`prefetch_related` in Django

- Purpose: Optimizes access to multi-valued relationships (reverse foreign key, many-to-many).
- Mechanism: Executes two separate queries and then does the **“join” in Python**, not SQL.
  - Query 1: Fetch base objects.
  - Query 2: Fetch related objects with an IN (...) filter.
- Type of JOIN: None at SQL level (Django does a “manual join” in memory).

### When would you prefer prefetch_related over select_related, even if a JOIN is possible?

1. Risk of Row Explosion

   - If I use select_related (JOIN), the result set size can blow up when one parent has many children.
   - Example: A User with 10,000 Posts.
   - select_related with a JOIN → returns 10,000 rows for 1 user, duplicating user fields in each row.
   - That wastes network bandwidth, memory, and ORM processing time.

   - prefetch_related avoids this by fetching:
   - 1 row for the user
   - 10,000 rows for posts (separate query)
   - Then Django associates them in Python.

2. Better Query Planner Performance

   - A huge JOIN with multiple relations can confuse the database’s query planner, leading to slow execution.
   - With prefetch_related, you keep queries simpler (SELECT ... WHERE id IN (...)) and let Django’s Python layer do the merge.
   - This is often faster in real-world apps where relations are 1-to-many or many-to-many.

3. Memory Efficiency in Python

   - With JOINs (select_related), Django has to hydrate a model instance per duplicate row — even though most fields are identical.
   - With prefetch_related, the base objects (User) are hydrated once, and the children (Posts) are hydrated separately and attached.

4. Database Load Balancing

   - In some setups (read replicas, sharded DBs), it’s useful to keep queries smaller and more cache-friendly.
   - prefetch_related queries (WHERE ... IN (...)) can be batched or routed independently, while a giant JOIN can’t.

## Database

### CAP Theorem (Brewer's theorem)

In a distributed database/system, you cannot simultaneously guarantee all three of these properties:

- **Consistency (C)**

  - Every read gets the most recent write (all nodes see the same data at the same time).
  - Example: If I write X=10, any read immediately after should return 10.

- **Availability (A)**

  - Every request receives a response, even if it might not be the latest version of the data.
  - System stays responsive even under failure.

- **Partition Tolerance (P)**

  - The system continues to function despite network partitions (nodes not being able to communicate).

CAP theorem says:
In the presence of a **network partition**, you must choose between **Consistency** and **Availability**.

### Trade-offs (CA, CP, AP)

- **CP (Consistency + Partition tolerance)**

  - Sacrifice availability during network failures.
  - Strongly consistent systems. (e.g. Banking Systems)
  - Example: HBase, MongoDB (with strong consistency configs).

- **AP (Availability + Partition tolerance)**

  - Sacrifice strict consistency → eventual consistency is allowed.
  - Prioritize always responding, even if data might be stale. (e.g. Social Media Feeds)
  - Example: Cassandra, DynamoDB.

- **CA (Consistency + Availability)**

  - Theoretically possible only if no network partitions exist → not practical in distributed systems.
  - Example: traditional single-node RDBMS (like PostgreSQL on one machine).

### ACID

`ACID` is a set of properties that guarantee reliable transactions in databases (especially relational ones like PostgreSQL, MySQL, Oracle).

1. **Atomicity**

   - "All or nothing."
   - A transaction is indivisible: either all operations succeed, or none do.
   - Example: In a money transfer:
     - Deduct $100 from Alice
     - Add $100 to Bob
     - If adding fails, the deduction is rolled back.

2. **Consistency**

   - Transactions bring the database from one valid state to another valid state, following all rules, constraints, and triggers.
   - Example: If a column must be unique, inserting a duplicate violates consistency → transaction fails.

3. **Isolation**

   - Concurrent transactions should not interfere with each other.
   - Intermediate states are not visible to other transactions.
   - Different isolation levels exist:
     - Read Uncommitted (dirty reads allowed)
     - Read Committed
     - Repeatable Read
     - Serializable (highest, behaves like transactions are sequential).

4. **Durability**

   - Once a transaction is committed, it is permanent, even if the system crashes right after.
   - Achieved via **write-ahead logs (WALs)**, **replication**, and **persistent storage**.

### BASE

Many NoSQL databases (Cassandra, DynamoDB, CouchDB, etc.) follow the BASE model to favor scalability and availability in distributed systems.

1. **Basically Available**

- The system guarantees availability, but not necessarily consistency at all times.
- Even under failure, it tries to respond — possibly with stale data.
- Example: Amazon DynamoDB or Cassandra nodes may return older values instead of failing.

2. **Soft State**

- The system state may change over time, even without input.
- Because of replication and eventual consistency, different nodes may temporarily hold different values.
- Example: A write to one replica may not immediately be visible on another.

3. **Eventual Consistency**

- Given enough time (assuming no new updates), all replicas will converge to the same state.
- Strong consistency is sacrificed for performance and fault tolerance.
- Example: In Cassandra, a read might not show the latest write, but eventually all nodes sync up.

### ACID Vs. BASE

| Property     | **ACID**                                                    | **BASE**                                                                    |
| ------------ | ----------------------------------------------------------- | --------------------------------------------------------------------------- |
| Consistency  | Strong consistency                                          | Eventual consistency                                                        |
| Availability | Can sacrifice availability (during conflicts or partitions) | Prioritizes availability                                                    |
| Use Case     | Banking, reservations, systems needing strong guarantees    | Large-scale distributed systems, social media, e-commerce with huge traffic |

### Choosing a Database

1. **Data Model & Structure**

- If data is highly relational with complex joins, foreign keys, and transactions → a Relational DB (PostgreSQL, MySQL, Oracle) makes sense.
- If data is document-oriented, hierarchical, or schema-flexible (e.g., product catalogs, JSON-like structures) → a Document Store (MongoDB, Couchbase) is better.
- If workload is time-series (metrics, IoT, monitoring) → use a Time-Series DB (InfluxDB, TimescaleDB).
- If workload is graph-like (social networks, recommendation engines) → a Graph DB (Neo4j, ArangoDB) fits best.

2. **Consistency vs Availability (CAP theorem)**

- If the system needs strict correctness (e.g., financial transactions) → choose a strongly consistent ACID DB (PostgreSQL, MySQL, Oracle).
- If the system prioritizes high availability and scale (e.g., social feeds, analytics) → a BASE / eventually consistent DB (Cassandra, DynamoDB) is more suitable.

3. **Scalability Requirements**

- For a single-region, moderate traffic system → vertical scaling with a relational DB works well.
- For globally distributed, high-traffic apps → need a horizontally scalable DB like Cassandra, DynamoDB, or CockroachDB.

4. **Query Patterns & Access Needs (Read/Write Heavy)**

- Do we need ad-hoc queries, aggregations, joins? → SQL databases shine.
- Do we mostly fetch by key/value lookups? → Key-Value stores (Redis, DynamoDB).
- Do we need real-time analytics? → Columnar DBs (ClickHouse, BigQuery).

5. **Transaction Requirements**

- Strong transactional integrity (ACID) → SQL DBs (Postgres, MySQL).
- Eventual consistency is okay (shopping cart, likes, logs) → NoSQL (MongoDB, Cassandra).

6. **Ecosystem, Tooling & Operational Overhead**

- Does the team have experience with SQL or NoSQL?
- Is there cloud-native support (AWS RDS, DynamoDB, GCP Spanner)?
- Do we need easy migrations, backups, replication?

- **Example**

  - Banking system / Payment gateway → PostgreSQL (ACID, strong consistency).
  - Social media feed → Cassandra / DynamoDB (BASE, high availability).
  - Product catalog with flexible schema → MongoDB.
  - Analytics dashboard → ClickHouse or BigQuery.
  - Cache / Session store → Redis.

### Isolation Levels

Concurrency Anomalies to Know:

- **Dirty Read** – A transaction reads uncommitted data from another transaction.
- **Non-Repeatable Read** – A transaction reads the same row twice and gets different results (because another transaction updated it in between).
- **Phantom Read** – A transaction re-runs a query (e.g., SELECT ... WHERE condition) and new rows appear/disappear (because another transaction inserted/deleted rows).

- **Read Uncommitted (Lowest level)**

  - ✅ Allows dirty reads.
  - Transactions can see uncommitted changes from others.
  - Rarely used in practice (can lead to inconsistent states).
  - Example use: analytics queries where stale data is acceptable.

- **Read Committed**

  - 🚫 Prevents dirty reads.
  - Each read sees only committed data.
  - But still allows non-repeatable reads and phantoms.
  - This is the default in PostgreSQL & Oracle.

- **Repeatable Read**

  - 🚫 Prevents dirty reads and non-repeatable reads.
  - Guarantees that if you read a row twice in the same transaction, it won’t change.
  - Still allows phantom reads (new rows might appear that match the query condition).
  - This is the default in MySQL (InnoDB).

- **Serializable (Highest level)**

  - 🚫 Prevents all three anomalies (dirty, non-repeatable, phantom).
  - Transactions are executed as if they were serial (one after another).
  - Strongest guarantee but lowest concurrency (can cause locking/contention).
  - Best for financial apps requiring correctness over performance.

| Isolation Level  | Dirty Read | Non-Repeatable Read | Phantom Read |
| ---------------- | ---------- | ------------------- | ------------ |
| Read Uncommitted | ✅ Allowed | ✅ Allowed          | ✅ Allowed   |
| Read Committed   | ❌ No      | ✅ Allowed          | ✅ Allowed   |
| Repeatable Read  | ❌ No      | ❌ No               | ✅ Allowed   |
| Serializable     | ❌ No      | ❌ No               | ❌ No        |

### Primary Indexing Vs. Secondary Indexing

- **Primary Index**

  - Built on the primary key (or clustering key) of a table.
  - The data file itself is ordered by this key (clustered index).
  - Each table can have only one primary index.
  - Lookup is very fast because the index order matches the physical storage order.

- **Secondary Index**

  - Built on non-primary key attributes (non-clustering key).
  - The data file is not ordered by this key.
  - A table can have multiple secondary indexes.
  - Provides fast lookups on attributes other than the primary key.
  - Usually implemented with an extra pointer (row ID / primary key reference) that links back to the actual row.Think of it as an extra search table that helps find rows quickly without scanning everything.
  - too many secondary indexes slow down writes (since every insert/update must update all relevant indexes).

| Feature             | Primary Index                         | Secondary Index                        |
| ------------------- | ------------------------------------- | -------------------------------------- |
| **Key Type**        | Built on primary key / clustering key | Built on non-primary key columns       |
| **Ordering**        | Data stored in order of index         | Data not stored in index order         |
| **Count per Table** | Only one                              | Many allowed                           |
| **Access Method**   | Direct, since data is aligned         | Needs extra lookup (to row/primary)    |
| **Performance**     | Faster for key-based searches         | Slight overhead (extra pointer lookup) |

## Docker & Containerization

### Image Vs. Container

- **Docker Image**

  - Think of it as a blueprint (or template).
  - It’s a read-only snapshot that contains everything needed to run an application: code, dependencies, libraries, environment variables, and configs.
  - Images are built in layers (each instruction in a Dockerfile creates a new layer).
  - They are immutable — once built, they don’t change.

- **Docker Container**

  - A running instance of an image.
  - Containers are mutable at runtime: they can write to their filesystem (a writable layer is added on top of the image).
  - Multiple containers can be created from the same image, each isolated with its own process space, networking, and storage.
  - Containers can be started, stopped, restarted, or destroyed without affecting the original image.

### Custom Image (Dockerfile) Best Practices

- Use official images or minimal base images (Prefer _language-specific_ base images)
- Use multi-stage builds (reduce image size by separating build and runtime environments)
- Document exposed ports and metadata (e.g. maintainer, version, etc.)
- Use Environment Variables (`ENV`) instead of hardcoding paths or other variables.
- Set WORKDIR instead of cd (use WORKDIR to define working directory; it’s clearer and Docker-layer aware)
- Install only what's necessary and combine RUN commands to reduce layers
- Clean up temporary files (remove caches and temp files after installing packages)
- Use non-root user (improves security by preventing privilege escalation in case of a container exploit)
- Minimize COPY scope using docker ignore (only copy what’s needed, use `.dockerignore` to skip unnecessary files e.g. node_modules, .git, etc.)
- Use ENTRYPOINT + CMD properly (ENTRYPOINT defines the fixed command; CMD defines default args -can be overridden-)
- Use specific tag for each image which shows file-version (e.g. _jenkins:2.1.4_)
- Use Linters for assessing Dockerfiles ([`hadolint`](https://github.com/hadolint/hadolint))
- Add HEALTHCHECK (helps detect if the app inside the container is working correctly)
- Limit containers processes during creation (use constraints like _CPU_ and _memory_ limits and _control group (cgroup)_ configurations)
- Analyze docker image layers ([`dive`](https://github.com/wagoodman/dive))

### Multi-Staging

Multi-staging allows you to separate the build environment (where you compile or bundle your app) from the runtime environment (where you actually run it).

- Compile/build in one stage (with all the heavy tooling).
- Copy only the final artifacts into a minimal base image.
- Keep the final runtime image lean and secure.

- **Benefits**

  - Smaller images → Faster pulls, less attack surface.
  - Cleaner Dockerfiles → You don’t need separate build scripts.
  - Security → No leftover compilers or secrets in the runtime image.
  - Flexibility → You can have multiple build stages for testing, linting, or packaging.

### CMD Vs. RUN

- `RUN`

  - Purpose: Executes a command at build time.
  - Used for: Installing software, modifying the image filesystem, etc.
  - Effect: The result becomes part of the final image layer.

- `CMD`

  - Purpose: Specifies the default command to run when a container starts (runtime).
  - Used for: Defining what the container should do by default.
  - Effect: Does not affect the image during build.

### Entrypoint

`ENTRYPOINT` defines the main command that will always run when a container starts.
It makes the container behave like an executable.
Unlike `CMD`, which is more of a “default argument”, `ENTRYPOINT` is the fixed command — arguments from `docker run` are passed to it.

- `ENTRYPOINT` -> fixed program.
- `CMD` -> default arguments to that program (but can be _overridden_ at runtime).

### Docker Vs. VM

1. Architecture

- VMs

  - Run a full operating system (guest OS) on top of a **hypervisor** (like VMware, VirtualBox, KVM).
  - Each VM includes its own kernel + system libraries + application.
  - Heavyweight: more resource overhead.

- Docker (containers)

  - Run on the **host OS kernel** (no guest OS).
  - Containers share the host kernel but isolate processes, filesystems, and networking using Linux namespaces & cgroups.
  - Lightweight: no need to boot a full OS.

2. Startup Time

- VMs: Minutes (booting an OS).
- Containers: Seconds or less (just starting processes).

3. Resource Usage

- VMs: Require dedicated CPU, memory, and disk. Duplicates OS overhead. (dedicated resources are not shared, even if they are not used!)
- Containers: Share resources dynamically; many more containers can run on the same host.

4. Portability

- VMs: Images are big (GBs), less portable.
- Containers: Images are layered and small (MBs), easy to move and deploy.

5. Isolation & Security

- VMs: Strong isolation — each VM has its own kernel. Good for untrusted workloads.
- Containers: Weaker isolation — all containers share the host kernel. Security depends on kernel hardening, namespaces, SELinux/AppArmor.

6. Use Cases

- VMs: Best for running multiple OS types on the same host (e.g., Linux + Windows). Good when strong isolation is needed.
- Containers (Docker): Best for microservices, CI/CD pipelines, cloud-native apps, fast scaling.

### How Docker Containers Are Isolated from Each Other?

1. Namespaces (provide isolation of resources)

Namespaces create the illusion that each container has its own dedicated system.

- **PID namespace** → Each container has its own process tree (can’t see or affect host/other containers’ processes).
- **NET namespace** → Each container has its own network stack (interfaces, IPs, routing tables, ports).
- **MNT namespace** → Separate filesystem view (different root FS, mounts).
- **UTS namespace** → Each container can have its own hostname & domain name.
- **IPC namespace** → Isolates inter-process communication (shared memory, semaphores, message queues).
- **User namespace** → Maps container users to different host users (can make root inside container map to unprivileged UID on host).

2. Control Groups (cgroups) (provide resource limits)

- Limit and monitor resources: CPU, memory, I/O, network bandwidth.
- Prevents one container from starving others.
- Example: You can cap a container to 512MB RAM and 1 CPU core.

3. Union File Systems (OverlayFS, AUFS, etc.)

- Each container gets its own **filesystem layer**.
- **Copy-on-write** ensures containers can modify files without affecting the base image or other containers.

4. Capabilities & Seccomp

- By default, containers drop many Linux capabilities (like loading kernel modules).
- `Seccomp` (secure computing mode) filters syscalls to restrict what a containerized process can do.

5. Security Modules

- Tools like `AppArmor` and `SELinux` add mandatory access control policies to restrict container actions beyond namespaces/cgroups.

## Git

### What does actually a git commit stores in itself?

A Git commit **_stores a snapshot of the entire working tree_**, not just the changes.

However, Git optimizes storage by:

- Storing the full snapshot only for the first commit.
- For subsequent commits, Git stores the snapshot as a set of differences (deltas) internally to save space — but conceptually, **each commit represents a full snapshot** of your project at that point in time.

1. Tree Object (Snapshot)

   Points to a tree object, which represents the directory structure and content (blobs) of the project at the time of the commit.
   This tree is what contains the actual files and folders (via SHA-1/SHA-256 hashes).

2. Parent Commits

   Points to one (or more) parent commits:

   - A normal commit has 1 parent.
   - The first commit has no parent.
   - A merge commit has 2 or more parents.

3. Author Information

   Includes the name and email of the person who originally wrote the changes.
   Also includes a timestamp (with timezone).

4. Committer Information

   Includes the name and email of the person who made the commit.
   Usually the same as the author, but can differ (e.g., if someone else applies your patch).
   Also includes a timestamp.

5. Commit Message

   A human-readable message describing what the commit does.
   Often includes details on what changed and why.

6. Commit Hash

   A SHA-1 or SHA-256 hash of the commit content (including metadata and tree).
   This hash uniquely identifies the commit and changes if any part of the commit changes.

7. Optional: GPG Signature

   A commit may be signed with a GPG key to verify its authenticity.

### Merge Vs. Rebase

`git merge`

- Combines changes from one branch into another by creating a new merge commit (unless _fast-forward_ is possible).
- Preserves the exact history of both branches.
- **Fast-forward merge**
  - Happens when the target branch has not diverged.
  - Git just moves the pointer forward — no new commit is created.
- **No fast-forward merge**
  - Happens when both branches have diverged.
  - Git creates a merge commit to tie them together.

`git rebase`

- Moves (or "replays") the commits from one branch on top of another branch, rewriting history.
- Commits are recreated with new hashes.

### Cherry-Pick

`git cherry-pick` lets you apply a specific commit (or set of commits) from one branch onto another branch, **without merging** the whole branch.
It takes the changes introduced by that commit and **creates a new commit** on top of your current branch.

- Usage:
  - **Hotfixes** → Apply a critical bug fix from a feature branch to main immediately.
  - **Backporting** → Apply a patch to an older release branch.
  - **Selective integration** → You want only one commit, not a whole merge.

## Network

### TCP Vs. UDP

**TCP (Transmission Control Protocol)** and **UDP (User Datagram Protocol)** are both transport-layer protocols, but they serve very different purposes depending on the application’s requirements.

1. Reliability & Delivery Guarantees:

   - TCP is connection-oriented. It ensures reliable delivery by using acknowledgments (ACKs), retransmissions, and sequencing. This means data arrives in order and without duplication. It’s great for applications where correctness is critical — e.g., web traffic (HTTP/HTTPS), file transfers, database replication.
   - UDP is connectionless. It does not guarantee delivery, ordering, or error correction beyond basic checksums. This makes it faster but unreliable. If packets are lost or arrive out of order, the application itself must handle that logic (if it cares).

2. Performance & Overhead:

   - TCP has more overhead due to connection setup (3-way handshake), state management, congestion control, and flow control. It prioritizes reliability over speed.
   - UDP is lightweight, with very little overhead. There’s no connection handshake, which makes it suitable for low-latency and high-throughput scenarios.

3. Use Cases:

   - TCP: Web browsers, APIs over HTTP(S), SSH, FTP — basically anywhere where consistency and data integrity are essential.
   - UDP: Real-time streaming, gaming, VoIP, DNS — where speed and low latency are more important than reliability, and occasional packet loss is tolerable.

4. Network Behavior:

   - TCP adapts to network conditions with congestion control (e.g., slow start, AIMD).
   - UDP just keeps sending — it doesn’t care if the network is congested. That’s why protocols like QUIC were introduced: to bring TCP-like reliability over UDP while maintaining low latency.

### 3-Way Handshake

The 3-way handshake is how TCP establishes a reliable, connection-oriented communication channel between two endpoints before exchanging data.

1. **SYN (synchronize)**

   - The client sends a packet with the SYN flag set and an initial sequence number (ISN_c).
   - This tells the server: “I want to start a connection, and here’s my starting sequence number.”

2. **SYN-ACK (synchronize + acknowledgment)**

   - The server responds with a packet that has both the SYN and ACK flags set.
   - It includes its own initial sequence number (ISN_s) and acknowledges the client’s ISN by setting ACK = ISN_c + 1.
   - This says: “I got your request, here’s my sequence number, and I acknowledge yours.”

3. **ACK (acknowledgment)**

   - The client sends back a final packet with the ACK flag set, acknowledging the server’s ISN (ACK = ISN_s + 1).
   - At this point, both sides have exchanged sequence numbers and acknowledgments. The connection is established.

### 4-Way Handshake

The 4-way handshake is the process TCP uses to gracefully terminate a connection. Unlike setup, teardown requires four steps because TCP connections are full-duplex — each side must close its half of the connection independently.

1. **FIN (finish) from client → server**

   - The client sends a FIN packet, indicating it has no more data to send.
   - The client enters the FIN_WAIT_1 state.

2. **ACK from server → client**

   - The server acknowledges the FIN with an ACK, meaning: “I know you’re done sending.”
   - The server can still send data back if it has some left.
   - The client enters the FIN_WAIT_2 state.

3. **FIN from server → client**

   - Once the server has finished sending its remaining data, it sends its own FIN.
   - This tells the client: “I’m also done sending.”
   - The server enters the LAST_ACK state.

4. **ACK from client → server**

   - The client responds with a final ACK, confirming the server’s FIN.
   - At this point:
     - The server transitions to the CLOSED state.
     - The client enters the TIME_WAIT state (usually 2×MSL — maximum segment lifetime), to ensure delayed packets are handled properly before fully closing.

### TLS Handshake

The TLS handshake establishes a secure channel between client and server by agreeing on encryption keys and verifying identities. The exact flow depends on TLS version (1.2 vs 1.3).

1. TLS 1.2 Handshake (traditional)

   - ClientHello

     - Client sends: supported TLS version, list of cipher suites, random nonce.
     - Says: “Here’s what I support.”

   - ServerHello

     - Server responds with chosen TLS version, cipher suite, its random nonce, and its certificate (X.509 cert containing public key).
     - The certificate is signed by a trusted Certificate Authority (CA).
     - The client validates the cert (domain name match, CA chain, expiration).

   - Key Exchange

     - If RSA: Client generates a random premaster secret, encrypts it with server’s public key, and sends it.
     - If ECDHE (more common today): Client and server perform a Diffie-Hellman key exchange to generate a shared secret.
     - Both sides now derive a session key from this secret + nonces.

   - Finished Messages

     - Client and server each send a “Finished” message encrypted with the new session key, proving encryption works.
     - From this point forward, all communication is encrypted.

2. TLS 1.3 Handshake (modern, what Google uses today)

- TLS 1.3 is faster and more secure:

  - Combines steps → handshake typically requires 1 round-trip (1-RTT) instead of 2.
  - Always uses forward-secret key exchange (ECDHE) — no more static RSA.
  - Encrypts more of the handshake itself for privacy.
  - Supports 0-RTT resumption: if you’ve connected before, you can start sending encrypted data immediately.

### What happens when you type-in "www.google.com" in your browser?

1. Browser Processing

   - The browser checks if it already has a cached mapping of google.com → IP address (in browser cache, OS cache, or DNS cache).
   - If cached, it uses it. Otherwise, it initiates a DNS lookup.

2. DNS Resolution

   - The browser/OS queries the configured DNS resolver (e.g., from ISP, or Google’s 8.8.8.8).
   - The resolver may return the IP from its cache, or it recursively queries:
   - Root DNS servers → TLD servers (.com) → Google’s authoritative DNS servers.
   - Eventually, the resolver returns the IP address of google.com (actually, a set of IPs, often load-balanced).

3. TCP Connection Establishment

   - With the IP in hand, the browser opens a TCP connection to the server (default port 80 for HTTP or 443 for HTTPS).
   - This involves the 3-way handshake (SYN → SYN-ACK → ACK).

4. TLS Handshake (if HTTPS, which Google always is)

   - The browser and server perform a TLS handshake:
   - Negotiate protocol version & cipher suites.
   - Exchange certificates (Google presents its SSL/TLS cert, which the browser validates against trusted Certificate Authorities).
   - Derive session keys for encrypted communication.
   - From now on, data is encrypted.

5. HTTP Request

   - The browser sends an HTTP GET request for / (the homepage) with headers (Host: google.com, User-Agent, etc.).
   - This is transmitted over the secure TCP+TLS connection.

6. Server Processing

   - Google’s load balancer receives the request (possibly via anycast IP).
   - The request may go through reverse proxies, caching layers (Google Frontend, CDNs), and eventually reach Google’s web servers.
   - The server generates or retrieves the response (HTML, JSON, or redirect).

7. HTTP Response

   - The server sends back an HTTP response (status code, headers, and body).
   - For Google, often it’s a redirect (302 to a localized domain like google.az) or directly the search page.

8. Browser Rendering

   - The browser parses the HTML:
   - Builds the DOM tree.
   - Fetches linked resources (CSS, JS, images). Each may trigger additional DNS lookups, TCP/TLS handshakes, and HTTP requests.
   - Executes JS, applies styles, and paints pixels on the screen.
   - This may involve parallel connections and caching strategies (HTTP/2 multiplexing, compression, etc.).

9. User Sees Page

   - Finally, the rendered page appears in the browser window.

### HTTP Request Methods

- **GET**

  - Retrieves a resource.
  - Should not modify server state.
  - Safe, idempotent.

- **POST**

  - Submits data to the server, often creating a new resource.
  - Not idempotent.

- **PUT**

  - Replaces an existing resource with the provided data.
  - Idempotent (sending the same request twice results in the same final state).

- **PATCH**

  - Partially updates a resource.
  - Not always idempotent (depends on implementation).

- **DELETE**

  - Removes a resource.
  - Idempotent (deleting the same resource twice still results in it being gone).

- **HEAD**

  - Same as GET, but returns only headers (no body).
  - Useful for checking metadata (e.g., resource existence, content length).

- **OPTIONS**

  - Returns supported methods for a resource.
  - Common in CORS preflight requests in browsers.

- **TRACE**

  - Echoes the received request, mainly for debugging. Rarely used (and often disabled for security).

- **CONNECT**

  - Establishes a tunnel to the server, often used for HTTPS via proxy.

## Algorithms & Data-structures

- **Two Sum** -> find the first two members of an array which their sum equals a target number.
- **Roman to Integer** -> convert roman numbers to integers.
- **Palindrome** -> determine whether a text/string/number is mirrored or not.
- **The N-Nearest drives** -> create an efficient way to find 'N' nearest drivers to a passenger (hint: an optimized way is using a min-heap)
- **Vectors** -> a class for storing vectors' X and Y coordinates and modify it so that these vectors can add-up with each other and print them in a customized way.

## Design Systems

- Design tweeter from the ground up
- Consider we have a project with 100,000 RPS and these requests data is written on files, design a system for reading and using that data
- Consider we have two postgres databases and a partition happens between them; what happens now?

## Projects

- Torna-System -> File-Manager
- Invex -> Block-Chain Wallet
- Faraswap -> User registration + Wallet
- Porsline -> Recommendation system based on user history and activity
- Toman -> E-commerce CRUD endpoints
- Torob -> Read, integrate and sort weather reports from a file
- Remote Synergy (Partnerz) -> Refactor a SMTP mailing service
- Maktabkhoone -> Design signals based on the observer design pattern (signal register + triggering)
