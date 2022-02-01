# %load property_1.py
class User:
    _lastname = 'Maimuta'
    _firstname = 'Plangatoare'

    @property
    def fullname(self):
        return self._lastname + ' ' + self._firstname


instance_of_User = User()
print(instance_of_User.fullname)
