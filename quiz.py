class Cars:
    def __init__(self, brand, doors, fuel):
        self.brand = brand
        self.doors = doors
        self.fuel = fuel

    def intro(self):
        print('My ' + self.brand + ' is reversing, beware')


car1 = Cars('BMW', 3, 'diesel')
car1.brand = 'Range rover'

car1.intro()


