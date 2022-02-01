class User:
    name = 'Generic Name'
    phone = '+xx xxxx xxx xxx'
    role = None
    _education = 'University of Ausonia'

    def __init__(self, **kwargs):
        self.name = kwargs.get('name', self.name)
        self.phone = kwargs.get('phone', self.phone)
        self.role = kwargs.get('role', self.role)
        self.age = kwargs.get('age', None)

    @property
    def education(self):
        return self._education

    @property
    def is_legal_to_drink(self):
        if self.age:
            return self.age > 18
        else:
            return False

    def user_info(self):
        print(f'User {self.name} with phone: {self.phone}\n'
        f'in the role of {self.role if self.role else "Undefined"}\n'
        f'and it is {"legal" if self.is_legal_to_drink else "ilegal"} for him/')


instance_of_User1 = User(name='John', phone='+40 0101 010 010', role='admin', age=21)
instance_of_User2 = User(name='Mark')
instance_of_User1.user_info()
instance_of_User2.user_info()

