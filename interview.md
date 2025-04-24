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
    - [What are different types of design patterns?](#what-are-different-types-of-design-patterns)
    - [What is the Singleton Design Pattern?](#what-is-the-singleton-design-pattern)
  - [Django](#django)
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

### What are different types of design patterns?
**Design patterns** are reusable solutions to common problems in software design. They represent best practices refined over time by experienced developers.

|Category   | Purpose                            | Example Patterns                   |
|-----------|------------------------------------|------------------------------------|
|Creational | Object creation logic              | Singleton, Factory, Abstract Factory,  Builder, Prototype        |
|Structural | Object composition and flexibility | Adapter, Decorator, Proxy, Facade, Composite, Bridge, Flyweight  |
|Behavioral | Communication & responsibility     | Observer, Strategy, Command, State, Chain of Responsibility, Template Method, Visitor, Interpreter, Iterator |

---

### What is the Singleton Design Pattern?

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




## Django

## Database

## Docker & Containerization

## Network

## Projects