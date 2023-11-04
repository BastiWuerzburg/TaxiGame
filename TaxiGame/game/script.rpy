# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#define e = Character("Eileen")
define y = Character("You")

default purse_found = False
default tin_foil_hat = False
default top_hat = False
default karma = 50
default money = 0

# animations 

image orange moving:
    animation
    "orange"
    xalign 0.0
    linear 5.0 xalign 1.0
    repeat


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    y "You've created a new Ren'Py game."

    y "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.


    menu:

        y "Sure, but what's a \"visual novel?\""

        "It's a videogame.":
            jump game

        "It's an interactive book.":
            jump book

    label game:

        scene red

        y "red"

    label book:

        scene blue

        y "blue"

        show green at left

        y "green"

        show pink at right

        y "pink"

        show orange moving

        y "orange moves"

        pause

    return
