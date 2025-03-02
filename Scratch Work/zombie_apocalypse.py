"""
This adapts the previous static coin collector game by the player shooting bullets to destroy the coins
The main changes to the code are as follows:
1. we create a 3rd sprite list to handle the bullets
2. the mouse movement function is changed so the player can only move left/right
3. a new mouse click function creates a bullet when the mouse is clicked, positions it, and adds it to the
   bullet sprite list
4. the window class update function has a new loop added - this loops through the bullet list and checks if
   the bullet has hit a coin, if so the bullet and coin are removed and the score increased. Also, if the
   bullet has moved off the top of the screen the bullet is removed.
"""


import random
import arcade

SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.3
SPRITE_SCALING_LASER = 0.8
COIN_COUNT = 100

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700

BULLET_SPEED = 5

# These numbers represent "states" that the game can be in.
INSTRUCTIONS_PAGE_0 = 0
INSTRUCTIONS_PAGE_1 = 1
GAME_RUNNING = 2
GAME_OVER = 3


class Coin(arcade.Sprite):
    """
    This class represents the coins on our screen. It is a child class of
    the arcade library's "Sprite" class.
    """

    def reset_pos(self):

        # Reset the coin to a random spot above the screen
        self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                         SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):

        # Move the coin
        self.center_y -= 0.5

        # See if the coin has fallen off the bottom of the screen.
        # If so, reset it.
        if self.top < 0:
            self.reset_pos()


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Zombie Apocalypse")

        # Variables that will hold sprite lists
        self.player_list = None
        self.coin_list = None
        self.bullet_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0
        self.lives = 5
        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        # Start 'state' will be showing the first page of instructions.
        self.current_state = INSTRUCTIONS_PAGE_0

        arcade.set_background_color(arcade.color.GREEN)
        self.laser_sound = arcade.load_sound("laser.wav")
        self.boom_sound = arcade.load_sound(":resources:sounds/explosion1.wav")

    def setup(self):

        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()

        # Set up the score
        self.score = 0
        self.lives = 5
        # Set up the player
        # Image from builtin resources
        self.player_sprite = arcade.Sprite(":resources:images/space_shooter/playerShip1_green.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 70
        self.player_list.append(self.player_sprite)

        # Create the coins
        for i in range(COIN_COUNT):

            # Create the coin instance
            # Coin image from builtin resources
            coin = Coin(":resources:images/animated_characters/zombie/zombie_walk2.png", SPRITE_SCALING_COIN)

            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(120, SCREEN_HEIGHT)

            # Add the coin to the lists
            self.coin_list.append(coin)

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

    def draw_instructions_page(self, page_number):
        """
        Draw an instruction page.
        """
        arcade.start_render()

        arcade.draw_text("Zombie Apocalypse Game", 100, 500, arcade.color.WHITE, 36)
        arcade.draw_text("Write some instructions here", 100, 400, arcade.color.WHITE, 14)
        arcade.draw_text("Press any key to continue", 100, 300, arcade.color.WHITE, 36)
    def draw_game(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.coin_list.draw()
        self.bullet_list.draw()
        self.player_list.draw()

        # Render the text
        arcade.draw_text(f"Score: {self.score}", 10, 20, arcade.color.WHITE, 14)
        arcade.draw_text(f"Lives: {self.lives}", 10, 50, arcade.color.WHITE, 14)

    def draw_game_over(self):
        """
        Draw "Game over" across the screen.
        """
        output = "Game Over"
        arcade.draw_text(output, 240, 400, arcade.color.WHITE, 54)

        output = "Press any key to restart"
        arcade.draw_text(output, 310, 300, arcade.color.WHITE, 24)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        if self.current_state == INSTRUCTIONS_PAGE_0:
            self.draw_instructions_page(0)

        elif self.current_state == INSTRUCTIONS_PAGE_1:
            self.draw_instructions_page(1)

        elif self.current_state == GAME_RUNNING:
            self.draw_game()

        else:
            self.draw_game()
            self.draw_game_over()

    def on_key_press(self, key, modifiers):
        # Change states as needed.
        if self.current_state == INSTRUCTIONS_PAGE_0:
            # Next page of instructions.
            self.current_state = INSTRUCTIONS_PAGE_1
        elif self.current_state == INSTRUCTIONS_PAGE_1:
            # Start the game
            self.setup()
            self.current_state = GAME_RUNNING
        elif self.current_state == GAME_OVER:
            # Restart the game.
            self.setup()
            self.current_state = GAME_RUNNING

    def on_mouse_motion(self, x, y, dx, dy):
        """
        Called whenever the mouse moves.
        """
        self.player_sprite.center_x = x

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called whenever the mouse button is clicked.
        """

        # Create a bullet
        bullet = arcade.Sprite(":resources:images/space_shooter/laserBlue01.png", SPRITE_SCALING_LASER)
        arcade.play_sound(self.laser_sound)

        # The image points to the right, and we want it to point up. So
        # rotate it.
        bullet.angle = 90

        # Position the bullet
        bullet.center_x = self.player_sprite.center_x
        bullet.bottom = self.player_sprite.top
        bullet.change_y = BULLET_SPEED

        # Add the bullet to the appropriate lists
        self.bullet_list.append(bullet)

    def update(self, delta_time):
        """ Movement and game logic """

        if self.current_state == GAME_RUNNING:
            # Call update on all sprites
            self.coin_list.update()
            self.bullet_list.update()

            # Loop through each bullet
            for bullet in self.bullet_list:

                # Check this bullet to see if it hit a coin
                hit_list = arcade.check_for_collision_with_list(bullet, self.coin_list)

                # If it did, get rid of the bullet
                if len(hit_list) > 0:
                    bullet.remove_from_sprite_lists()

                # For every coin we hit, add to the score and remove the coin
                for coin in hit_list:
                    coin.remove_from_sprite_lists()
                    self.score += 100
                    arcade.play_sound(self.boom_sound)

                # If the bullet flies off-screen, remove it.
                if bullet.bottom > SCREEN_HEIGHT:
                    bullet.remove_from_sprite_lists()

            # Loop through each zombie
            for coin in self.coin_list:

                # Check this zombie to see if it hit a player
                hit_list = arcade.check_for_collision_with_list(coin, self.player_list)

                # If it did, get rid of the zombie
                if len(hit_list) > 0:
                    coin.remove_from_sprite_lists()

                # If a zombie hits the player, lose a life
                for player in hit_list:
                    self.lives -= 1
                    arcade.play_sound(self.boom_sound)

            if self.lives <= 0:
                self.current_state = GAME_OVER


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()