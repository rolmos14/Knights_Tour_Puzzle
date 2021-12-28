def last_indexof_max(numbers):
    index_max = -1
    for i in range(0, len(numbers)):
        if numbers[i] >= numbers[index_max]:
            index_max = i
    return index_max
