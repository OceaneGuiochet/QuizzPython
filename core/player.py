class Player:

    def __init__(self, name):
        self.name = name
        self.total_points = 0

    def add_points(self, points):
        self.total_points += points