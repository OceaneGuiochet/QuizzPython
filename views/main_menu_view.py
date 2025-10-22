import arcade
from arcade import key
from core.settings import SCREEN_WIDTH, SCREEN_HEIGHT
from views.game_view import GameView

BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50

class MenuView(arcade.View):

    def __init__(self):
        super().__init__()
        self.name = ""
        self.button_x = SCREEN_WIDTH // 2 - BUTTON_WIDTH // 2
        self.button_y = SCREEN_HEIGHT // 2 - BUTTON_HEIGHT // 2

    def on_show_view(self):
        arcade.set_background_color(arcade.color.LIGHT_BLUE)

    def on_draw(self):
        self.clear()

        arcade.draw_text("Entrer votre nom :", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100,
                         arcade.color.BLACK, 24, anchor_x="center")

        arcade.draw_text(self.name, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50,
                         arcade.color.GRAY, 20, anchor_x="center")

        arcade.draw_lbwh_rectangle_filled(self.button_x, self.button_y, BUTTON_WIDTH, BUTTON_HEIGHT, arcade.color.GRAY)
        arcade.draw_text("Commencer", self.button_x + BUTTON_WIDTH // 2, self.button_y + BUTTON_HEIGHT // 2,
                         arcade.color.WHITE, 20, anchor_x="center", anchor_y="center")

    def on_key_press(self, symbol, modifiers):
        if symbol == key.BACKSPACE:
            self.name = self.name[:-1]
        elif 32 <= symbol <= 126 and len(self.name) < 20:
            self.name += chr(symbol)

    def on_mouse_press(self, x, y, button, modifiers):
        if (self.button_x <= x <= self.button_x + BUTTON_WIDTH and
                self.button_y <= y <= self.button_y + BUTTON_HEIGHT and
                self.name.strip()):
            game_view = GameView(self.name)
            self.window.show_view(game_view)
