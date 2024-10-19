def is_sorted_and_rotated(arr):
    n = len(arr)
    if n == 0:
        return False

    # Find the index of the pivot point
    pivot_index = -1
    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            pivot_index = i
            break

    # If no pivot is found, the array is sorted
    if pivot_index == -1:
        return True

    # Check if the two parts are sorted
    # Part 1: arr[0] to arr[pivot_index - 1]
    for i in range(1, pivot_index):
        if arr[i] < arr[i - 1]:
            return False

    # Part 2: arr[pivot_index] to arr[n - 1]
    for i in range(pivot_index + 1, n):
        if arr[i] < arr[i - 1]:
            return False

    # Finally, check if the last element is greater than the first element
    if arr[n - 1] > arr[0]:
        return False

    return True

# Example usage
arr = [4, 5, 1, 2, 3]
print(is_sorted_and_rotated(arr))  