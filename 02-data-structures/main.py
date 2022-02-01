# my_list = []
# my_list = list()
# my_list = [1, 2, 3.5, 3+6j, "Lenny", False, True, None, [1, 2, 3]]
#            0  1  2    3     4        5      6     7     8
#            -9 -8 -7   -6    -5       -4     -3    -2    -1

# print(type(my_list))
# print(my_list[0])
# print(my_list[1])
# print(my_list[2])
# print(my_list[6])
# print(my_list[8][0])
# print(my_list[8][2])
# print(my_list[8])
# print(my_list[-1])
# print(my_list[-9])
# print(len(my_list), type(len(my_list)))
# print(my_list[len(my_list) // 2])
# index = 8
# print(my_list[index])

# list[index_start:index_end:step]
# my_list = [1, 2, 3.5, 3+6j, "Lenny", False, True, None, [1, 2, 3]]
# print(my_list[1:])
# print(my_list[1:5])
# print(my_list[1:7:2])
# print(my_list[5:1:-1])
# print(my_list[::-1])

# my_name = "Lenny"
# print(len(my_name))
# print(my_name[1])
# print(my_name[1:4])
# print(my_name[::-1])

# my_list = ['a', 'b']
# print(my_list * 6)
# print(my_name * 6)

# my_list = [1, 2, 3, -1, 4, 6, 10]
# print(min(my_list))
# my_list = ['a', 'r', 't']
# print(max(my_list))

# print(my_list.index(1))
# my_list.append(11)
# my_list.insert(1, 'a')
# my_list.remove(2)
# my_list.pop(1)
# my_list.clear()

# my_list = [1, 2, 3, -1, 4, 6, [0, 1]]
# new_list = my_list.copy()
# print(my_list)
# my_list[-1][1] = 'a'
# print(new_list)

# my_list = [1, 2, 3, -1, 4, 6, [0, 1]]
# import copy
# new_list = copy.deepcopy(my_list)
# my_list[-1][1] = 'a'
# print(my_list)
# print(new_list)

# my_list.reverse()
# print(my_list)

# my_name = "Lenny"
# my_name[1] = '2'
# my_list1 = [1, 2]
# my_list2 = [3, 4]
# print(my_list1 + my_list2)
# print(my_list1)

# my_list1.extend(my_list2)
# my_list1 += my_list2
# my_list1 = my_list1 + my_list2
# print(my_list1)

# my_list = [1, 2, 3, -1, 4, 6, 10]
# my_list.sort()
# print(my_list)

# my_tuple = (1, 2, 'Lenny', [1,2])
# print(id(my_tuple))
# my_tuple1 = (1, 2)
# my_tuple2 = (3, 4)
# print(my_tuple1 + my_tuple2)
# my_list = list(my_tuple)
# print(my_list, type(my_tuple), type(my_list))
# my_list.append('a')
# my_tuple = tuple(my_list)
# print(my_tuple)
# print(id(my_tuple))

# my_tuple = (1, 2, "Lenny")
# var1, var2, nume = my_tuple
# print(var2, nume)

# my_dict = {
#     'a': 1,
#     'b': 2,
#     'c': 3
# }
# print(my_dict, type(my_dict))
# print(my_dict['a'])

# var = 5
# my_list = [1, 2, 3]
# print(var in my_list)

# print('d' in my_dict)
# print(my_dict['d'])
# print(my_dict.get('d', "Nu exista"))

# my_dict['a'] = 'Lenny'
# my_dict.clear()

# my_dict = {
#     'a': 1,
#     'b': 2,
#     'c': 3
# }
# dict_keys = my_dict.keys()
# print(dict_keys, type(dict_keys))
# key_list = list(dict_keys)
# print(key_list, type(key_list))

# dict_values = my_dict.values()
# print(dict_values, type(dict_values))
# values_list = list(dict_values)
# print('a' in values_list)

# dict_items = my_dict.items()
# print(dict_items, type(dict_items))

# my_dict.pop('a')
# print(my_dict)

# my_dict['a'] = 0
# my_dict['d'] = 'd'
# print(my_dict)

# my_dict = {'a': [{'key': 1}, {'key2': 212}], 'b': {'key': 232, 'key4': [1, 2, 3]}, 'c': 3}
#
# import pprint
# pprint.pprint(my_dict)
#
# pp = pprint.PrettyPrinter(indent=2)
# pp.pprint(my_dict)

# my_set = {1, 2, 3, 4, 5, 6}
# print(my_set, type(my_set))
# my_set.discard(8)
# my_set.clear()
# print(my_set)

# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# print(set1.intersection(set2))
# print(set1.union(set2))

set1 = {1, 2, 3, 4}
set2 = {2, 3}
print(set1.issuperset(set2))
print(set2.issubset(set1))
print(set1.difference(set2))
