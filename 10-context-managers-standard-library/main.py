# with open('file_with_text.txt') as file:
#     chars = file.read(25)
#
# print(len(chars), chars)
# print('-' * 50)
# print(file)
# print('-' * 50)
# print(file.closed, file.encoding)


# class LookingGlass:
#     def __enter__(self):
#         import sys
#         self.original_write = sys.stdout.write
#         sys.stdout.write = self.reverse_write
#         return 'I am just a string object'
#
#     def reverse_write(self, text):
#         self.original_write(text[::-1])
#
#     def __exit__(self, exc_type, exc_value, traceback):
#         import sys
#
#         sys.stdout.write = self.original_write
#         if exc_type is ZeroDivisionError:
#             print('Please DO NOT divide by zero!')
#             return True
#
#
# with LookingGlass() as mirror:
#     x = 2 / 0
#     print('What happened to this text')
#     print(mirror)
#
# print('-' * 50)
# print(mirror)
# print('No more mirror')


# looking_glass = LookingGlass()
# looking_glass.__enter__()
# print(looking_glass.reverse_write('My text'))
# looking_glass.__exit__(None, None, None)
# print('After exit')

# import contextlib
#
# @contextlib.contextmanager
# def looking_glass():
#     import sys
#     original_write = sys.stdout.write
#     def reverse_write(text):
#         original_write(text[::-1])
#
#     sys.stdout.write = reverse_write
#     error_message = ''
#     try:
#         yield 'I am just a string object'
#     except ZeroDivisionError:
#         error_message = 'Please DO NOT divide by zero!'
#     finally:
#         sys.stdout.write = original_write
#         if error_message:
#             print(error_message)
#
#
# with looking_glass() as mirror:
#     x = 2 / 0
#     print('What happened to this text')
#     print(mirror)
#
# print(mirror)
# print('No more mirror')


# try:
#     print(var)
#     fp = open('dsdsds')
# except ZeroDivisionError:
#     print('Please DO NOT divide by zero!')
# except NameError:
#     print('This is a name error')
# finally:
#     fp.close()


# class Indenter():
#
#     def __init__(self):
#         self.indent = 1
#
#     def __enter__(self):
#         self.indent += 1
#         return self
#
#     def __exit__(self, et, e, st):
#         self.indent -= 1
#         return True
#
#     def print(self, msg):
#         print("  " * self.indent, msg)
#
#
# with Indenter() as indent:
#     indent.print("Level1")
#
#     with indent:
#         indent.print("Level2")
#
#         with indent:
#             indent.print("Level3")
#
#     indent.print("Level1")


# import re
# text_input = 'This is a random text'
# pattern = r'random'
# match = re.search(pattern, text_input)
# start_index = match.start()
# end_index = match.end()
# print(f'Found {match.re.pattern} pattern in \"{match.string}\" => \"{match.group(0)}\" between indices ({start_index}, {end_index})')
#
#
# import re
# text_input = 'This is a random'
# pattern = r'random\s(\w+)'
# compiled_regex = re.compile(pattern)
# match = re.search(compiled_regex, text_input)
# print(match.group(0),'|', match.group(1))


# import re
# text_input = 'This is a random text. This is a random another. ' * 20
# pattern = r'(random)\s(\w+)\.'
# print(text_input)
# for match in re.findall(pattern, text_input):
#     print(match)


# import re
# text_input = 'This is a random text. ' * 20
# pattern = r'(random)\s(\w+)\.'
# print(text_input)
# for match in re.finditer(pattern, text_input):
#     print(match)


# from functools import partial
# def multiply(number, by=2, print_only=False):
#     if not print_only:
#         return number * by
#
#     print(f'The result of the multiplication is: {number * by}')
#
# print(multiply(4), multiply(3, by=3))
# multiplier_by_4 = partial(multiply, by=4, print_only=True)
# multiplier_by_5 = partial(multiply, by=5, print_only=True)
# multiplier_by_4(4)
# multiplier_by_5(2)

# from functools import partial
# basetwo = partial(int, base=2)
# print(int('100'))
# print(basetwo('100'))

# import random
#
# for _ in range(5):
#     print(random.random())
#
# for _ in range(5):
#     print(random.randint(1,100))
#
#
# import random
# outcomes = {
#     'heads': 0,
#     'tails': 0,
# }
# sides = list(outcomes.keys())
# for i in range(10000):
#     outcomes[random.choice(sides)] += 1
# print('Heads:', outcomes['heads'])
# print('Tails:', outcomes['tails'])


# import requests
# import textwrap
# response = requests.get('https://www.google.ro/')
# print(response.status_code)
# print('-' * 40)
# print(response.headers)
# print('-' * 40)
# print(textwrap.shorten(response.text, width=250))