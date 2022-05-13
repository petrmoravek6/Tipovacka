def is_positive_integer(number):
    if isinstance(number, float):
        return False
    try:
        val = int(number)
        if val < 0:
            return False
    except ValueError:
        return False
    return True
