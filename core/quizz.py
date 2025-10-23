class Quizz:
    def __init__(self,questions, player):
        self.questions = questions
        self.player = player
        self.current_index = 0
        self.points = 0

    def first_question(self):
        return self.questions[self.current_index]

    def next_question(self):
        self.current_index += 1
        if self.current_index < len(self.questions):
            question = self.questions[self.current_index]
            return question
        return None

    def add_points(self, points):
        self.points += points
        self.player.add_points(points)