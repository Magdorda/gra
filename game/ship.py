class Ship:
    def __init__(self):
        from game.room import Room
        self.bridge = Room()
        self.engine = Room()
        self.cabin = Room()

    