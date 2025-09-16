# Interview Questions

## Table of Contents

- [Interview Questions](#interview-questions)
  - [Table of Contents](#table-of-contents)
  - [Programming General Concepts](#programming-general-concepts)
    - [Process Vs. Thread](#process-vs-thread)
    - [Regular Thread Vs. Light Thread](#regular-thread-vs-light-thread)
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

## Programming General Concepts

### Process Vs. Thread

- **Process**

  - A process is an **independent program in execution**.
  - Each process has:
    - Its **own memory space** (heap, stack, code).
    - Its **own resources** (file descriptors, sockets, etc.).
  - Communication between processes requires **IPC (Inter-Process Communication)** like pipes, sockets, shared memory.
  - Isolation → one process crash won’t usually crash others.
  - Heavier to create, switch, and communicate.

- **Thread**
  - A thread is a **lightweight execution unit inside a process**.
  - Threads in the same process share:
    - The **same memory space** (heap, global variables).
    - **File descriptors** and **other resources**.
  - Each thread has its _own stack and program counter_.
  - Lightweight, faster context switch, easy to share data.
  - Less isolation → one thread crash can crash the whole process.

---

### Regular Thread Vs. Light Thread

- **Regular Thread (OS Thread)**

  - Managed by the **operating system kernel**.
  - Each thread has its own stack, registers, and is **scheduled by the OS scheduler**.
  - True parallelism → if you have multiple CPU cores, OS threads can run simultaneously.
  - Heavier: creating, destroying, and context switching threads has overhead.

- **Lightweight Thread (Green Thread / User Thread)**
  - Managed at the **user level**, not by the OS.
  - **Scheduler runs inside the runtime/library** (not the kernel).
  - Multiple lightweight threads are multiplexed onto fewer OS threads.
  - Examples: `Goroutines` in Go.
  - Very cheap to create (thousands to millions possible).
  - Fast context switching (just saving a few registers).
  - _Don’t get true parallelism_ unless the runtime maps them onto multiple OS threads.
  - If one lightweight thread makes a blocking system call, it can block the entire runtime thread.

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
