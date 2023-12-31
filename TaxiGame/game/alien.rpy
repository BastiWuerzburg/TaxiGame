# Alienszenario
define a = Character("Alien")

# animations 

image alien_moving:
    animation
    "alien"
    xalign -0.8 yalign 0 zpos 0.1
    linear 2.0 xalign 0.0

label alien:

    scene background_video
    show backseats:
        xalign 0.5 yalign 0.5 zpos 1
    show frontseat:
        xalign 0.5 yalign 0.5 zpos 0.5
    show mc:
        xalign 0.9999 yalign 0 zpos 0.2
    show alien_moving
    show dashboard:
        xalign 0.5 yalign 0.5 zpos 0.01

    a "//()2€(&\%7'@€2)==';"
    y "Ah, that's a language I haven't heard before. Would English be a language you speak?"
    a "Yeees, indeeeeed."
    y "Where would you like to go?"
    a "Take meee to your leeeeader. The most poweeeeerful human."
    y "Sure, I can do that."
    y "Might I ask why you wish to meet them?"
    a "..."
    y "No? You don't need to tell me. I hope it's nothing sinister."
    a "Peeeeerhaps..."

    menu:
        "Tanke a choice."
        "President":
            jump president
        "A random person":
            jump random_person
        "Your wife":
            jump wife

    label president:
        a "Teeeell meeee about your kind. What do you consume?"
        y "You mean food? Well, there's many different kinds of foods, depending on culture and stuff."
        y "Many people like pizza, for example. Thats a baked good with a choice of toppings."
        a "Yeees, the carbohydrateeees in doughy form. What toppings are you reeeefeeering to?"
        y "Most common are cheese and tomatoes, or fungus, sometimes pepperoni or spinach."
        a "Fungus? Is that not poisonous to you humans?"
        y "Not all of them are. Some fungi are edible and others need to be prepared correctly, but most are poisonous."
        a "Strange behaviour, you humans."
        y "..."
        y "Here we are. If you go that way, you'll meet the most powerful human on this planet."
        $ karma += 1
        $ money += 50
        jump alien_end

    label random_person:
        a "Soo, what is this ship you useeee?"
        y "Ship? You mean my car? It's basically a big cart to transport people and stuff."
        a "Can you traveeeel through spaceee with it?"
        y "I'm afraid not, humanity hasn't progressed that far yet."
        a "That's sad. Spaceee has many colours and planeeets."
        y "I suppose it is, but I myself am quite happy here on earth, getting to meet different kinds of people like yourself."
        a "..."
        y "There! That's the leader of earth. The guy with the tin foil top hat. Go talk to him, he's a funny guy."
        a "This is wheeereee you humans say „thank you“, is that correeect."
        y "You are very welcome."
        $ karma += 0
        $ money += 20
        jump alien_end

    label wife:
        a "Wheeereee areee weee going?"
        y "To my home."
        a "Reeealy? Areee you theee „king“ of humans?"
        y "I am not, but I know the most powerful human."
        a "Theeen should weee not go to theeeir homeee?"
        y "We are."
        a "What an odd human."
        y "So, where are you from?"
        a "I'm from ~3>≠¥£8, theeereee is no eeenglish word."
        y "Hm, how troublesome. Anyway, here we are. If you ring the top doorbell, my wife should answer. You can meet her then."
        $ karma -= 1
        $ money += 30

    label alien_end:
    jump choose_passenger