class Person:
    def __init__(self, strength, brainpower, agility, charisma, perception, vitality, hunger, thirst, fatigue, morale,
                 health, time):
        self.strength = strength
        self.current_strength = strength
        self.brainpower = brainpower
        self.current_brainpower = brainpower
        self.agility = agility
        self.current_agility = agility
        self.charisma = charisma
        self.current_charisma = charisma
        self.perception = perception
        self.current_perception = perception
        self.vitality = vitality
        self.current_vitality = vitality

        self.hunger = hunger
        self.thirst = thirst
        self.fatigue = fatigue
        self.morale = morale
        self.health = health
        self.time = time

    def hunger_condition(self):
        pass

    def thirst_condition(self):
        penalty1 = self.thirst // 4
        penalty2 = self.thirst // 8
        self.current_strength -= penalty1
        self.current_vitality -= penalty1
        self.morale -= 10 * penalty1
        self.current_brainpower -= penalty2
        self.current_agility -= penalty2
        self.current_charisma -= penalty2
        self.current_perception -= penalty2

    def fatigue_condition(self):
        pass

    def morale_status(self):
        pass

    def health_status(self):
        pass

    def time_flow(self):
        if not self.time % 4:
            self.hunger += 1
        if not self.time % 3:
            self.thirst += 1
        if not self.time % 2:
            self.fatigue += 1


if __name__ == '__main__':
    mareczek = Person(10, 10, 10, 10, 10, 10, 0, 0, 0, 100, 100, 0)
    mareczek.thirst = 40
    mareczek.thirst_condition()
    print(mareczek.current_strength, mareczek.current_perception, mareczek.morale)
