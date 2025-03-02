"""
This program shows how to load sounds by assigning the file path to a variable in the window constructor method
And then how to play it using a conditional to play it when the appropriate key is pressed
The laser sound is saved to the project file folder. The jump sound is an example of how to access the builtin sounds

!!! The laser sound is quiet - turn the volume right up to hear it !!!

"""

import arcade


class MyApplication(arcade.Window):

    def __init__(self, width, height):
        super().__init__(width, height, "Trigger Sound With Key")

        # Load the sounds when the application starts
        self.laser_sound = arcade.load_sound("laser.wav")
        self.jump_sound = arcade.load_sound(":resources:sounds/jump2.wav")

    def on_key_press(self, key, modifiers):

        # If the user hits the space bar or up arrow key, play a sound that we loaded
        if key == arcade.key.SPACE:
            arcade.play_sound(self.laser_sound)
        if key == arcade.key.UP:
            arcade.play_sound(self.jump_sound)


def main():
    window = MyApplication(300, 300)
    arcade.run()


main()
