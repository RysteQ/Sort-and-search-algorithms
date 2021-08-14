def binary_search(array, element):
    first = 0
    last = len(array) - 1

    while first <= last:
        mid = (first + last) // 2

        if array[mid] == element:
            return True, mid
        elif array[mid] < element:
            first = mid + 1
        else:
            last = mid - 1

    return False, -1