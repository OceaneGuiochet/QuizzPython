import json

from core.player import Player
from core.question import Question
from core.quizz import Quizz


class QuizzManager():
    def __init__(self):
        self.player = None
        self.quizz = None

    def load_questions(self, json_file):
        with open(json_file) as json_file:
            data = json.load(json_file)
        questions = []
        for question in data:
            questions.append(Question(question["text"], question["choices"] , question["answer"]))
        return questions

    def start_quizz(self, player_name, json_file):
        self.player = Player(player_name)
        questions = self.load_questions(json_file)
        self.quizz = Quizz(questions, self.player)
        return self.quizz