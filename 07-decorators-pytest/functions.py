from decorators import multiply_by_decorator


@multiply_by_decorator(3)
def sum_from_args(*args):
    """
    Returns the sum of the arguments
    :param args: list of params to sum
    :return: sum of params
    """
    my_sum = 0

    for value in args:
        my_sum += value

    return my_sum