import arcade

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Jogo de Plataforma"
JOGADOR_VELOCIDADE = 3
GRAVITY = 1
PLAYER_JUMP_SPEED = 16
COIN_SCALING = 1.4

class GameView(arcade.Window):
    
    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

        self.player_texture = None
        self.player_sprite = None
        self.player_list = None
        self.wall_list = None
        self.camera = None
        self.coin_list = None
        self.collect_coin_sound = arcade.load_sound("Sounds\item-pick-up-38258.mp3")
        self.jump_sound = arcade.load_sound("Sounds\jump.mp3")
        self.music = arcade.load_sound("Sounds\Music_Theme.mp3")
        self.music_player = arcade.play_sound(self.music)

        self.gui_camera = None
        self.score = 0
        self.score_text = None
        self.scene = None

    def setup(self):
         
         self.scene = arcade.Scene()
         self.player_texture = arcade.load_texture("Images\Personagen.png")
         self.player_sprite = arcade.Sprite(self.player_texture)
         self.player_sprite.center_x = 100
         self.player_sprite.center_y = 128
         self.scene.add_sprite("Player", self.player_sprite)
        
         self.scene.add_sprite_list("Walls", use_spatial_hash=True)
         self.scene.add_sprite_list("Coins", use_spatial_hash=True)

         for x in range(0, 1250, 64):
            wall = arcade.Sprite("Images\Terreno.png", scale=0.5)
            wall.center_x = x
            wall.center_y = 32
            self.scene.add_sprite("Walls", wall)


            coordinate_list = [[512, 96], [256, 96], [768, 96]]

            for x in range(128, 1250, 256):
                coin = arcade.Sprite("Images\Moeda.png", scale=COIN_SCALING)
                coin.center_x = x
                coin.center_y = 96
                self.scene.add_sprite("Coins", coin)

            for coordinate in coordinate_list:
                 wall = arcade.Sprite("Images\Caixa.png", scale=0.2)
                 wall.position = coordinate
                 self.scene.add_sprite("Walls", wall)
                
                 self.background_color = arcade.csscolor.BLUE_VIOLET

                 self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, walls=self.scene["Walls"], gravity_constant=GRAVITY)

                 self.camera = arcade.Camera2D()
                 self.gui_camera = arcade.Camera2D()
                 self.score = 0
                 self.score_text = arcade.Text(f"Score: {self.score}", x=0, y=5)
    def on_draw(self):
             
             self.clear()
             self.camera.use()
             self.scene.draw()
             self.gui_camera.use()
             self.score_text.draw()


    def on_update(self, delta_time):

        self.physics_engine.update()

        coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.scene["Coins"])

        for coin in coin_hit_list:
            coin.remove_from_sprite_lists()
            arcade.play_sound(self.collect_coin_sound)
            self.score += 1
            self.score_text.text = f"Score: {self.score}"
            
            
        self.camera.position = self.player_sprite.position

    def on_key_press(self, key, modifiers):
        
        if key == arcade.key.ESCAPE:
            self.setup()
            
        if key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = PLAYER_JUMP_SPEED
                arcade.play_sound(self.jump_sound)
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -JOGADOR_VELOCIDADE
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = JOGADOR_VELOCIDADE
    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0
def main():
    window = GameView()
    window.setup()
    arcade.run()
if __name__ == "__main__":
    main()