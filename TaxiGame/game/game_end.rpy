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

    # Good ending:
    "The Phone rings, your wife is calling"
    y "Hello, dear, I'm on my way home right now. Do need me to pick up some things on the way?"
    wi "No that's okay, I've got dinner on the stove. How was your day, love?"
    y "It was nice, I had some fascinating customers. And some very weird ones too."
    wi "That's nice, I hope you were kind to all of them, dear. Oh, our daughter called, she said she's bringing the kids round to ours this weekend, so we can come up with some fun activities."
    y "That's some great news, it's been too long, and they grow up way too fast. I can't wait to see them again."
    wi "Then hurry home, my love, we can video call and chat about what they want to do on the weekend."
    y "Yes, honey, I'm almost there."

    # Neutral ending
    "The Phone rings, your wife is calling"
    wf "Hello love, are you heading home soon?"
    y "Yes, love, I'm on my way and I'm starving."
    wi "Oh, you're always hungry! But you're in luck I made you're favorite for dinner."
    y "Oh that's lovely, my day keeps getting better."
    wi "You're such a charmer! Just hurry home and drive safe!"
    y "Yes, dear, I'll be there soon."

    # Bad ending
    "The Phone rings, your wife is calling"
    y "Hello, dear, I'm on my way home now."
    wi "Oh why even bother? Dinner's been ready for ages and everything's gone cold already. I told you I was expecting you home for dinner."
    y "Oh, don't be mad, you know how it is. I'm working!"
    wi "We had guests over! This dinner was scheduled for weeks and you couldn't even manage to remember?"
    y "Look, I'm sorry. I had to work late, it happens! I had so many weird passengers today, you wouldn't even believe it!"
    wi "Yeah well the neighbors were able to finish work on time and came over, they left by now, so I'm going to bed. You can put your dinner portion in the microwave."
    y "Alright. See when I get home, then."

    # TODO show score

    "The END"
    
    return