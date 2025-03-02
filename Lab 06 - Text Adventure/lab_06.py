# A simple text adventure game
class Room:
    """
    this class represents the rooms in the playing area
    """

    def __init__(self, name, descr, north, east, south, west, go_up, go_down):
        """ This is a method that sets up the variables in the object. """
        self.name = name
        self.description = descr
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.up = go_up
        self.down = go_down


def main():
    """ This is my main program function """

    # this code populates the room info
    room_list = []
    names = ['Dining Room', 'Hall', 'Lounge', 'Library', 'Store', 'Kitchen']
    descriptions = [
        'You are in a grand but faded dining room. Cobwebs cover the table and chairs.There are doors to the north '
        'and to the east.',
        'You are in a large marble floored entrance hall with hunting trophies adorning the walls. There is a grand '
        'staircase leading to the upper floor and doors to the east and the west.',
        'You are in the smoking lounge. There are tatty sofas and chairs and a sideboard with half empty drink '
        'bottles. There are doors to the north and the west',
        'You are in the library. In the dim light you can see scores of dust covered bookshelves. There are doors to '
        'the south and the west.',
        'You are in a store room. It is dark. You can faintly see a door to the west and ramshackle stairs going down '
        'to the basement.',
        'You are in the kitchen. There is an old cauldron in the centre and cooking utensils scattered about. There '
        'are doors to the south and the east.'
    ]
    norths = [5, None, 3, None, None, None]
    easts = [1, 2, None, None, None, 4]
    souths = [None, None, None, 2, None, 0]
    wests = [None, 0, 1, 4, 5, None]
    ups = [None, None, None, None, None, None]
    downs = [None, None, None, None, None, None]
    for i in range(len(names)):
        room = Room(names[i], descriptions[i], norths[i], easts[i], souths[i], wests[i], ups[i], downs[i])
        room_list.append(room)

    # this code sets the game
    current_room = 1
    done = False
    while not done:
        print(room_list[current_room].description)
        answer = input('What do you want to do? Enter n for north, e for east, s for south, w for west, u for up, '
                       'd for down, q to quit: ')
        print()
        low_answer = answer.lower()
        move = low_answer[0]

        if move == 'n':
            new_room = room_list[current_room].north
            if new_room is None:
                print("Sorry, you can't go that way")
            else:
                current_room = new_room
        elif move == 'e':
            new_room = room_list[current_room].east
            if new_room is None:
                print("Sorry, you can't go that way")
            else:
                current_room = new_room
        elif move == 'w':
            new_room = room_list[current_room].west
            if new_room is None:
                print("Sorry, you can't go that way")
            else:
                current_room = new_room
        elif move == 's':
            new_room = room_list[current_room].south
            if new_room is None:
                print("Sorry, you can't go that way")
            else:
                current_room = new_room
        elif move == 'u':
            new_room = room_list[current_room].up
            if new_room is None:
                print("Sorry, you can't go that way")
            else:
                current_room = new_room
        elif move == 'd':
            new_room = room_list[current_room].down
            if new_room is None:
                print("Sorry, you can't go that way")
            else:
                current_room = new_room
        elif move == 'q':
            print('Goodbye. I hope you liked exploring the house.')
            done = True
        else:
            print('Sorry, I did not understand your answer')


main()
