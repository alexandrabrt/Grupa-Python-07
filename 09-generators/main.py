# def letter_printer():
#     print('letter_printer has been called ...')
#     print('Yielding A ...')
#
#     yield 'A'
#     print('Yielding B ...')
#     yield 'B'
#     print('Yielding c ...')
#     yield 'C'
#     print('letter_printer has called it a day!')

# print(letter_printer)
# lprinter = letter_printer()
# print(lprinter)
#
# # lprinter()
# # A
# print(next(lprinter))
#
# # B
# letter_b = next(lprinter)
# print(letter_b)
#
# # C
# print(next(lprinter))


# next(lprinter)
# next(lprinter)

# print(lprinter)
#
# new_lprinter = letter_printer()
# print("my letters\n")
# for letter in new_lprinter:
#     print(">>> {}\n".format(letter))

# letter_list = [letter for letter in letter_printer()]
# print(letter_list)


# def number_printer(max_number=10):
#     print('number_printer has been called ...')
#     for number in range(1, max_number):
#         print(number)
#
# number_printer()
#
# from pympler import asizeof
# numbers = [x for x in range(10)]
# print(asizeof.asized(numbers, detail=2).format())
#
# def number_printer_generator(max_number=10):
#     print('number_printer has been called ...')
#     for number in range(1, max_number):
#         print(number)
#         yield number
#
#
# gen = number_printer_generator()
# print(asizeof.asized(gen, detail=2).format())

# from arithmetic_progression import arithmetic_progression as arith_prog
# integers = arith_prog(0, 1, 5)
# print(list(integers))
#
#
# decimals = arith_prog(0, 0.25, 5)
# print(next(decimals))
# print(next(decimals))
#
# sample = [next(decimals) for _ in range(5)]
# print(sample)

# def is_even(number):
#     return number % 2 == 0
#
#
# def filter_even(iterable):
#     for item in iterable:
#         if is_even(item):
#             yield item
#
# numbers = list(range(10))
# print(numbers)
#
# even = filter_even(numbers)
# print(even)
#
# print(len(numbers))
#
# print([next(even) for _ in range(4)])
# numbers.extend(list(range(10, 20)))
# print(numbers)
#
# print([next(even) for _ in range(6)])
#
# numbers.extend(list(range(20, 30)))
# print(numbers)
#
# print(next(even))
#
#
# print('new generator', list(filter_even(numbers)))
#
# print(next(even))


# import itertools
# def is_even(number):
#     return number % 2 == 0
#
# numbers = list(range(10))
# print('numbers >> {}'.format(numbers))
# builtin_filter = filter(is_even, numbers)
# print('builtin_filter >> {}'.format(builtin_filter))
# builtin_filter = list(builtin_filter)
# print('builtin_filter >> {}\n'.format(builtin_filter))
#
# print('numbers >> {}'.format(numbers))
# filterfalse = itertools.filterfalse(is_even, numbers)
# print('filterfalse >> {}'.format(filterfalse))
# filterfalse = list(filterfalse)
# print('filterfalse >> {}\n'.format(filterfalse))
#
#
# # dropwhile
# print('numbers >> {}'.format(numbers))
# dropwhile = list(itertools.dropwhile(is_even, numbers))
# print('dropwhile >> {}\n'.format(dropwhile))
#
# print('numbers >> {}'.format(numbers))
# dropwhile = list(itertools.dropwhile(lambda x: x > 5, numbers))
# print('dropwhile >> {}\n'.format(dropwhile))
#
# # takewhile
# print('numbers >> {}'.format(numbers))
# takewhile = list(itertools.takewhile(is_even, numbers))
# print('takewhile >> {}\n'.format(takewhile))
#
# print('numbers >> {}'.format(numbers))
# takewhile = list(itertools.takewhile(lambda x: x > 5, numbers))
# print('takewhile >> {}\n'.format(takewhile))

# builtin enumerate function
# sequence = 'Python is cool!'
# print('sequence >> {}'.format(sequence))
# enum = list(enumerate(sequence, 0))
# print('enumerate >> {}\n'.format(enum))
#
# enum1 = list(enumerate(sequence, 1))
# print('enumerate >> {}\n'.format(enum1))
#
# for index, value in enumerate(sequence, 1):
#     print(f"Index: {index} Value: {value}")

# builtin map function
# print('numbers >> {}'.format(numbers))
# squared = list(map(lambda x: x * x, numbers))
# print('squared >> {}\n'.format(squared))
#
import operator
# print('numbers >> {}'.format(numbers))
# multiplied = list(map(operator.mul, numbers, squared))
# print('multiplied >> {}\n'.format(multiplied))

# itertools accumulate
# print('numbers >> {}'.format(numbers))
# accumulated = list(itertools.accumulate(numbers))
# print('accumulated >> {}\n'.format(accumulated))
#
# print('numbers >> {}'.format(numbers))
# accumulated_min = list(itertools.accumulate(numbers, min))
# print('accumulated_min >> {}\n'.format(accumulated_min))
#
# print('numbers >> {}'.format(numbers))
# accumulated_max = list(itertools.accumulate(numbers, max))
# print('accumulated_max >> {}\n'.format(accumulated_max))
#
# print('numbers >> {}'.format(numbers))
# accumulated_multi = list(itertools.accumulate(numbers[1:], operator.mul))
# print('accumulated_multi >> {}\n'.format(accumulated_multi))
#
# import functools
# print('numbers >> {}'.format(numbers))
# reduceresult = functools.reduce(operator.mul, numbers[1:])
# print('reduceresult >> {}\n'.format(reduceresult))

import itertools
numbers = list(range(10))
sequence = 'Python is cool!'
# built-in zip
# print('numbers >> {}'.format(numbers))
# zipped = list(zip(sequence, numbers))
# print('zipped >> {}\n'.format(zipped))

# itertools chain
print('numbers >> {}'.format(numbers))
print('sequence >> {}'.format(sequence))
chain = list(itertools.chain(sequence, numbers))
print('chain >> {}\n'.format(chain))
