my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

# lista noua sortata
asc_list = my_list.copy()
asc_list.sort()
print('Crescator: ', asc_list)

# lista sortata descendent
desc_list = list(my_list)
desc_list.sort(reverse=True)
print('Descrescator: ', desc_list)

# elementele pare
print('Elemente pare: ', asc_list[1::2])

# elementele impare
print('Elemente impare: ', asc_list[0::2])

# elemente ce se impart la 3
print('Elemente multiple de 3: ', asc_list[2::3])
