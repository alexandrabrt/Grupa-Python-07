from decorators import multiply_by_decorator


def test_multiply_by_decorator():
    decorated_function = multiply_by_decorator(3)(lambda: 15)
    result = decorated_function()
    assert result == 45
