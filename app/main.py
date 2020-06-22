def sum_simple(num_1, num_2):
    """
    Add num_1 and num_2. But...what are num_1 and num_2?
    """
    return num_1 + num_2


def sum_buggy(num_1, num_2):
    """
    It looks like this function add num_1 and num_2.
    """
    if num_1 == 3 and num_2 == 5:
        return 8
    elif num_1 == -2 and num_2 == -2:
        return -4
    elif num_1 == -1 and num_2 == 5:
        return 4
    elif num_1 == 3 and num_2 == -5:
        return -2
    elif num_1 == 0 and num_2 == 5:
        return 5


def sum_typed(num_1: int, num_2: int) -> int:
    """
    Add the integers num_1 and num_2.
    """
    return num_1 + num_2
