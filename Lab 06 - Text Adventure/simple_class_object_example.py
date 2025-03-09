class Dog():
    def __init__(self, dog_name, dog_color):
        """ Constructor """
        self.name = dog_name
        self.color = dog_color
        print("A new dog is born!")


def main():
    # This creates the dog object
    my_dog = Dog("Bouncer", "black")
    print("The dog's name is: ", my_dog.name)
    print("The dog's colour is", my_dog.color)


main()
