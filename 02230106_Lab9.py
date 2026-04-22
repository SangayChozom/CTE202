# Task 1 & 2: Selection Sort with Comparison and Swap Counting
def selection_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    
    print(f"Original list: {arr}") 
    
    # Outer loop to go through each position 
    for i in range(n - 1):
        min_idx = i  # Variable to store index of minimum element 
        
        # Inner loop to find the smallest element in unsorted part 
        for j in range(i + 1, n):
            comparisons += 1 
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap operation
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1 
            
        print(f"Pass {i+1}: {arr}")
    
    print(f"Sorted list: {arr}") 
    print(f"Total comparisons: {comparisons}") 
    print(f"Total swaps: {swaps}") 
    return arr

# Task 3: Create Index Table
def create_index_table(arr, block_size):
    index_table = []
    # Select first element of each block 
    for i in range(0, len(arr), block_size):
        # Store selected value and its position 
        index_table.append((arr[i], i))
    
    print("\nIndex table created:") 
    for val, pos in index_table:
        print(f"{val} -> {pos}") 
    return index_table

# Task 4 & 5: Indexed Search Implementation
def indexed_search(arr, index_table, key):
    print(f"\nSearch key: {key}") 
    imin = 0
    imax = len(arr) - 1
    found_range = False

    # 1. Search index table to determine possible range 
    for i in range(len(index_table)):
        if index_table[i][0] <= key:
            imin = index_table[i][1] 
            if i + 1 < len(index_table):
                imax = index_table[i+1][1] - 1 
            else:
                imax = len(arr) - 1 
            found_range = True
        else:
            break

    if not found_range:
        print(f"{key} not found")
        return -1

    # Printing range in the format required by instructions [cite: 90, 103]
    # Note: imax+1 is used here just to show the boundary of the next block
    upper_bound = arr[imax+1] if imax+1 < len(arr) else "End"
    print(f"Index range found:")
    print(f"{arr[imin]}<={key}<{upper_bound}") 
    print(f"Searching from index {imin} to index {imax}:") 

    # 2. Search sequentially inside selected range 
    for idx in range(imin, imax + 1):
        print(f"Checking index {idx}: {arr[idx]}") 
        if arr[idx] == key:
            print(f"{key} found at index {idx}") 
            return idx
    
    print(f"{key} not found") 
    return -1

# --- EXECUTION ---

# Testing Selection Sort (Tasks 1 & 2)
sample_arr = [29, 10, 14, 37, 13] 
selection_sort(sample_arr)

# Testing Indexed Search (Tasks 3, 4, & 5)
sorted_arr = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65] 
idx_tbl = create_index_table(sorted_arr, 3) 

# Task 4: Key Found
indexed_search(sorted_arr, idx_tbl, 45) 

# Task 5: Key Not Found
indexed_search(sorted_arr, idx_tbl, 43) 

