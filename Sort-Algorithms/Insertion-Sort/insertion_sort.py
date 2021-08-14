def insertion_sort(array):
    for i in range(len(array)):
        current = array[i]
        toSwap = i - 1

        while toSwap >= 0 and current < array[toSwap]:
            array[toSwap + 1] = array[toSwap]
            toSwap = toSwap - 1

        array[toSwap + 1] = current

    return array