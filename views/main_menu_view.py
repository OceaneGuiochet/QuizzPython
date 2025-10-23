import os

import arcade
import arcade.gui
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
        self.background = arcade.load_texture("assets/background_menu.png")
        self.input_box_y = SCREEN_HEIGHT // 2 - 20  # zone de saisie plus bas
        self.button_y = self.input_box_y - 80  # bouton encore plus bas

        self.manager = arcade.gui.UIManager()

        self.column = arcade.gui.UIButtonRow(vertical=True)

        self.column.add(arcade.gui.UILabel(
            text="QUIZZ",
            font_size=64,
            text_color=arcade.color.LIGHT_BLUE,
        ))

        self.column.add(arcade.gui.UILabel(
            text="Entrer votre nom :",
            font_size=24,
            text_color=arcade.color.LIGHT_APRICOT,
        ))

        self.input = arcade.gui.UIInputText(
            width=BUTTON_WIDTH,
            border_color=arcade.color.LIGHT_GRAY,
            border_width=2,
            text_color=arcade.color.LIGHT_APRICOT,
        )
        self.column.add(self.input)


        self.play_button = self.column.add_button(label="Commencer", width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
        @self.play_button.event('on_click')
        def on_click_play(event):
            game_view = GameView(self.input.text)
            self.window.show_view(game_view)

        self.anchor = self.manager.add(arcade.gui.UIAnchorLayout())

        self.anchor.add(
            anchor_x="center_x",
            anchor_y="center_y",
            child=self.column,
        )


    def on_show_view(self):
        arcade.set_background_color(arcade.color.LIGHT_BLUE)
        self.manager.enable()

    def on_hide_view(self):
        self.manager.disable()

    def on_draw(self):
        self.clear()

        arcade.draw_texture_rect(
            self.background,
            arcade.LBWH(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT),
        )

        self.manager.draw()

    """def on_key_press(self, symbol, modifiers):
        if symbol == key.BACKSPACE:
            self.name = self.name[:-1]
        elif 32 <= symbol <= 126 and len(self.name) < 20:
            self.name += chr(symbol)"""
