"""Part 1"""
def sequential_search(arr, target):
    """
    Returns index and number of comparisons.
    """
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons
    return -1, comparisons

# --- Logic to match the exact output ---
data_list = [23, 45, 12, 67, 89, 34, 56]
target_value = 67

# 1. Print the initial list
print(f"List: {data_list}")

# 2. Print what is being searched for [cite: 30]
print(f"Searching for {target_value} using Sequential Search")

# 3. Perform the search
index, num_comparisons = sequential_search(data_list, target_value)

# 4. Print the result and comparison count 
if index != -1:
    print(f"Found at index {index}")
else:
    print("Not found")

print(f"Number of comparisons: {num_comparisons}")

"""Part 2"""
def binary_search(arr, target):
    comparisons = 0
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        comparisons += 1
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid, comparisons  # Target found at index mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1, comparisons  # Target not found

# --- Part 2 Example Usage ---
# Binary search requires the data to be sorted [cite: 14]
sorted_test_list = [12, 23, 34, 45, 56, 67, 89]
target_val = 67

index, count = binary_search(sorted_test_list, target_val)

print("--- Binary Search ---")
print(f"Sorted List: {sorted_test_list}")
print(f"Searching for {target_val} using binary search")
if index != -1:
    print(f"Found at index {index}")
else:
    print("Not found")
print(f"Number of comparisons: {count}")