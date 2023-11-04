define dct = Character("Drunken Conspiracy Theorist")
define y = Character("You")

label conspiracy:

    dct "You gotta get me out of here! The government is mind reading and pidgeons are coming!"
    y "Pigeons? Thats a new one. Where do you want to go?"
    dct "Anywhere is fine, just not here! Take this tinfoil hat,its the only protection against their mind reading feathers."
    
    menu:
    
        "Accept the tinfoil hat and drive him to his destination":
            jump tinfoil_hat
        "Make subtle pigeon noises":
            jump pigeon
        "Drive arround to increase his payment until he is sober":
            jump drive_sober
            
    label tinfoil_hat:
        dct "You get it my man, its rare to see any people who actually acknowledge the truth."
        y "Sure... have a nice ride."
        jump conspiracy_end
    
    label pigeon:
        dct "Oh no... they´ve found us! Drive faster we need to escape! Can you hear them ecolocate us?"
        y "What do you mean? I can´t hear anything."
        dct "Why aren´t you accelerating? They are all aroun... wait... youre one of THEM! Halt the car this instant!"
        y "stops the car"
        dct "Opens door and runs of youll never take me alive!!!"
        jump conspiracy_end
    
    label drive_sober:
        "You drive around for hours" # background changes to darker colour
        dct "waking up ugh... where am i? who are you?"
        y "Im your taxi driver and youve asked me to drive as far away from the mind reading pidgeons as possible"
        dct "wha...? I was just at the bar! You didnt kidnap me did you?"
        y "Nope, now pay up. You have amassed quite the price due to time and distance traveled."
        y "Also, take back your tinfoil hat. I don´t want it anyway."
        "The drunken conspiracy theorist pays up unhapily and gets out. Next time wake the drunk person up you idiot!"
    
    label conspiracy_end: