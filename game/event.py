import random


class Event:
    # przyjmuje obiekt klasy materials
    def found_materials(self, material):
        founded = {}
        m = material.materials_list()
        k = random.randint(1, 3)
        names = random.choices(m, k=k)
        for i in names:
            amount = random.randrange(1, 150)
            founded[i] = amount
        return founded

    def lose_materials(self, material):
        losed = {}
        m = material.materials_list()
        k = random.randint(1, 3)
        names = random.choices(m, k=k)
        for i in names:
            amount = random.randrange(-50, -1)
            losed[i] = amount
        return losed

    def injure_person(self, person, injure_kind):
        pass


if __name__ == '__main__':
    from game.materials import Materials
    m = Materials()
    e = Event()

    znaleziono = e.found_materials(m)
    print(znaleziono)
    m.materials_change(znaleziono)
    print(m.materials_status())

    stracono = e.lose_materials(m)
    print(stracono)
    m.materials_change(stracono)
    print(m.materials_status())
