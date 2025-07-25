def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Track if any swapping happens in this pass
        swapped = False
        for j in range(0, n - i - 1):
            # Swap if elements are in the wrong order
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no elements were swapped, array is already sorted
        if not swapped:
            break
    return arr
