def arithmetic_progression(begin, step, end=None):
    result = type(begin + step)(begin)
    forever = True if end is None else False

    index = 0
    while forever or result < end:
        yield result
        index += 1
        result = begin + step * index