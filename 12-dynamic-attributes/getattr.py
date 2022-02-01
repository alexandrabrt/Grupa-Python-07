class User:
    name = 'Generic Name'
    phone = '+xx xxxx xxx xxx'
    role = None
    myAge = 34
    yourAge = 100


user = User()
print(user.name, user.phone, user.role)
print('-' * 100)
# print(user.job)

my = 'my'
age = 'Age'

attrs = ['name', 'role', my+age]
for attr in attrs:
    print(getattr(user, attr, 'No field was found'))

print(getattr(user, 'job', 'No field was found'))
print(getattr(user, 'job', 'Default value for user'))

