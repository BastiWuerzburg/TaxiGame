define go = Character("Goose")

label goose:

    "A goose hops into the cab." 
    go "Honk! Honk! Honk!"

    menu:
        "What are you going to do?"

        "Empathise":
            jump empathise

        "Understand teh destination":
            jump understand

        "Honk":
            jump honk

    label empathise:
        y "Damn, that all happened? Im so sorry for you."
        go "suprised Honks"
        y "Yea, I have been honked at all my life so I know what you mean."
        go "Happy Honks"
        "Over the drive towards the hospital where the wife of the distressed goose resides a new friendship is forged and stories arw exchanged."
        $ += 1
        jump goose_end
    
    label understand:
        y "What was that you said?"
        go "Honk"
        y "The hospital?"
        go "Suprised honks"
        y "I understood where you want to go but i cant make out the rest, sorry about that."
        go "Understanding honks"
        "Remaining in silence for the rest of the drive you deliver the goose at the hospital and wave it of with a smile on your face."
        $ += 0
        jump goose_end

    label honk:
        y "Honks back at the goose"
        go "surprised honks"
        y "Honks back at the goose"
        go "angry honks"
        y "honks in response"
        "After having honked insults at the goose the entire trip and dropped them of at the wrong location the goose steals your car keys and tries to escape."
        "You manage to barely get them back before you continue your trip."
        $ -=1
    
    label goose_end:
    jump choose_passenger