# numar = 5
# if numar % 2 == 0:
#     print("Numarul este par!")
# elif numar < 5:
#     print("Numarul este < 5!")
# elif numar > 5:
#     print("Numarul este > 5!")
# else:
#     print("Numarul este 5")

# numar = 7
# while numar > 5:
#     if numar % 2 == 0:
#         print("Numarul este par!")
#     print(f"{numar} mai mare de 5")
#     numar -= 1
#
# print("End program")

# print(range(1, 5), type(range(1, 5)))
# my_list = [4, 5, 6, 7]
# for elem in my_list:
#     print(elem)
# my_range = range(1, 10)
# my_list = list(my_range)
# my_range.append([1, 2])
# my_list.append([1, 2])
# print(my_list)

# my_dict = {
#     1: 'a',
#     2: 'b',
#     3: 'c'
# }
# for key in my_dict.keys():
#     print(key)
#
# for value in my_dict.values():
#     print(value)
#
# for key, value in my_dict.items():
#     print(f"Key {key} => value {value}")
#
# print(list(my_dict.items()))
# for item in my_dict.items():
#     print(item)
#
# for elem in range(1, 10, 2):
#     print(elem)

# numar = 7
# while numar > 5:
#     print("Iteration #")
#     if numar % 5 == 0:
#         break
#
#     numar += 1
#
#     if numar % 2 == 0:
#         continue
#
#     print("Nu se executa la continue")
#
# print("End program")

# while True:
#     pass
#
# if numar > 5:
#     pass
# elif numar > 2:
#     pass
# else:
#     pass

# numar = int(input("Give me a number: "))
#  print("Numarul introdus este: ", numar)
#
# while numar > 5:
#     print(f"Repeat {numar}")
#     numar -= 1

# def hello():
#     print("Hello, world!")
#
# hello()
#
# def my_sum(var1, var2):
#     return var1 + var2
#
# print(my_sum(1, 2))
# sum_result = my_sum(2, 3)
# print(sum_result)

# def operation(var1, var2, operator='+'):
#     if operator == '+':
#         return var1 + var2
#
#     if operator == '*':
#         return var1 * var2
# print(operation(1, 2))
# print(operation(1, 2, '*'))

# def operation2(var1, *args, cheie=14, **kwargs):
#     print(var1)
#     print(cheie)
#     print(args)
#     print(kwargs)
#
# print(operation(2,4, operator='*'))
# operation2(2, 3, 5, cheie=10, cheie2=30)

# def func(my_list):
#     my_list = [1, 2, 3]
#     my_list[0] = 'a'
#
# my_list = [1, 2, 3, 4]
# func(my_list)
# print(my_list)

def recursive_sum(n):
    if n == 0:
        return n

    return n + recursive_sum(n-1)
