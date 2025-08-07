# Data-Structures

## Table of Contents

- [Data-Structures](#data-structures)
  - [Table of Contents](#table-of-contents)
  - [Array (List)](#array-list)
  - [Hash Table (Dictionary)](#hash-table-dictionary)
  - [Stack (LIFO)](#stack-lifo)
  - [Queue (FIFO)](#queue-fifo)
  - [Singly Linked List](#singly-linked-list)

## Array (List)

Key Features:

- Contiguous memory allocation
- Fixed or dynamic size
- Supports indexing, slicing, and iteration.

![Array](images/array.png)

Operations:

- Access: O(1)
- Search: O(n)
- Insert/Delete at end: O(1) (amortized)
- Insert/Delete at start or middle: O(n)

## Hash Table (Dictionary)

Key Features:

- Uses hashing to store key-value pairs
- Handles collisions via chaining or open addressing

![Hash Table](images/hash-table.webp)

Operations:

- Insert/Search/Delete: O(1) average

## Stack (LIFO)

Key Features:

- Last-In-First-Out structure
- Can be implemented using an array
- Has a **limit** which determines size of the stack

![Stack](images/stack.png)

Operations:

- Push/Pop: O(1)
- Peek: O(1)

**Implementation**: [Stack](Data-Structures/Stack.py)

## Queue (FIFO)

Key Features:

- First-In-First-Out structure
- **front** points to the first member of queue
- **rear** points to the last member of queue
- Has a **limit** which determines size of the queue

![Queue](images/queue.png)

Operations:

- Enqueue/Dequeue: O(1)

**Implementation**: [Queue](Data-Structures/queue.py)

## Singly Linked List

Key Features:

- Each link list starts from **head** node
- Each node holds **data** and a reference to the **next** node.
- No direct indexing; traversal required.

![Singly Linked List](images/singly-linked-list.png)

Operations:

- Insert/Delete at head: O(1)
- Insert/Delete at tail or by value: O(n)
- Search: O(n)

**Implementation**: [Singly Linked List](Data-Structures/Singly_Linked_List.py)
