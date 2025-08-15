# Heap: A full binary tree
# (+) filling starts from left side and
#   each level must be full in order to start the next one!
# MaxHeap: root has the biggest key
# MinHeap: root has the smallest key
# i node =>
# left-node: 2i+1
# right-node: 2i+2
# node's parent: floor((i-1)/2)


def heapify(array, index):
    """
    Converts your heap to a MaxHeap using its array, based on the given node index
    Compares nodes with their parents and swap them if needed
    """
    p = int((index - 1) / 2)
    if array[p] > 0:
        if array[index] > array[p]:
            array[index], array[p] = array[p], array[index]
            heapify(array, p)


def insert_node(array, data):
    """
    Inserting a node into a max-heap and then heapify
    Node is inserted at the end of our array
    """
    n = len(array)
    array.append(data)  # data is inserted an 'n' index
    heapify(array, n)


def max_heapify(arr, n, i):
    "Converts your heap to a MaxHeap using its array"
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)


def heap_sort(arr):
    "Sorts your MaxHeap array"
    n = len(arr)
    # Creating MaxHeap
    # floor(n/2) - 1 gives you the last parent node index
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)
    # Sorting created MaxHeap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        max_heapify(arr, i, 0)


def min_heapify(array, index):
    "Converts your heap to a MinHeap using its array based on node index"
    l = 2 * index + 1
    r = 2 * index + 2
    if l < len(array) and array[l] < array[index]:
        smallest = l
    else:
        smallest = index
    if r < len(array) and array[r] < array[smallest]:
        smallest = r
    if smallest != index:
        array[index], array[smallest] = array[smallest], array[index]
        min_heapify(array, smallest)


def build_min_heap(array):
    "Creates a MinHeap from an array"
    n = int((len(array) // 2) - 1)
    for i in range(n, -1, -1):
        min_heapify(array, i)


A = [5, 6, 3, 1, 4, 2, 7]
build_min_heap(A)
print(A)  # [1, 4, 2, 6, 5, 3, 7]

c = [45, 35, 23, 27, 21, 22, 4, 19]
insert_node(c, 42)
for i in range(len(c)):
    print(c[i], end=" ")  # 45 42 23 35 21 22 4 19 27

print()
arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
n = len(arr)
for i in range(n):
    print(arr[i], end=" ")  # 5 6 7 11 12 13
