class Stack:
    """Stack data structure demonstration"""

    def __init__(self, size: int = 100):
        "Creating stack considering size as its capacity limit"
        self.size = size
        self.stack = []

    def peek(self):
        "Seeing the last data on the stack"
        if len(self.stack) <= 0:
            return -1
        else:
            return self.stack[len(self.stack) - 1]

    def push(self, data):
        "Adding data to the stack"
        if len(self.stack) >= self.size:
            return -1
        else:
            self.stack.append(data)

    def pop(self):
        "removing data from top of the stack"
        if len(self.stack) <= 0:
            return -1
        else:
            return self.stack.pop()

    def is_empty(self):
        "Checks if the stack is empty or not"
        if len(self.stack) > 0:
            return False
        return True


# ------------- Some Educational Examples -------------
def d2b(number):
    "Converting decimal numbers to binary numbers"
    s = Stack()
    while number > 0:
        s.push(number % 2)
        number = number // 2
    b = ""
    while not s.is_empty():
        b = b + str(s.pop())
    return b


def reverser(lst):
    "Reverses list members"
    s = Stack()
    for m in lst:
        s.push(m)
    for i in range(len(lst)):
        lst[i] = s.pop()


def reverse_stack(S):
    "Reverses stack members"
    s1 = Stack()
    s2 = Stack()
    while not S.is_empty():
        s1.push(S.pop())
    while not s1.is_empty():
        s2.push(s1.pop())
    while not s2.is_empty():
        S.push(s2.pop())
