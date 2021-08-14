def step_search(array, element, step):
    temp = 0

    for i in range(0, len(array), step):
        if array[i] == element:
            return True, i
        elif array[i] > element:
            for j in range(i - step + 1, i, 1):
                if array[j] == element:
                    return True, j

        temp = i

    for i in range(temp, len(array), 1):
        if array[i] == element:
            return True, i

    return False, -1