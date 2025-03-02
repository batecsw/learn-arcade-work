class Dog():
    def __init__(self, dog_name):
        """ Constructor """
        self.name = dog_name
        print("A new dog is born!")


def main():
    # This creates the dog object
    my_dog = Dog("Bouncer")
    print("The dog's name is: ", my_dog.name)


main()
