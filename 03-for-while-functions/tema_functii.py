# 1
def sum_numbers(*args, **kwargs):
    number_sum = 0
    for number in args:
        if type(number) == int or type(number) == float:
            number_sum += number

    return number_sum


print(sum_numbers(1, 5, -3, 'abc', [12, 56, 'cad']))
print(sum_numbers())
print(sum_numbers(2, 4, 'abc', param_1=2))


# 2
def sum_recursive(n):
    if n == 0:
        return 0, 0, 0

    sum_n, sum_odd, sum_even = sum_recursive(n-1)
    sum_n += n
    if n % 2 == 0:
        sum_even += n
    else:
        sum_odd += n

    return sum_n, sum_odd, sum_even


print(sum_recursive(6))


# 3
def get_input():
    user_input = input('Show me the number: ')
    try:
        return int(user_input)
    except ValueError:
        return 0


print(get_input())