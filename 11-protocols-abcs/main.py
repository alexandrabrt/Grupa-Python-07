from utils import print_header
from crayons_box import crayons_box

print_header('__len__')
print(len(crayons_box))

print_header('__getitem__')
print(crayons_box[2])

print_header('__contains__')
if 'Blue' in crayons_box:
    print('Blue crayon is in the crayon box')

print_header('__iter__')
for crayon in crayons_box:
    print(crayon)