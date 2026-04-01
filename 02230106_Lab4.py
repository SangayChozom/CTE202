class ArrayQueue:
    def __init__(self, capacity=10):
        """Task 1: Initialize the queue with a fixed capacity."""
        self.capacity = capacity
        self.queue = [None] * capacity  # Private-like array with default capacity
        self.front = 0
        self.rear = 0
        self.num_elements = 0
        print(f"Created new Queue with capacity: {self.capacity}")

    def is_empty(self):
        """Check if the queue is empty."""
        return self.num_elements == 0

    def is_full(self):
        """Check if the queue has reached its capacity."""
        return self.num_elements == self.capacity

    def enqueue(self, element):
        """Task 2: Add an element to the rear of the queue."""
        if self.is_full():
            print("Queue Overflow! Cannot enqueue.")
            return
        
        self.queue[self.rear] = element
        # Use modulo arithmetic to make it a circular queue
        self.rear = (self.rear + 1) % self.capacity
        self.num_elements += 1
        print(f"Enqueued {element} to the queue")

    def dequeue(self):
        """Task 2: Remove and return the element at the front."""
        if self.is_empty():
            print("Queue Underflow! Cannot dequeue.")
            return None
        
        element = self.queue[self.front]
        self.queue[self.front] = None  # Clear the spot
        self.front = (self.front + 1) % self.capacity
        self.num_elements -= 1
        return element

    def peek(self):
        """Task 2: Return the front element without removing it."""
        if self.is_empty():
            print("Queue is empty.")
            return None
        return self.queue[self.front]

    def size(self):
        """Task 2: Return the current number of elements."""
        return self.num_elements

    def display(self):
        """Task 2: Show all elements in the queue."""
        if self.is_empty():
            print("Display queue: []")
            return
            
        elements = []
        current = self.front
        for _ in range(self.num_elements):
            elements.append(self.queue[current])
            current = (current + 1) % self.capacity
        print(f"Display queue: {elements}")


# --- Demonstration for Part 1 ---
if __name__ == "__main__":
    print("--- Testing Array Queue ---")
    aq = ArrayQueue(10)
    print(f"Queue is empty: {aq.is_empty()}")
    
    aq.enqueue(10)
    aq.display()
    aq.enqueue(20)
    aq.display()
    aq.enqueue(30)
    aq.display()
    
    print(f"Front element: {aq.peek()}")
    print(f"Dequeued element: {aq.dequeue()}")
    aq.display()
    print(f"Queue size: {aq.size()}")
    print()



class Node:
    """Class to represent a single node in the linked list."""
    def __init__(self, data):
        self.data = data      # Data field to store the element [cite: 67]
        self.next = None      # Next field to reference the next node 


class LinkedQueue:
    """Class to represent a Queue using a Linked List."""
    def __init__(self):
        self._front = None    # Front reference to the first node [cite: 70]
        self._rear = None     # Rear reference to the last node [cite: 71]
        self._size = 0        # Size counter to track number of elements [cite: 72]
        print("Created new Linked Queue") # Matches example output [cite: 74]

    def is_empty(self):
        """Check if the queue is empty."""
        return self._front is None

    def size(self):
        """Return the current number of elements."""
        return self._size

    def enqueue(self, element):
        """Add an element to the rear of the queue."""
        new_node = Node(element)
        
        # If queue is empty, both front and rear will point to the new node
        if self.is_empty():
            self._front = new_node
            self._rear = new_node
        else:
            self._rear.next = new_node
            self._rear = new_node
            
        self._size += 1
        print(f"Enqueued {element} to the queue") 

    def dequeue(self):
        """Remove and return the element at the front."""
        if self.is_empty():
            print("Queue Underflow! Cannot dequeue from an empty queue.")
            return None
            
        removed_data = self._front.data
        self._front = self._front.next
        
        # If the queue becomes empty after dequeue, set rear to None
        if self._front is None:
            self._rear = None
            
        self._size -= 1
        return removed_data

    def peek(self):
        """Return the element at the front without removing it."""
        if self.is_empty():
            print("Queue is empty.")
            return None
        return self._front.data

    def display(self):
        """Show all elements in the queue matching requested formats."""
        if self.is_empty():
            print("Current queue: empty")
            return
            
        elements = []
        current = self._front
        while current:
            elements.append(str(current.data))
            current = current.next
            
        # Matches the formatting requested in your task example outputs 
        if len(elements) == 1:
            print(f"Display queue: [{elements[0]}]")
        else:
            arrow_format = " -> ".join(elements) + " -> null"
            print(f"Current queue: {arrow_format}")


if __name__ == "__main__":
    # Task 3 Example Output Test 
    queue = LinkedQueue()
    print(f"Queue is empty: {queue.is_empty()}") 
    print("-" * 30)

    # Task 4 Example Output Test 
    queue.enqueue(10) 
    queue.display()   
    
    queue.enqueue(20) 
    queue.display()   
    
    queue.enqueue(30) 
    queue.display()   
    
    print(f"Front element: {queue.peek()}")
    
    dequeued = queue.dequeue() 
    print(f"Dequeued element: {dequeued}") 
    
    queue.display() 
    print(f"Queue size: {queue.size()}") 