class Toys():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name' : 'Yoyo',
            'has pets' : False
        }

    def __str__(self):
        return f'{self.color}'

    def __len__(self):
        return 5

    def __del__(self):
        print ('deleted!')

    def __call__(self):
        return ('yes?')

    def __getitem__(self, i):
        return self.my_dict[i]


action_figure = Toys("red", 0)
print(action_figure.__str__())
print(str(action_figure))
print(str('action_figure'))
print(len(action_figure))
#del(action_figure)
print(action_figure())
print(action_figure['name'])
