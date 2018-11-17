class NoMoreWear(Exception):
    """ No more items can wear exception """ 
    pass


class NoSuchBodyPart(Exception):
    """ No more items can wear exception """ 
    pass


class Inventory:
    """ Character personal inventory """
    ITEMS_LIMIT = 2
    def __init__(self):
        """ Body parts equipment """
        self.head = []
        self.torso = []
        self.arms = []
        self.legs = []

    
    def wear_item(self, body_part, item_name):
        """
        parts are:
        head, torso, arms, legs
        """ 
        if body_part == 'head':
            self._wear(self.head, item_name)
        elif body_part == 'torso':
            self._wear(self.torso, item_name)
        elif body_part == 'arms':
            self._wear(self.arms, item_name)
        elif body_part == 'legs':
            self._wear(self.legs, item_name)
        else:
            raise NoSuchBodyPart('no such body part')
    
    def unwear_item(self, body_part, item_name):
        if body_part == 'head':
            self.head.remove(item_name)
        elif body_part == 'torso':
            self.torso.remove(item_name)
        elif body_part == 'arms':
            self.arms.remove(item_name)
        elif body_part == 'legs':
            self.legs.remove(item_name)
        else:
            raise NoSuchBodyPart('no such body part')

    def _wear(self, part, item_name):
        if len(part) < self.ITEMS_LIMIT:
            part.append(item_name)
        else:
            raise NoMoreWear('You cant wear more')

