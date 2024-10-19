def remove_duplicates(arr):
    if not arr:
        return 0

    # Pointer for the next unique element
    unique_index = 1

    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            arr[unique_index] = arr[i]
            unique_index += 1

    return unique_index  # Length of the array without duplicates

# Example usage
arr = [1, 1, 2, 2, 3, 4, 4]
length = remove_duplicates(arr)
print(arr[:length]) 