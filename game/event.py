import random

class Event:

    # przyjmuje obiekt klasy materials
    def found_materials(self, material):
        m = material.materials_list()
        print(m)
        k = random.randint(1, 3)
        names = random.choices(m, k=k)
        return names


if __name__ == '__main__':
    from game.materials import Materials
    m = Materials()
    e = Event()

    znaleziono = e.found_materials(m)
    print(znaleziono)
