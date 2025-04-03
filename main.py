import arcade

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Jogo de Plataforma"
JOGADOR_VELOCIDADE = 5


class GameView(arcade.Window):
    
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
        self.player_texture = arcade.load_texture("Images\Personagen.png")

        self.player_sprite = arcade.Sprite(self.player_texture)
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
                 self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

    def setup(self):

        pass
    def on_draw(self):
             self.clear()
             arcade.draw_sprite(self.player_sprite)
             self.player_list.draw()
             self.wall_list.draw()
    def on_update(self, delta_time):
        self.physics_engine.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.W:
            self.player_sprite.change_X = -JOGADOR_VELOCIDADE
        elif key == arcade.key.RIGHT or key == arcade.key.A:
            self.player_sprite.change_x +=JOGADOR_VELOCIDADE
    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.W:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.A:
            self.player_sprite.change_x = 0
def main():
    window = GameView()
    window.setup()
    arcade.run()
if __name__ == "__main__":
    main()