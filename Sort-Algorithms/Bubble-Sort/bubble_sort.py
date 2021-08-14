def bubble_sort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - 1, i, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]

    return array

print(bubble_sort([13,654,234,786,3242,765,342,1321,99,0,5,43,246,2]))