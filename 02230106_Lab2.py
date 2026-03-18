class Node:
    def __init__(self, data):
        self.data = data  # Data field to store the element
        self.next = None  # Next field to reference the next node 

class LinkedList:
    def __init__(self):
        self.head = None  # Head reference to the first node 
        self.tail = None  # Tail reference to the last node (optional)
        self._size = 0    # Size counter to track number of elements
        print("Created new LinkedList")

# Example Output for Task 1
if __name__ == "__main__":
    ll = LinkedList()
    print(f"Current size: {ll._size}")
    print(f"Head: {ll.head}")

class Node:
    def __init__(self, data):
        self.data = data # Data field to store the element 
        self.next = None # Next field to reference the next node

class LinkedList:
    def __init__(self):
        self.head = None # Head reference to the first node 
        self.tail = None # Tail reference to the last node 
        self._size = 0   # Size counter 
        print("Created new LinkedList")  

    def size(self):
        """Return the current number of elements"""
        return self._size 

    def append(self, element):
        """Add an element to the end of the list"""
        new_node = Node(element)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1
        print(f"Appended {element} to the list")  

    def prepend(self, element):
        """Add an element at the beginning of the list"""
        new_node = Node(element)
        new_node.next = self.head
        self.head = new_node
        if self._size == 0:
            self.tail = new_node
        self._size += 1
        print(f"Prepend {element} to the list")  

    def get(self, index):
        """Retrieve an element at a specific index"""
        if index < 0 or index >= self._size:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data 

    def set(self, index, element):
        """Replace an element at a specific index"""
        if index < 0 or index >= self._size:
            return
        current = self.head
        for _ in range(index):
            current = current.next
        current.data = element 
        print(f"Set element at index {index} to {element}") 

    def display(self):
        """Displays the list in the required format"""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(f"Print Linked list : [{' '.join(elements)}]") 

# Testing the implementation
if __name__ == "__main__":
    ll = LinkedList()
    print(f"Current size: {ll.size()}") 
    print(f"Head: {ll.head}") 
    
    ll.append(5) # 
    print(f"Element at index 0: {ll.get(0)}") 
    ll.set(0, 10) 
    print(f"Element at index 0: {ll.get(0)}")
    print(f"Current size: {ll.size()}") 
    ll.prepend(10)  
    ll.append(5) 
    ll.display() 