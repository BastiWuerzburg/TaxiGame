# Stalkerszenario
define s = Character("Stalker")

# animations 

image victim_moving:
    animation
    "victim"
    xalign -0.8 yalign 0 zpos 0.1
    linear 2.0 xalign 0.0

label stalker:

    scene background_video
    show backseats:
        xalign 0.5 yalign 0.5 zpos 1
    show frontseat:
        xalign 0.5 yalign 0.5 zpos 0.5
    show mc:
        xalign 0.9999 yalign 0 zpos 0.2
    show victim_moving
    show dashboard:
        xalign 0.5 yalign 0.5 zpos 0.01

    y "Where would you-"
    s "Anywhere! Away from here! There's this really creepy guy following me."

    menu:
        "Make a choice."
        "Take detours to confuse the stalker":
            jump detours
        "Ask for a specific destination":
            jump specific_destination
        "Drive in the direction they came from":
            jump came_from

    label detours:
        y "Alrighty, I've got you covered. Hop in."
        s "Thank you so much, I just noticed the guy and started walking faster."
        y "You wouldn't be the first one to ask me such a favour." 
        y "I'm going to drive a confusing route and bring you to a populated area, or would you prefer a different location?"
        s "No, that would be great, I can call a friend when I loaded my phone."
        y "No problem at all."
        $ karma += 1
        $ money += 30
        jump stalker_end

    label specific_destination:
        y "Alrighty, where to?"
        s "Anywhere away from here! Please!"
        y "I'm afraid I'm going to need a location."
        s "Please! I need to get away from here!"
        y "To where?"
        s "To the police; yeah, that's where I need to go, or the mall, or home?" 
        s "No - not home, they would follow me there. Then maybe the train station or-"
        y "If you want to get away fast, you should make a decision."
        s "Yes, yes, just take me to the nearest police station."
        y "Very well, off we go."
        $ karma += 0
        $ money += 20
        jump stalker_end

    label came_from:
        y "Where would you like to go?"
        s "Anywhere but here! Quick! There's this creepy stalkers following me!"
        y "Ok, let's go."
        "you drive away and around the block towards the direction your passenger came from"
        y "Here we are, away from where you got in."
        s "Thank you so much."
        $ karma -= 1
        $ money += 10

    label stalker_end:
    jump choose_passenger