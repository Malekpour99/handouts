# Heap: A full binary tree
# (+) filling starts from left side and
#   each level must be full in order to start the next one!
# MaxHeap: root has the biggest key
# MinHeap: root has the smallest key
# i node =>
# left-node: 2i+1
# right-node: 2i+2
# node's parent: floor((i-1)/2)


def heapify(array: list[int], index: int):
    """
    Converts your heap to a MaxHeap using its array, based on the given node index
    Compares nodes with their parents and swap them if needed
    """
    p = int((index - 1) / 2)
    if array[p] > 0:
        if array[index] > array[p]:
            array[index], array[p] = array[p], array[index]
            heapify(array, p)


def insert_node(array: list[int], data: int):
    """
    Inserting a node into a max-heap and then heapify
    Node is inserted at the end of our array
    """
    n = len(array)
    array.append(data)  # data is inserted an 'n' index
    heapify(array, n)


def max_heapify(arr: list, node_index: int, current_node_index: int):
    "Converts your heap to a MaxHeap using its array"
    largest = current_node_index
    left_node_index = 2 * current_node_index + 1
    right_node_index = 2 * current_node_index + 2
    if left_node_index < node_index and arr[current_node_index] < arr[left_node_index]:
        largest = left_node_index

    if right_node_index < node_index and arr[largest] < arr[right_node_index]:
        largest = right_node_index

    if largest != current_node_index:
        arr[current_node_index], arr[largest] = arr[largest], arr[current_node_index]
        max_heapify(arr, node_index, largest)


def heap_sort(arr: list[int]):
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


def min_heapify(array: list[int], index: int):
    "Converts your heap to a MinHeap using its array based on node index"
    left_node_index = 2 * index + 1
    right_node_index = 2 * index + 2
    if left_node_index < len(array) and array[left_node_index] < array[index]:
        smallest = left_node_index
    else:
        smallest = index

    if right_node_index < len(array) and array[right_node_index] < array[smallest]:
        smallest = right_node_index

    if smallest != index:
        array[index], array[smallest] = array[smallest], array[index]
        min_heapify(array, smallest)


def build_min_heap(array: list[int]):
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
