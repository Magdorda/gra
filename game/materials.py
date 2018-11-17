

class Materials:
    def __init__(self):
        self.fuel = 1000
        self.food = 1000
        self.water = 1000
        self.screw = 1000
        self.iron = 0
        self.gold = 50

    # @classmethod
    def materials_list(self, b):
        print(b)
        variables = [i for i in dir(self) if (not callable(i) and i.find('__') == -1)]
        return variables

    def materials_add(self):
        pass

if __name__ == '__main__':
    t = Materials()
    # variables = [i for i in dir(t) if (not callable(i) and i.find('__') == -1)]

    import inspect

    for i in dir(t):
        print(i)
        print(inspect.ismethod(t.__getattribute__(i)))
        print()

    # variables = [i for i in dir(t) if (not inspect.isfunction(i) and i.find('__') == -1)]
    # print(variables)
    # print(type(variables[1]))
