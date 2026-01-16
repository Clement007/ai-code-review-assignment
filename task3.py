def sum_positive_numbers(numbers):
    total = 0

    for n in numbers:
        if n > 0:
            total += n

    return total
