# def my_initial_func(msg):
#     print(msg)

# def another_function(function_param):
#     function_param('Hello, Python!')
#
# another_function(my_initial_func)
#
# def another_function():
#     return my_initial_func
#
#
# another_function()('Hello, One Line!')
# # echivalent cu
# my_var = another_function()
# my_var('Hello, Python!')
# # echivalent cu
# my_var = my_initial_func
# my_var('Hello, Python!')
# # echivalent cu
# my_initial_func('Hello, Python!')


# def sum_from_args(*args):
#     return sum(args)

def sum_decorator(function_to_decorate):
    def wrapper(*args):
        print('Before function call ...')
        function_result = function_to_decorate(*args)
        print('After function call ...')

        return function_result

    return wrapper
#
# my_sum = sum_from_args(1, 2, 3, 4, 5)
# print(my_sum)
#
#
# my_sum = sum_decorator(sum_from_args)(1, 2, 3, 4, 5)
# # echivalent cu
# decorated_sum_from_args = sum_decorator(sum_from_args)
# my_sum = decorated_sum_from_args(1, 2, 3, 4, 5)
# print(my_sum)

from functools import wraps

def multiply_by_decorator(number):
    def function_wrapper(function_to_decorate):
        @wraps(function_to_decorate)
        def wrapper(*args):
            """
            Wrapper documentation
            """

            print('Before function call ...')
            function_result = function_to_decorate(*args)
            print('After function call ...')

            return function_result * number

        return wrapper

    return function_wrapper


# decorated_function_wrapper = multiply_by_decorator(3)
# decorated_sum_from_args = decorated_function_wrapper(sum_from_args)
# my_sum = decorated_sum_from_args(1, 2, 3, 4, 5)
# # echivalent cu
# my_sum = multiply_by_decorator(3)(sum_from_args)(1, 2, 3, 4, 5)
#
# print(my_sum)

# @sum_decorator
# def sum_from_args(*args):
#     return sum(args)

# decorated_sum_from_args = sum_decorator(sum_from_args)
# my_sum = decorated_sum_from_args(1, 2, 3, 4, 5)
# print(my_sum)

# my_sum = sum_from_args(1, 2, 3, 4, 5)
# print(my_sum)
# @multiply_by_decorator(3)
# def sum_from_args(*args):
#     """
#     Returns the sum of the arguments
#     :param args: list of params to sum
#     :return: sum of params
#     """
#
#     return sum(args)

# my_sum = sum_from_args(1, 2, 3, 4, 5)
# print(my_sum)

# print(sum_from_args.__name__)
# print(sum_from_args.__doc__)
#
# print(sum_from_args(1, 2, 3, 4, 5))
# print(sum_from_args.__wrapped__(1, 2, 3, 4, 5))

import time

def time_decorator(my_func):
    def wrapper(*args, **kwargs):
        start = time.time()
        my_func_result = my_func(*args, **kwargs)
        end = time.time()
        duration = end - start
        print(f'The function call took {duration} miliseconds')

        return my_func_result

    return wrapper


@time_decorator
def sum_from_args(range_end, range_start=0):
    print(f'range_start={range_start}')
    sum = 0
    for number in range(range_start, range_end):
        sum += number

    return sum

my_sum = sum_from_args(10000, range_start=15)
print(my_sum)
