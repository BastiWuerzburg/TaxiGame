define dct = Character("Drunken Conspiracy Theorist")

label conspiracy:

    scene background_video
    show backseats:
        xalign 0.5 yalign 0.5 zpos 1
    show frontseat:
        xalign 0.5 yalign 0.5 zpos 0.5
    show mc:
        xalign 0.9999 yalign 0 zpos 0.2
    show conspiracy:
        xalign 0 yalign 0 zpos 0.1
    show dashboard:
        xalign 0.5 yalign 0.5 zpos 0.01

    dct "You gotta get me out of here! The government is mind reading and pidgeons are coming!"
    y "Pigeons? Thats a new one. Where do you want to go?"
    dct "Anywhere is fine, just not here! Take this tinfoil-tophat,its the only protection against their mind reading feathers."
    
    menu:
        "Take a choice."
        "Accept the tinfoil-tophat and drive him to his destination":
            jump tinfoil_hat
        "Make subtle pigeon noises":
            jump pigeon
        "Drive arround to increase his payment until he is sober":
            jump drive_sober
            
    label tinfoil_hat:
        dct "You get it my man, its rare to see any people who actually acknowledge the truth these days."
        y "Sure... have a nice ride."
        dct "I thank you from the bottom of my heart, you have saved my life today."
        $ karma += 1
        $ money += 20
        jump conspiracy_end
    
    label pigeon:
        dct "Oh no... they have found us! Drive faster we need to escape! Can you hear them ecolocate us?"
        y "What do you mean? I can not hear anything."
        dct "Why are you not accelerating? They are all aroun... wait... youre one of THEM! Halt the car this instant!"
        "You stop the car as per request"
        "The man stumbles out of the car and starts to frantically run of"
        dct "You will never take me alive! I have seen through your schemes, you wont ever fool me!"
        $ karma += 0
        $ money += 0
        jump conspiracy_end
    
    label drive_sober:
        "You drive around for a few hours making the taximeter count higher in the proccess" # background changes to darker colour
        "Having sobered up the man wakes up after having fallen asleep"
        dct "Where am i? who are you?"
        y "Im your taxi driver and youve asked me to drive as far away from the mind reading pidgeons as possible"
        dct "wha...? I was just at the bar! You didnt kidnap me did you?"
        y "Nope, now pay up. You have amassed quite the price due to time and distance traveled."
        y "Also, take back your tinfoil-tophat. I already have my own hat."
        "The drunken conspiracy theorist pays up unhapily and gets out." 
        dct "Next time wake the drunk person up you idiot!"
        $ karma -= 1
        $ money += 60
    
    label conspiracy_end:
    jump choose_passenger