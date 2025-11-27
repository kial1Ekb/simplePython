def sum_distance(from_val, to_val):
    """
    Суммирует все числа от from_val до to_val включительно.
    Если from_val > to_val, меняет их местами.
    """
    if from_val > to_val:
        from_val, to_val = to_val, from_val
    return sum(range(from_val, to_val + 1))


if __name__ == "__main__":
    print(sum_distance(1, 5))
    print(sum_distance(5, 1))
    print(sum_distance(-2, 2))
