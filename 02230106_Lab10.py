#PART 1
def counting_sort(arr):
    if not arr:
        return arr
    
    # Find the range of the input
    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1
    
    # Initialize count and output arrays
    count = [0] * range_of_elements
    output = [0] * len(arr)
    
    # 1. Store the frequency of each element 
    for num in arr:
        count[num - min_val] += 1
        
    # 2. Update count[i] so it contains actual position in output
    for i in range(1, len(count)):
        count[i] += count[i-1]
        
    # 3. Build the output array (handles duplicate values) [cite: 34]
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i] - min_val] - 1] = arr[i]
        count[arr[i] - min_val] -= 1
        
    return output

# Example Usage [cite: 36]
arr = [4, 2, 2, 8, 3, 3, 1]
print(f"Counting Sort Output: {counting_sort(arr)}")

#Part 2
def radix_sort(arr):
    if not arr:
        return arr
        
    # Find the maximum number to know number of digits 
    max_val = max(arr)
    
    # Perform counting sort for every digit. 
    # 'exp' is 10^i where i is the current digit position
    exp = 1
    while max_val // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10
    return arr

def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # Base 10 for digits 0-9
    
    # Store count of occurrences
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
        
    # Change count[i] to actual positions
    for i in range(1, 10):
        count[i] += count[i-1]
        
    # Build the output array
    for i in range(n - 1, -1, -1):
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        
    # Copy output to original array
    for i in range(len(arr)):
        arr[i] = output[i]

# Example Usage [cite: 46]
arr_radix = [170, 45, 75, 90, 802, 24, 2, 66]
print(f"Radix Sort Output: {radix_sort(arr_radix)}")