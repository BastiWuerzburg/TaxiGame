# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define y = Character("You")

default purse_found = False
default tinfoil_hat = False
default top_hat = False
default karma = 0
default money = 0
default pasangengersLeft = 7
default passengers = ["Drunken Conspiracy Theorist", "Goose", "Alien", "Stalker Victim", "Wallet", "K-pop Star", "Beach Girl", "Karen", "Bonzai Tree", "Old Lady", "Stripper Nun", "Brain in a Jar"]
        #define a array of jump labels
default jump_labels = ["conspiracy", "goose", "alien", "stalker", "wallet", "kpop", "beach", "karen", "bonzai", "old_lady", "stripper_nun", "simulation"]
default passenger_indexes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

image background_video = Movie(play="Fenster_animation8.webm", pos=(0, 0), anchor=(0, 0))

# 3D view settings

#define config.perspective = (100, z, 100000)

camera:
    perspective True

camera background:
    perspective True

# animations 

image mc_moving:
    animation
    "mc"
    xalign 2.0
    linear 3.0 xalign 1.0

# stats

screen Karma:
     text "Your karma is: [karma]" xpos 0.18 ypos 0.48

screen Money:
     text "Money earned: [money] $" xpos 0.18 ypos 0.52

# The game starts here.

label start:

    play music "sounds/bg.mp3"

    scene street
    show backseats:
        xalign 0.5 yalign 0.5 zpos 1
    show frontseat:
        xalign 0.5 yalign 0.5 zpos 0.5
    show mc_moving
    show dashboard:
        xalign 0.5 yalign 0.5 zpos 0.01
    

    # These display lines of dialogue.

    play sound ["sounds/close.mp3"]
    y "A new working day has begun."
    y "My taxi, here I come!"
    play sound ["sounds/start.mp3"]
    y "I feel like today is gonna be a good day."

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
        
        #todo: add and jump to a end scene
        if pasangengersLeft < 1:
            jump game_end
        #select a random passenger    
        $passenger = passengers[passenger_indexes.pop(int(renpy.random.random() * len(passenger_indexes) - 1))]
        $pasangengersLeft -= 1
        
        menu:
           #create a menug item
            "Pick up [passenger]":
                play sound ["sounds/close.mp3"]
                pause 0.1 #2.1
                $renpy.jump(jump_labels[passengers.index(passenger)])

            "END":
                jump game_end
