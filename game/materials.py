class Materials:
    def __init__(self):
        self.fuel = 1000
        self.food = 1000
        self.water = 1000
        self.screw = 1000
        self.iron = 0
        self.gold = 50
        self.stones = 10

    def materials_list(self):
        names = [i for i in dir(self) if (not callable(getattr(self, i)) and i.find('__') == -1)]
        # names = [i for i in dir(self) if (not callable(self.__getattribute__(i)) and i.find('__') == -1)]
        return names

    def materials_change(self, change):
        for name, amount in change.items():
            how_many = getattr(self, name)
            how_many = how_many + amount
            setattr(self, name, how_many)

    def materials_status(self):
        status = {}
        names = self.materials_list()
        for name in names:
            amount = getattr(self, name)
            status[name] = amount
        return status

if __name__ == '__main__':
    t = Materials()

    names = t.materials_list()
    print(names)
