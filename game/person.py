from inventory import Inventory

class Person:
    def __init__(self, strength, brainpower, agility, charisma, perception, vitality, hunger, thirst, fatigue, morale,
                 health, injury, time):
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
        self.inventory = Inventory()

        self.hunger = hunger
        self.thirst = thirst
        self.fatigue = fatigue
        self.morale = morale
        self.health = health
        self.injury = injury
        self.injury = set()
        self.time = time

    def hunger_condition(self):
        pass

    def thirst_condition(self):
        penalty1 = self.thirst // 4
        penalty2 = self.thirst // 8
        self.current_strength -= penalty1
        self.current_vitality -= penalty1
        self.morale -= 8 * penalty1
        self.current_brainpower -= penalty2
        self.current_agility -= penalty2
        self.current_charisma -= penalty2
        self.current_perception -= penalty2

    def fatigue_condition(self):
        pass

    def morale_status(self):
        if self.morale == 0:
            #self.injury
            pass
        if 1 <= self.morale <= 10:
            pass

        if 11 <= self.morale <= 30:
            pass

        if 31 <= self.morale <= 50:
            self.charisma -= 1
            self.vitality -= 1

        if 51 <= self.morale <= 70:
            self.charisma += 1
            self.vitality += 1

        if 71 <= self.morale <= 90:
            pass

        if 91 <= self.morale <= 100:
            pass

    def injuries(self):
        pass
        # broken_arm
        # broken_leg
        # severed_arm
        # severed_leg
        # concussion
        # fever
        # poisoning
        # light_wound
        # deep_wound
        # internal_wound
        # broken_jaw
        # amok
        # amnesia
        # skull_fracture
        # impacted_vision
        # brain_trauma
        # burst_eardrum
        # twitch
        # mysterious_ailment
        # missing_eye
        # megalomania
        # maimed_hand
        # confusion
        # mental_breakdown

    def time_flow(self):
        if not self.time % 4:
            self.hunger += 1
        if not self.time % 3:
            self.thirst += 1
        if not self.time % 2:
            self.fatigue += 1


if __name__ == '__main__':
    mareczek = Person(10, 10, 10, 10, 10, 10, 0, 0, 0, 100, 100, False, 0)
    mareczek.thirst = 40
    mareczek.thirst_condition()
    print(mareczek.current_strength, mareczek.current_perception, mareczek.morale)
