import arcade

from core.settings import BUTTON_WIDTH, SCREEN_WIDTH, SCREEN_HEIGHT, BUTTON_SPACING, BUTTON_HEIGHT
from managers.quizz_manager import QuizzManager



class GameView(arcade.View):
    """Vue principale du jeu."""

    def __init__(self, player_name=""):
        super().__init__()
        self.player_name = player_name
        self.manager = QuizzManager()
        self.quizz = self.manager.start_quizz(player_name, "assets/questions.json")

        self.current_question = self.quizz.first_question()
        self.buttons = []
        self.create_buttons()

    def on_show_view(self):
        arcade.set_background_color(arcade.color.LIGHT_BLUE)

    def create_buttons(self):
        self.buttons = []
        if self.current_question:
            num_choices = len(self.current_question.choices)
            total_width = num_choices * BUTTON_WIDTH + (num_choices - 1) * BUTTON_SPACING
            start_x = (SCREEN_WIDTH - total_width) // 2
            y = SCREEN_HEIGHT // 2 - BUTTON_HEIGHT // 2

            for i, choice in enumerate(self.current_question.choices):
                x = start_x + i * (BUTTON_WIDTH + BUTTON_SPACING)
                self.buttons.append((x, y, BUTTON_WIDTH, BUTTON_HEIGHT, choice))

    def on_draw(self):
        self.clear()

        if self.current_question:

            arcade.draw_text(
                self.current_question.text,
                SCREEN_WIDTH // 2,
                SCREEN_HEIGHT - 150,
                arcade.color.WHITE,
                22,
                anchor_x="center",
                anchor_y="center",
                align="center"
            )
            for x, y, w, h, choice in self.buttons:
                arcade.draw_lbwh_rectangle_filled(x, y, w, h, arcade.color.WHITE)
                arcade.draw_text(
                    choice,
                    x + w / 2,
                    y + h / 2,
                    arcade.color.BLACK,
                    16,
                    anchor_x="center",
                    anchor_y="center",
                )
        else:
            arcade.draw_text(
                f"Quizz fini, Total points: {self.quizz.player.total_points}",
                100,
                200,
                arcade.color.WHITE,
                18
            )

    def on_mouse_press(self, x, y, button, modifiers):
        if not self.current_question:
            return

        for bx, by, bw, bh, choice_text in self.buttons:
            if bx <= x <= bx + bw and by <= y <= by + bh:
                clicked_choice = choice_text.strip()
                correct_choice = self.current_question.answer.strip()

                if clicked_choice.lower() == correct_choice.lower():
                    self.quizz.add_points(1)
                    print("Bonne réponse ! +1 point")
                else:
                    print("Mauvaise réponse ! 0 point")

                self.current_question = self.quizz.next_question()
                self.create_buttons()
                break
