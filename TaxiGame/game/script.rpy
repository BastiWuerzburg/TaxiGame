# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define y = Character("You")

default purse_found = False
default tinfoil_hat = False
default top_hat = False
default karma = 50
default money = 0
default pasangengersLeft = 5
default passengers = ["Drunken Conspiracy Theorist", "Goose", "Alien", "Stalker", "Wallet", "Kpop", "Beach", "Karen", "Bonzai Tree", "Old Lady", "Stripper Nun", "Brain in a Jar"]
        #define a array of jump labels
default jump_labels = ["conspiracy", "goose", "alien", "stalker", "wallet", "kpop", "beach", "karen", "bonzai", "old_lady", "stripper_nun", "simulation"]
default passenger_indexes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

image background_video = Movie(play="Fenster_animation6.webm", pos=(0, 0), anchor=(0, 0))

# 3D view settings

#define config.perspective = (100, z, 100000)

camera:
    perspective True

camera background:
    perspective True

# animations 

image orange moving:
    animation
    "orange"
    xalign 0.0
    linear 5.0 xalign 1.0
    repeat

# stats

screen Karma:
     text "Karma [karma]" xpos 0.1 ypos 0.1

screen Money:
     text "Money [money]" xpos 0.1 ypos 0.2

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene room#:
        #xalign 0.5 yalign 0.5 zpos -1000

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy#:
        #xalign 0.5 yalign 0.5 zpos 100

    # These display lines of dialogue.

    y "You've created a new Ren'Py game."
    y "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    label choose_passenger:

        scene background_video
        show backseats:
            xalign 0.5 yalign 0.5 zpos 1
        show frontseat:
            xalign 0.5 yalign 0.5 zpos 0.5
        show mc:
            xalign 0.9999 yalign 0 zpos 0.2
        show dashboard:
            xalign 0.5 yalign 0.5 zpos 0.01
        show screen Karma
        show screen Money
        #todo: add and jump to a end scene
        if pasangengersLeft < 1:
            jump end_game
        #select a random passenger    
        $passenger = passengers[passenger_indexes.pop(int(renpy.random.random() * len(passenger_indexes) - 1))]
        $pasangengersLeft -= 1
        
        menu:
           #create a menug item
            "Pick up [passenger]":
                $renpy.jump(jump_labels[passengers.index(passenger)])

            "END":
                jump end_game

    label game:

        scene red#:
            #xalign 0.5 yalign 0.5 zpos -1000

        y "red"

    label book:

        scene blue#:
            #xalign 0.5 yalign 0.5 zpos -1000

        y "blue"

        show green at left

        y "green"

        show pink at right

        y "pink"

        show orange moving

        y "orange moves"

        pause

label end_game:
    return
