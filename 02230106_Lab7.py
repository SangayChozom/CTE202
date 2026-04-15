class Node:
    def __init__(self, value):
        self.value = value      # Value of the node 
        self.left = None       # Left child reference 
        self.right = None      # Right child reference 
class BinaryTree:
    """
    A class representing the Binary Tree structure.
    """
    def __init__(self, root_value=None):
        # Constructor to initialize an empty or pre-populated tree 
        if root_value is not None:
            self.root = Node(root_value) # Root node reference 
        else:
            self.root = None # Root node reference 
# --- Demonstration of Example Output ---
if __name__ == "__main__":
    # Initializing an empty tree to match the example output requirements
    my_tree = BinaryTree()
    
    print("Created new Binary Tree") 
    
    # Checking if root is None or printing value
    if my_tree.root is None:
        print("Root: None") 
    else:
        print(f"Root: {my_tree.root.value}")

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_value=None):
        """Constructor to initialize an empty or pre-populated tree [cite: 34]"""
        if root_value is not None:
            self.root = Node(root_value)
        else:
            self.root = None

    def height(self, node):
        """Calculate the maximum depth of the tree [cite: 40]"""
        if node is None:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    def size(self, node):
        """Count total number of nodes [cite: 41]"""
        if node is None:
            return 0
        return 1 + self.size(node.left) + self.size(node.right)

    def count_leaves(self, node):
        """Count number of leaf nodes [cite: 42]"""
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        return self.count_leaves(node.left) + self.count_leaves(node.right)

    def is_full_binary_tree(self, node):
        """Check if every node has either 0 or 2 children [cite: 18, 43]"""
        if node is None:
            return True
        if node.left is None and node.right is None:
            return True
        if node.left is not None and node.right is not None:
            return self.is_full_binary_tree(node.left) and self.is_full_binary_tree(node.right)
        return False

    def is_complete_binary_tree(self, node, index, number_nodes):
        """Check if all levels are filled except possibly the last [cite: 19, 44]"""
        if node is None:
            return True
        if index >= number_nodes:
            return False
        return (self.is_complete_binary_tree(node.left, 2 * index + 1, number_nodes) and
                self.is_complete_binary_tree(node.right, 2 * index + 2, number_nodes))

# --- Execution ---
if __name__ == "__main__":
    # Task 1 Output
    print("Task 1")
    empty_tree = BinaryTree()
    print("Created new Binary Tree")
    print(f"Root: {empty_tree.root}")
    
    print("-" * 20)

    # Task 2 Output
    print("Task 2")
    
    # Building a Perfect Binary Tree (7 nodes) to achieve the example metrics
    # Level 0
    root = Node(1)
    # Level 1
    root.left = Node(2)
    root.right = Node(3)
    # Level 2
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    
    lab_tree = BinaryTree()
    lab_tree.root = root
    
    # Run calculations once
    h = lab_tree.height(lab_tree.root)
    s = lab_tree.size(lab_tree.root)
    l = lab_tree.count_leaves(lab_tree.root)
    is_full = lab_tree.is_full_binary_tree(lab_tree.root)
    is_comp = lab_tree.is_complete_binary_tree(lab_tree.root, 0, s)

    # Clean Printing (No duplicates)
    print(f"Tree Height: {h}")
    print(f"Total Nodes: {s}")
    print(f"Leaf Nodes Count: {l}")
    print(f"Is Full Binary Tree: {is_full}")
    print(f"Is Complete Binary Tree: {is_comp}")