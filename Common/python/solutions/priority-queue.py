import heapq


# using a min-heap for efficient priority queue implementation
class PriorityQueue:
    def __init__(self):
        self._heap = []

    def append(self, value, priority):
        """
        Add an item with a given priority.
        Lower priority numbers are popped first.
        """
        # heapq is a min-heap; first element is priority
        heapq.heappush(self._heap, (priority, value))

    def pop(self):
        """
        Remove and return the item with the highest priority.
        Raises IndexError if queue is empty.
        """
        if not self._heap:
            raise IndexError("pop from an empty priority queue")
        priority, value = heapq.heappop(self._heap)
        return value


# Example usage:
pq = PriorityQueue()
pq.append("low", 5)
pq.append("medium", 3)
pq.append("high", 1)

print(pq.pop())  # "high"
print(pq.pop())  # "medium"
print(pq.pop())  # "low"


# using a simple list for priority queue implementation
class PriorityQueue:
    def __init__(self):
        self._queue = []

    def append(self, value, priority):
        """
        Add an item with a given priority.
        Lower priority numbers are considered higher priority.
        """
        # Find the right position to insert
        inserted = False
        for i, (_, p) in enumerate(self._queue):
            if priority < p:
                self._queue.insert(i, (value, priority))
                inserted = True
                break
        if not inserted:
            # If no higher priority found, append at the end
            self._queue.append((value, priority))

    def pop(self):
        """
        Remove and return the item with the highest priority.
        Raises IndexError if the queue is empty.
        """
        if not self._queue:
            raise IndexError("pop from an empty priority queue")
        value, _ = self._queue.pop(0)
        return value


# Example usage
pq = PriorityQueue()
pq.append("low", 5)
pq.append("medium", 3)
pq.append("high", 1)

print(pq.pop())  # high
print(pq.pop())  # medium
print(pq.pop())  # low
