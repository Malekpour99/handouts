class CircularQueue:
    """simple demonstration of a circular queue and its relevant actions"""
    def __init__(self, k):
        "Creating simple queue"
        self.k = k
        self.queue = [None] * k
        self.front = -1
        self.rear = -1

    def display(self):
        "Outputting the current status of queue"
        if(self.front == -1):
            print("Queue is empty!")
            return None
        elif(self.front <= self.rear):
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=' ')
        else:
            for i in range(self.front, self.k):
                print(self.queue[i], end=' ')
            for i in range(0, self.rear + 1):
                print(self.queue[i], end=' ')

    def dequeue(self):
        "removing front member of the queue"
        if(self.front == -1):
            print("Queue is empty!")
            return None
        elif(self.front == self.rear):
            # in order to avoid changing queue length, we don't pop its members
            target = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return target
        else:
            target = self.queue[self.front]
            self.front = (self.front + 1) % self.k
            return target

    def enqueue(self, data):
        "Adding new member to the end of the queue"
        if((self.rear + 1) % self.k == self.front):
            print("Queue is full!")
            return None
        elif(self.front == -1):
            self.front = 0 
            self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear = (self.rear + 1) % self.k
            self.queue[self.rear] = data


# just a simple example:
q = CircularQueue(3)
q.display()
q.enqueue('a')
q.enqueue('b')
q.enqueue('c')
q.display()

