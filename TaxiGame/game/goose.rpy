define go = Character("Goose")

# animations 

image goose_moving:
    animation
    "goose"
    xalign -0.8 yalign 0 zpos 0.1
    linear 2.0 xalign 0.0

label goose:

    scene background_video
    show backseats:
        xalign 0.5 yalign 0.5 zpos 1
    show frontseat:
        xalign 0.5 yalign 0.5 zpos 0.5
    show mc:
        xalign 0.9999 yalign 0 zpos 0.2
    show goose_moving
    show dashboard:
        xalign 0.5 yalign 0.5 zpos 0.01

    "A goose hops into the cab." 
    go "Honk! Honk! Honk!"
    play sound ["sounds/quack.mp3"]        

    menu:
        "What are you going to do?"

        "Empathise":
            jump empathise

        "Understand the destination":
            jump understand

        "Honk":
            jump honk

    label empathise:
        y "Damn, that all happened? Im so sorry for you."
        go "suprised Honks"
        y "Yea, I have been honked at all my life so I know what you mean."
        go "Happy Honks"
        "Over the drive towards the hospital where the wife of the distressed goose resides a new friendship is forged and stories arw exchanged."
        $ karma += 1
        $ money += 20
        jump goose_end

    
    label understand:
        y "What was that you said?"
        play voice["sounds/quack.mp3"]
        go "Honk"
        y "The hospital?"
        go "Suprised honks"
        play voice["sounds/quack.mp3"]
        y "I understood where you want to go but i cant make out the rest, sorry about that."
        play voice["sounds/quack.mp3"]
        go "Understanding honks"
        "Remaining in silence for the rest of the drive you deliver the goose at the hospital and wave it of with a smile on your face."
        $ karma += 0
        $ money += 20
        jump goose_end

    label honk:
        y "Honks back at the goose"
        play voice["sounds/quack.mp3"]
        go "surprised honks"
        y "Honks back at the goose"
        play voice["sounds/quack.mp3"]
        go "angry honks"
        y "honks in response"
        "After having honked insults at the goose the entire trip and dropped them of at the wrong location the goose steals your car keys and tries to escape."
        "You manage to barely get them back before you continue your trip."
        $ karma -=1
        $ money += 20
    
    label goose_end:
    jump choose_passenger