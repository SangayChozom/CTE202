import ctypes

class CustomList:
    def __init__(self, default_capacity=10):
        self.capacity = default_capacity 
        self.current_size = 0
        self._array = (self.capacity * ctypes.py_object)()
        
        # Exact Example Output Requirement:
        print(f"Created new CustomList with capacity: {self.capacity}")
        print(f"Current size: {self.current_size}")

    def append(self, element):
        if self.current_size < self.capacity:
            self._array[self.current_size] = element
            self.current_size += 1
            print(f"Appended {element} to the list")

    def get(self, index):
        if 0 <= index < self.current_size:
            return self._array[index]
        return "Index out of bounds"

    def set(self, index, element):
        if 0 <= index < self.current_size:
            self._array[index] = element
            print(f"Set element at index {index} to {element}")

    def size(self):
        return self.current_size

# --- Execution ---
if __name__ == "__main__":
    # This section matches your requested Example Output exactly
    my_list = CustomList(10)
    my_list.append(5)
    print(f"Element at index 0: {my_list.get(0)}")
    my_list.set(0, 10)
    print(f"Element at index 0: {my_list.get(0)}")
    print(f"Current size: {my_list.size()}")