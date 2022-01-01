def range_sum(numbers, start, end):
    # Python way
    # return sum(filter(lambda x: start <= x <= end, numbers))
    total = 0
    for num in numbers:
        if start <= num <= end:
            total += num
    return total


input_numbers = [int(number) for number in input().split()]
a, b = [int(number) for number in input().split()]
print(range_sum(input_numbers, a, b))
