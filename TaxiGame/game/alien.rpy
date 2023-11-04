# Alienszenario
define a = Character("Alien")

label alien:

    a "/()2€(&%7ˋ@€2)==ˋ;"
    y "Ah, that’s a language I haven’t heard before. Would English be a language you speak?"
    a "Yeees, indeeeeed."
    y "Where would you like to go?"
    a "Take meee to your leeeeader. The most poweeeeerful human."
    y "Sure, I can do that."
    y "Might I ask why you wish to meet them?"
    a "…"
    y "No? You don’t need to tell me. I hope it’s nothing sinister."
    a "Peeeeerhaps…"

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
        y "You mean food? Well, there’s many different kinds of foods, depending on culture and stuff."
        y "Many people like pizza, for example. Thats a baked good with a choice of toppings."
        a "Yeees, the carbohydrateeees in doughy form. What toppings are you reeeefeeering to?"
        y "Most common are cheese and tomatoes, or fungus, sometimes pepperoni or spinach."
        a "Fungus? Is that not poisonous to you humans?"
        y "Not all of them are. Some fungi are edible and others need to be prepared correctly, but most are poisonous."
        a "Strange behaviour, you humans."
        y "…"
        y "Here we are. If you go that way, you’ll meet the most powerful human on this planet."

    label random_person:
        a "Soo, what is this ship you useeee?"
        y "Ship? You mean my car? It’s basically a big cart to transport people and stuff."
        a "Can you traveeeel through spaceee with it?"
        y "I’m afraid not, humanity hasn’t progressed that far yet."
        a "That’s sad. Spaceee has many colours and planeeets."
        y "I suppose it is, but I myself am quite happy here on earth, getting to meet different kinds of people like yourself."
        a "…"
        y "There! That’s the leader of earth. The guy with the tin foil top hat. Go talk to him, he’s a funny guy."
        a "This is wheeereee you humans say „thank you“, is that correeect."
        y "You are very welcome."

    label wife:
        a "Wheeereee areee weee going?"
        y "To my home."
        a "Reeealy? Areee you theee „king“ of humans?"
        y "I am not, but I know the most powerful human."
        a "Theeen should weee not go to theeeir homeee?"
        y "We are."
        a "What an odd human."
        y "So, where are you from?"
        a "I’m from ~3>≠¥£8, theeereee is no eeenglish word."
        y "Hm, how troublesome. Anyway, here we are. If you ring the top doorbell, my wife should answer. You can meet her then."

    label alien_end:
    jump choose_passenger