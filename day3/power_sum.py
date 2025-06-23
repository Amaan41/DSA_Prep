def power_sum(array, power=1):
    total = 0
    for i in array:
        if isinstance(i, int):
            total += i
        elif isinstance(i, list):
            total += power_sum(i, power + 1)
    return total ** power

print(power_sum([2, 3, [4, 1, 2]]))
