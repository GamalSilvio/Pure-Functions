class User(object):
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')

class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)
        self.name = name
        self.power = power
        self.email = email

    def attack(self):
        print(f'attack with power of {self.power}')

wizard1 = Wizard('Merlin', 60, 'merlin@wizard.com')
print(wizard1)

print(dir(wizard1))
