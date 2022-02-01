# my_lambda = lambda x, y: x + y
# def my_lambda(x, y):
#     return x + y

# def a(x):
#     return x + x
#
# def b(x):
#     return x * x
#
# print(id(a))
# print(id(b))
# print(id(lambda x: x+x))
# print(id(lambda x: x*x))

# my_dict_list = [
#     {
#         'nume': 'Lenny',
#         'varsta': 34
#     },
#     {
#         'nume': 'Simona Halep',
#         'varsta': 30
#     }
# ]
#
# def get_key(my_dict):
#     return my_dict.get('varsta')
#
# my_dict_list.sort(key=get_key)
#
# my_dict_list.sort(key=lambda d: d.get('varsta'))
# print(my_dict_list)
# sorted(my_dict_list, key=lambda d: d.get('varsta'))

# students = [
#     {
#         'nume': 'Lenny',
#         'nota': 10
#     },
#     {
#         'nume': 'Simona Halep',
#         'nota': 4
#     },
#     {
#         'nume': 'NoName',
#         'nota': 3
#     }
# ]

# def update_student(student):
#     nota = student.get('nota', 0)
#
#     student['nota'] = nota
#     return student
#
# print(list(map(update_student, students)))
#
# my_list = [1, 2, 3, 4, 5]
# result = map(lambda elem: elem * elem, my_list)
# print(list(result))
#
# def filter_students(student):
#     if student.get('nota') < 5:
#         return True
#
#     return False
#
# students_admisi = filter(filter_students, students)
# print(list(students_admisi))
#
# students_admisi = filter(lambda s: s.get('nota') < 5, students)
# print(list(students_admisi))

# my_list1 = ['Halep', 'Simona', 30]
# my_list2 = ['Nume', 'Prenume', 'Varsta']
# for elem1, elem2 in zip(my_list1, my_list2):
#     print(elem1)
#     print(elem2)

# from itertools import zip_longest
# my_list1 = [1, 2, 3, 4]
# my_list2 = ['a', 'b', 'c']
# print(list(zip_longest(my_list1, my_list2, fillvalue='d')))
# print(zip(my_list1, my_list2))

# my_list = [1, 2, 3, 4, 5]
# my_new_list = [elem * elem for elem in my_list]
# my_odd_list = [elem for elem in my_list if elem % 2 == 1]
# my_new_list_2 = [0 if elem % 2 == 0 else elem for elem in my_list]
# print(my_new_list)
# print(my_odd_list)
# print(my_new_list_2)

# without comprehension
# new_list = []
# for elem in my_list:
#     if elem % 2 == 0:
#         new_list.append(0)
#     else:
#         new_list.append(elem)
#

# my_keys = [1, 2, 3, 4, 5]
# my_values = ['a', 'b', 'c', 'd', 'e']
# # my_tuples = [(1, 'a') ...]
# d = {
#     key: value for key, value in zip(my_keys, my_values)
# }
#
# print(d)
# new_dict = {
#     key*2: value for key, value in d.items()
# }
# print(new_dict)

# file = open('data_new.txt', 'w')
# file.write('Hello, files new content!')
# file.close()

# with open('data.txt', 'w') as fisierul_meu:
#     fisierul_meu.write('File content!')

# with open('data_cars.csv', 'r') as fisierul_meu:
#     for line in list(fisierul_meu):
#         print('Line: ', line)
#
# import csv
# with open('data_cars.csv', 'r') as fisierul_meu:
#     rows = csv.reader(fisierul_meu, delimiter=',')
#     for row in rows:
#         print('line', row)
#
# cars = [
#     ['Dacia', 'Logan', 2005, 75],
#     ['Dacia', 'Sandero', 2010, 76]
# ]
#
# with open('data_cars.csv', 'a') as fisierul_meu:
#     csv_writer = csv.writer(fisierul_meu, delimiter=',')
#     for car in cars:
#         csv_writer.writerow(car)

import os

for dir_item in os.scandir():
    if os.path.isfile(dir_item):
        print(f"{dir_item} is a file")
    else:
        print(f"{dir_item} is a directory")
