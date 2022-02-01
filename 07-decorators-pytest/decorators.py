from functools import wraps


def sum_decorator(function_to_decorate):
    def wrapper(*args):
        print('Before function call ...')
        function_result = function_to_decorate(*args)
        print('After function call ...')

        return function_result

    return wrapper


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