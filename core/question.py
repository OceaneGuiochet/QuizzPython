class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def show(self):
        print(self.text)
        i = 1
        for choice in self.choices:
            print(str(i) + ". " + choice)
            i += 1

    def check_answer(self, choice_text):
        return choice_text == self.answer
