def binary_search(numbers, to_find):
    low = 0
    high = len(numbers) - 1
    while low <= high:
        mid = (low + high) // 2
        if numbers[mid] == to_find:
            return mid
        if numbers[mid] > to_find:
            # exclude upper half
            high = mid - 1
        else:
            # exclude lower half
            low = mid + 1
    return None

