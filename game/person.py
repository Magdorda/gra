from game.inventory import Inventory


class Person:
    def __init__(self, strength, brainpower, agility, charisma, perception, vitality, hunger, thirst, fatigue, morale,
                 morale_factor, health, status_effects, time):
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
        self.morale_factor = morale_factor
        self.health = health
        self.status_effects = status_effects
        self.status_effects = set()
        self.time = time

    def hunger_condition(self):
        pass

    def thirst_condition(self):
        penalty1 = self.thirst // 4
        penalty2 = self.thirst // 8
        self.current_strength -= penalty1
        self.current_vitality -= penalty1
        self.current_brainpower -= penalty1
        self.morale -= 6 * penalty1
        self.current_agility -= penalty2
        self.current_charisma -= penalty2
        self.current_perception -= penalty2

    def fatigue_condition(self):
        if self.fatigue >= 12:
            self.current_perception -= 1
            self.current_agility -= 1
            self.current_strength -= 1
            self.current_brainpower -= 1
            self.current_charisma -= 1
            self.current_vitality -= 1
            self.morale -= 2
            more_fatigue = self.fatigue - 12
            more_fatigue = more_fatigue // 3
            self.current_perception -= more_fatigue
            self.current_agility -= more_fatigue
            self.current_strength -= more_fatigue
            self.current_brainpower -= more_fatigue
            self.current_charisma -= more_fatigue
            self.current_vitality -= more_fatigue
            self.morale -= 2 * more_fatigue


    def morale_status(self):
        if self.morale == 0:
            """add mental breakdown status effect"""
        if 1 <= self.morale <= 10:
            self.morale_factor = -3
            self.current_charisma -= 3
            self.current_vitality -= 3
            self.current_brainpower -= 2
            self.current_strength -= 2
            self.current_agility -= 2
            self.current_perception -= 2

        if 11 <= self.morale <= 30:
            self.morale_factor = -2
            self.current_charisma -= 2
            self.current_vitality -= 2
            self.current_brainpower -= 1
            self.current_strength -= 1
            self.current_agility -= 1
            self.current_perception -= 1

        if 31 <= self.morale <= 45:
            self.morale_factor = -1
            self.current_charisma -= 1
            self.current_vitality -= 1

        if 46 <= self.morale <= 55:
            self.morale_factor = 0

        if 56 <= self.morale <= 70:
            self.morale_factor = 1
            self.current_charisma += 1
            self.current_vitality += 1

        if 71 <= self.morale <= 90:
            self.morale_factor = 2
            self.current_charisma += 1
            self.current_vitality += 1
            self.current_brainpower += 1
            self.current_perception += 1

        if 91 <= self.morale <= 100:
            self.morale_factor = 3
            self.current_charisma += 2
            self.current_vitality += 2
            self.current_brainpower += 2
            self.current_perception += 1
            self.current_agility += 1
            self.current_strength += 1

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
    mareczek = Person(10, 10, 10, 10, 10, 10, 0, 0, 0, 100, 100, 0, False, 0)
    mareczek.thirst = 40
    mareczek.thirst_condition()
    print(mareczek.current_strength, mareczek.current_perception, mareczek.morale)
