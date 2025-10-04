"""
Custom Data Structures Implementation
All data structures are implemented from scratch without using built-in libraries.
"""

class Stack:
    """
    Stack implementation using a list.
    LIFO (Last In First Out) data structure.
    """
    def __init__(self):
        self.items = []
    
    def push(self, item):
        """Add an item to the top of the stack. O(1)"""
        self.items.append(item)
    
    def pop(self):
        """Remove and return the top item. O(1)"""
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.items.pop()
    
    def peek(self):
        """Return the top item without removing it. O(1)"""
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.items[-1]
    
    def is_empty(self):
        """Check if stack is empty. O(1)"""
        return len(self.items) == 0
    
    def size(self):
        """Return the number of items in the stack. O(1)"""
        return len(self.items)


class Queue:
    """
    Queue implementation using a list.
    FIFO (First In First Out) data structure.
    """
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        """Add an item to the rear of the queue. O(1)"""
        self.items.append(item)
    
    def dequeue(self):
        """Remove and return the front item. O(n) due to list shift"""
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.items.pop(0)
    
    def front(self):
        """Return the front item without removing it. O(1)"""
        if self.is_empty():
            raise IndexError("Front from empty queue")
        return self.items[0]
    
    def is_empty(self):
        """Check if queue is empty. O(1)"""
        return len(self.items) == 0
    
    def size(self):
        """Return the number of items in the queue. O(1)"""
        return len(self.items)


class MinHeap:
    """
    Min Heap implementation for priority queue.
    Used in A* algorithm for efficient priority-based retrieval.
    """
    def __init__(self):
        self.heap = []
    
    def push(self, item):
        """
        Add an item to the heap and maintain heap property.
        Time Complexity: O(log n)
        """
        self.heap.append(item)
        self._sift_up(len(self.heap) - 1)
    
    def pop(self):
        """
        Remove and return the minimum item.
        Time Complexity: O(log n)
        """
        if self.is_empty():
            raise IndexError("Pop from empty heap")
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        min_item = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        return min_item
    
    def peek(self):
        """Return the minimum item without removing it. O(1)"""
        if self.is_empty():
            raise IndexError("Peek from empty heap")
        return self.heap[0]
    
    def is_empty(self):
        """Check if heap is empty. O(1)"""
        return len(self.heap) == 0
    
    def size(self):
        """Return the number of items in the heap. O(1)"""
        return len(self.heap)
    
    def _sift_up(self, index):
        """Move item up to maintain heap property. O(log n)"""
        parent = (index - 1) // 2
        if index > 0 and self.heap[index][0] < self.heap[parent][0]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._sift_up(parent)
    
    def _sift_down(self, index):
        """Move item down to maintain heap property. O(log n)"""
        min_index = index
        left = 2 * index + 1
        right = 2 * index + 2
        
        if left < len(self.heap) and self.heap[left][0] < self.heap[min_index][0]:
            min_index = left
        
        if right < len(self.heap) and self.heap[right][0] < self.heap[min_index][0]:
            min_index = right
        
        if min_index != index:
            self.heap[index], self.heap[min_index] = self.heap[min_index], self.heap[index]
            self._sift_down(min_index)

