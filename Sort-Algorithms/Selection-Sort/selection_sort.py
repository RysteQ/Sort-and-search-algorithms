def selection_sort(array):
    for i in range(len(array)):
        minimum = i

        for j in range(i + 1, len(array), 1):
            if array[j] < array[minimum]:
                minimum = j

        if minimum != i:
            array[i], array[minimum] = array[minimum], array[i]

    return array