import arcade
import pygame
# Constants
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Jogo de Plataforma"
rodando = True
velocidade =1

class GameView(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
        self.player_texture = arcade.load_texture("Images\Personagen.png")

        self.player_sprite = arcade.Sprite(self.player_texture)
        perso = self.player_sprite = arcade.Sprite(self.player_texture)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 128
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player_sprite)
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)
        for x in range(0, 1250, 64):
            wall = arcade.Sprite("Images\Terreno.png", scale=0.5)
            wall.center_x = x
            wall.center_y = 32
            self.wall_list.append(wall)
            coordinate_list = [[512, 96], [256, 96], [768, 96]]
            for coordinate in coordinate_list:
                 wall = arcade.Sprite("Images\Caixa.png", scale=0.2)
                 wall.position = coordinate
                 self.wall_list.append(wall)
                 self.background_color = arcade.csscolor.BLUE_VIOLET

    def setup(self):

        pass

    def on_draw(self):

             self.clear()
             arcade.draw_sprite(self.player_sprite)
             self.player_list.draw()
             self.wall_list.draw()
def main():
    window = GameView()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()