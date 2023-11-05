# Verlorener Geldbeutel
define wi = Character("Wife")

label game_end:

    scene background_video
    show backseats:
        xalign 0.5 yalign 0.5 zpos 1
    show frontseat:
        xalign 0.5 yalign 0.5 zpos 0.5
    show mccalling:
        xalign 0.9999 yalign 0 zpos 0.2
    show dashboard:
        xalign 0.5 yalign 0.5 zpos 0.01

    "You are calling your wife."

    # TODO dialog

    # TODO show score

    "The END"
    
    return