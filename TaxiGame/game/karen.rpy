# KarenSzenario
define ka = Character("Karen")

label karen:
    ka "Take me to the nearest café."
    y "There are multiple, which one do you mean?"
    ka "Are you deaf? I said the closest one."
    y "Alright, off we go."
    ka "Do you see that girl over there? Green hair, GREEN! This world is devolving! As if they want to merge with the grass."
    y "There’s nothing wrong with dyeing your hair."
    ka "MY hair? No one touches my hair!"
    y "No, I meant ones hair, as in there’s nothing wrong with wanting to dye ones own hair."
    ka "Hmp."
    "You notice a roadwork sign"
    y "Road work ahead? I sure hope it does! Ha ha."
    y "We’re going to have to take a detour."
    ka "A detour? Unacceptable! Take me to your manager!"

    menu:
        "Take her to your manager":
            jump to_manager
        "Let her get out of the car":
            jump throw_out
        "I am the manager":
            jump i_am_manager

    label to_manager:
        y "If you say so."
        ka "Good, finally someone who does!"
        "You drive Karen to the company building"
        y "Here we are, any complaints you can bring to the front desk"
        ka "Fine!"
        jump karen_end

    label throw_out:
        y "Ma’am, you are going to have to leave my cab."
        ka "What?! Why?"
        y "Your behaviour is unprofessional and rude and I have the right to refuse service."
        ka "WHAT? You are the rude one!"
        y "Are you deaf? I said to get out of my cab."
        ka "Inexcusable! I’m never coming back!"
        "Karen leaves"
        y "Good."
        jump karen_end

    label i_am_manager:
        y "I am the manager!"
        ka "gasp How? No manager would be doing a job as lowly as driving a cab."
        y "Well I am and I don’t see why you would need to complain. There’s nothing wrong with a detour."
        ka "Let me out. I’m calling a new cab."
        y "Sure, but it’s still going to cost you."
        ka "Fine! Never again!"

    label karen_end:
    jump choose_passenger