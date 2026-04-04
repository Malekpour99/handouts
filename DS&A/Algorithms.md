# Algorithms

## Table of Contents

- [Algorithms](#algorithms)
  - [Table of Contents](#table-of-contents)
  - [Asymptotic Notations](#asymptotic-notations)
  - [Sorting Algorithms](#sorting-algorithms)
    - [Bubble Sort](#bubble-sort)
    - [Selection Sort](#selection-sort)
    - [Insertion Sort](#insertion-sort)
    - [Merge Sort](#merge-sort)
    - [Quick Sort](#quick-sort)
    - [Heap Sort](#heap-sort)
  - [Dijkstra Algorithm](#dijkstra-algorithm)

## Asymptotic Notations

| Notation      | Meaning                          | Describes                                          |
| ------------- | -------------------------------- | -------------------------------------------------- |
| **Big O (O)** | Upper bound                      | Worst-case scenario (maximum time or space)        |
| **Omega (Ω)** | Lower bound                      | Best-case scenario (minimum time or space)         |
| **Theta (Θ)** | Tight bound (both upper & lower) | Exact runtime for all inputs (exact time or space) |

- Most of the time, **Big O notation** is used for describing _time and space complexity_.
- **Time complexity** describes how the number of operations grows as input size increases.
- **Space Complexity** is the amount of memory an algorithm uses relative to the input size.

| Complexity (Best to Worst) | Name         | Example Algorithm                                         |
| -------------------------- | ------------ | --------------------------------------------------------- |
| **O(1)**                   | Constant     | Accessing an array element                                |
| **O(log n)**               | Logarithmic  | Binary search                                             |
| **O(n)**                   | Linear       | Loop over array, DFS                                      |
| **O(n log n)**             | Linearithmic | Merge sort, Heap sort, Quick sort (avg case)              |
| **O(n²)**                  | Quadratic    | Nested loops, Bubble sort, Selection sort, Insertion sort |
| **O(n³)**                  | Cubic        | Naive matrix multiplication                               |
| **O(aⁿ)**                  | Exponential  | Recursive Fibonacci, brute-force subsets                  |
| **O(n!)**                  | Factorial    | Traveling Salesman Problem (TSP), Permutations            |

## Sorting Algorithms

### Bubble Sort

- Idea: Repeatedly swap adjacent elements if they are in the wrong order.
- Time Complexity: **O(n²)**

```python
# python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1): # Last i elements are already in place
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
```

```go
// go
func BubbleSort(arr []int) {
	n := len(arr)
	for i := 0; i < n; i++ {
		for j := 0; j < n-i-1; j++ {
			if arr[j] > arr[j+1] {
				arr[j], arr[j+1] = arr[j+1], arr[j]
			}
		}
	}
}
```

### Selection Sort

- Idea: Repeatedly find the minimum element and move it to the sorted portion at the front.
- Time Complexity: **O(n²)**

```python
# python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
```

```go
// go
func SelectionSort(arr []int) {
	n := len(arr)
	for i := 0; i < n; i++ {
		minIdx := i
		for j := i + 1; j < n; j++ {
			if arr[j] < arr[minIdx] {
				minIdx = j
			}
		}
		arr[i], arr[minIdx] = arr[minIdx], arr[i]
	}
}
```

### Insertion Sort

- Idea: Build the sorted array one element at a time by inserting each new element into its correct position.
- Time Complexity: **O(n²)**

```python
# python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
```

```go
// go
func InsertionSort(arr []int) {
	n := len(arr)
	for i := 1; i < n; i++ {
		key := arr[i]
		j := i - 1
		for j >= 0 && arr[j] > key {
			arr[j+1] = arr[j]
			j--
		}
		arr[j+1] = key
	}
}
```

### Merge Sort

- Idea: Divide and conquer. Divide the array into halves, sort recursively, and merge.
- Time Complexity: **O(n log n)**

```python
# python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        # Merging
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Remaining elements
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr
```

```go
// go
func MergeSort(arr []int) []int {
	if len(arr) <= 1 {
		return arr
	}

	mid := len(arr) / 2
	left := MergeSort(arr[:mid])
	right := MergeSort(arr[mid:])

	return merge(left, right)
}

func merge(left, right []int) []int {
	result := []int{}
	i, j := 0, 0

	for i < len(left) && j < len(right) {
		if left[i] < right[j] {
			result = append(result, left[i])
			i++
		} else {
			result = append(result, right[j])
			j++
		}
	}

	result = append(result, left[i:]...)
	result = append(result, right[j:]...)

	return result
}
```

### Quick Sort

- Idea: Pick a pivot, partition array into elements less than pivot and greater than pivot, and sort recursively.
- Time Complexity: **O(n log n) average, O(n²) worst case (when pivot is the max/min of array)**

```python
# python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left, right = [], []
    for x in arr[1:]:
      if x < pivot:
        left.append(x)
      else:
        right.append(x)
    return quick_sort(left) + [pivot] + quick_sort(right)
```

```go
// go
func QuickSort(arr []int) []int {
	if len(arr) <= 1 {
		return arr
	}

	pivot := arr[0]
	left := []int{}
	right := []int{}

	for _, x := range arr[1:] {
		if x < pivot {
			left = append(left, x)
		} else {
			right = append(right, x)
		}
	}

	left = QuickSort(left)
	right = QuickSort(right)

	result := append(left, pivot)
	result = append(result, right...)

	return result
}
```

### Heap Sort

- Idea: Build a max-heap and repeatedly extract the maximum element.
- Time Complexity: **O(n log n)**

```python
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    # Build max-heap (floor(n/2) -1 gives you the last parent index)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one from max-heap
    for i in range(n - 1, 0, -1):
        # arr[0] is the max-heap root in every step
        arr[i], arr[0] = arr[0], arr[i] # move current root to end
        heapify(arr, i, 0)              # call max heapify on the reduced heap
    return arr
```

```go
// go
func HeapSort(arr []int) {
	n := len(arr)

	// Build Max-Heap
	for i := n/2 - 1; i >= 0; i-- {
		heapify(arr, n, i)
	}

	// One by one extract elements from heap
	for i := n - 1; i > 0; i-- {
    // arr[0] is the max-heap root in every step
		arr[0], arr[i] = arr[i], arr[0] // Move current root to end
		heapify(arr, i, 0)              // call max heapify on the reduced heap
	}
}

func heapify(arr []int, n, i int) {
	largest := i
	left := 2*i + 1
	right := 2*i + 2

	if left < n && arr[left] > arr[largest] {
		largest = left
	}

	if right < n && arr[right] > arr[largest] {
		largest = right
	}

	if largest != i {
		arr[i], arr[largest] = arr[largest], arr[i]
		heapify(arr, n, largest)
	}
}
```

## Dijkstra Algorithm

- Dijkstra's algorithm is a popular **greedy algorithm** used to **find the shortest path between nodes in a graph**.
- It solves the Single-Source Shortest Path (SSSP) problem, meaning it finds the shortest path from a specific starting node to all other nodes in the graph.
- Key Requirements:
  - Weighted Graph: The edges connecting nodes must have values (weights/costs).
  - Non-Negative Weights: Dijkstra's algorithm **does not work with negative edge weights**. (If you have negative weights, use the Bellman-Ford algorithm).

- How It Works (Step-by-Step):
  1. Initialization:
     - Set the distance to the start node as 0.
     - Set the distance to all other nodes as infinity (∞).
     - Add all nodes to a priority queue (or unvisited set), prioritized by their current known distance.
  2. Selection:
     - Select the unvisited node with the smallest known distance from the start node. (Initially, this is the start node itself).
  3. Relaxation (Updating Neighbors):
     - For the current node, look at all its unvisited neighbors.
     - Calculate the distance from the start node to the neighbor through the current node (current_distance + edge_weight).
     - If this calculated distance is less than the neighbor's currently recorded distance, update the neighbor's distance.
  4. Mark as Visited:
     - Once all neighbors are checked, mark the current node as visited. A visited node will not be checked again.
  5. Repeat:
     - Repeat steps 2–4 until the priority queue is empty or the target node is visited.

```python
import heapq
from collections import defaultdict

def dijkstra(graph, start_node):
    """
    Finds the shortest path from start_node to all other nodes in the graph.

    Args:
        graph: A dictionary representing an adjacency list.
               Format: {node: [(neighbor, weight), ...]}
        start_node: The starting vertex.

    Returns:
        distances: A dictionary mapping each node to its shortest distance from start_node.
    """

    # 1. Initialize distances to infinity for all nodes
    # We use a defaultdict so accessing a missing key returns infinity
    distances = defaultdict(lambda: float('inf'))
    distances[start_node] = 0

    # 2. Priority queue to store (distance, node) tuples
    # We start with the start_node having distance 0
    priority_queue = [(0, start_node)]

    # Set to keep track of visited nodes (optional optimization with heap)
    visited = set()

    while priority_queue:
        # 3. Pop the node with the smallest distance
        current_distance, current_node = heapq.heappop(priority_queue)

        # If we have already processed this node with a shorter distance, skip it
        if current_node in visited:
            continue

        visited.add(current_node)

        # 4. Iterate over neighbors
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # 5. Relaxation step: If a shorter path is found, update distance
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# --- Example Usage ---

# Define a graph as an adjacency list
# Format: Node -> List of (Neighbor, Weight)
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

start = 'A'
shortest_distances = dijkstra(graph, start)

print(f"Shortest distances from node {start}:")
for node, distance in shortest_distances.items():
    print(f"Node {node}: {distance}")
```
