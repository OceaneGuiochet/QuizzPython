import random
import arcade

from core.settings import BUTTON_WIDTH, SCREEN_WIDTH, SCREEN_HEIGHT, BUTTON_SPACING, BUTTON_HEIGHT
from managers.quizz_manager import QuizzManager


class GameView(arcade.View):
    """Vue principale du jeu."""

    def __init__(self, player_name="", quizz_number=1, total_points=0):
        super().__init__()
        self.player_name = player_name
        self.current_quizz_number = quizz_number
        self.manager = QuizzManager()
        self.quizz = self.manager.start_quizz(player_name, f"assets/quizz{quizz_number}.json")

        self.quizz.player.total_points = total_points

        self.current_question = self.quizz.first_question()
        self.buttons = []
        self.bonus_buttons = None
        self.feedback_message = ""
        self.final_message = ""
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

            self.bonus_buttons = (100, 60, 120, 40, "50/50 (-5pts)")

    def on_draw(self):
        self.clear()

        arcade.draw_text(
            f"{self.player_name} | Total points: {self.quizz.player.total_points}",
            SCREEN_WIDTH - 300,
            SCREEN_HEIGHT - 40,
            arcade.color.WHITE,
            16,
        )

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

            if self.feedback_message:
                y_under_buttons = self.buttons[0][1] - 50
                arcade.draw_text(
                    self.feedback_message,
                    SCREEN_WIDTH // 2,
                    y_under_buttons,
                    arcade.color.DARK_BLUE_GRAY if "Bonne" in self.feedback_message else arcade.color.RED,
                    20,
                    anchor_x="center",
                    anchor_y="center"
                )

            if self.bonus_buttons:
                bx, by, bw, bh, label = self.bonus_buttons
                arcade.draw_lbwh_rectangle_filled(bx, by, bw, bh, arcade.color.ORANGE)
                arcade.draw_text(
                    label,
                    bx + bw / 2,
                    by + bh / 2,
                    arcade.color.BLACK,
                    14,
                    anchor_x="center",
                    anchor_y="center"
                )

        else:
            arcade.draw_text(
                f"Quizz fini, Total points: {self.quizz.player.total_points}",
                SCREEN_WIDTH // 2,
                SCREEN_HEIGHT // 2 + 80,
                arcade.color.WHITE,
                18,
                anchor_x="center",
            )

            if self.final_message:
                arcade.draw_text(
                    self.final_message,
                    SCREEN_WIDTH // 2,
                    SCREEN_HEIGHT // 2 - 50,
                    arcade.color.RED,
                    20,
                    anchor_x="center",
                    anchor_y="center"
                )
            else:
                bx, by, bw, bh = (SCREEN_WIDTH - 350) / 2, (SCREEN_HEIGHT - 100) / 2, 350, 100
                arcade.draw_lbwh_rectangle_filled(bx, by, bw, bh, arcade.color.GRAY)
                arcade.draw_text(
                    "Commencer le Quizz suivant",
                    bx + bw / 2,
                    by + bh / 2,
                    arcade.color.WHITE,
                    20,
                    anchor_x="center",
                    anchor_y="center"
                )

    def on_mouse_press(self, x, y, button, modifiers):
        if not self.current_question:
            bx, by, bw, bh = (SCREEN_WIDTH - 350) / 2, (SCREEN_HEIGHT - 100) / 2, 350, 100
            if bx <= x <= bx + bw and by <= y <= by + bh:
                self.current_quizz_number += 1
                try:
                    new_quizz = GameView(
                        self.player_name,
                        self.current_quizz_number,
                        total_points=self.quizz.player.total_points  # cumuler les points
                    )
                    self.window.show_view(new_quizz)
                except FileNotFoundError:
                    self.final_message = "Tous les quizz sont terminés."
            return

        if self.bonus_buttons:
            bx, by, bw, bh, label = self.bonus_buttons
            if bx <= x <= bx + bw and by <= y <= by + bh:
                self.use_bonus_5050()
                return

        for bx, by, bw, bh, choice_text in self.buttons:
            if bx <= x <= bx + bw and by <= y <= by + bh:
                clicked_choice = choice_text.strip()
                correct_choice = self.current_question.answer.strip()

                if clicked_choice.lower() == correct_choice.lower():
                    self.quizz.add_points(1)
                    self.feedback_message = "Bonne réponse !"
                else:
                    self.feedback_message = f"Mauvaise réponse ! (La bonne réponse était : {correct_choice})"

                self.current_question = self.quizz.next_question()
                self.create_buttons()
                break

    def use_bonus_5050(self):

        if self.quizz.player.total_points < 5:
            self.feedback_message = "Points insuffisants pour utiliser le 50/50"
            return

        self.quizz.player.total_points -= 5

        wrong_choices = [c for c in self.current_question.choices if c != self.current_question.answer]
        to_remove = random.sample(wrong_choices, min(2, len(wrong_choices)))
        self.current_question.choices = [c for c in self.current_question.choices if c not in to_remove]
        self.create_buttons()
        self.feedback_message = "Bonus 50/50 utilisé (-5pts)"
