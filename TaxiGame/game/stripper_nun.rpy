# Stripper-Nun
define sc = Character("Sister Candice")

label stripper_nun:

    scene background_video
    show backseats:
        xalign 0.5 yalign 0.5 zpos 1
    show stripper:
        xalign 0.45 yalign 10 zpos 0.6
    show frontseat:
        xalign 0.5 yalign 0.5 zpos 0.5
    show mc:
        xalign 0.9999 yalign 0 zpos 0.2
    show dashboard:
        xalign 0.5 yalign 0.5 zpos 0.01
    
    y "Where to?"
    sc "St. Micheals Church please."
    y "..."
    sc "The lord says who is without sin cast the first stone. I can feel you judging me."
    y "Oh not at all, miss. I was simply surprised. I wouldn't think a young lady such as you would be interested in religion."
    sc "I'm a nun actually."
    y "..."
    sc "I know I'm not currently dressed like it but I am. In fact I'm on my way to service." 
    y "Then is it you personal preference to dress like this outside of your convent?"
    sc "Well, the lord guides us through the mysterious sea of life and we've hit a bit of troubled waters lately."
    y "Troubled waters?"
    sc "Well, our abbess joined the convent after she finished treatment for her gambling addiction. And she was better. It was all fine." 
    sc "But you see our abbess has control over all the finances in the monastery."
    y "That seems really risky. Giving someone with that history ALL your money."
    sc "Yeah, yeah, you know what they say about hindsight. But Jesus teaches us to give second chances." 
    sc "It doesn't really matter at this point though, we're already in way over our heads with debt."
    y "And you dressing like this somehow helps with that?"
    sc "well not necessarily just dressing like this, but it does make the dancing easier."
    y "...sooooo you're a stripper?"
    sc "I'm an EXOTIC DANCER!"
    y "My apologies. Exotic dancer then. So, you decided to use the greed of middle-aged men to save your monastery?"
    sc "Well the bible does teach to use our talents to make the most of our lives and it actually makes good money." 
    sc "I will stop the second we don't need it anymore, until then it's the best way I can help." 
    sc "The Lord will understand my intentions and forgive me in his eternal grace."
    y "And do your fellow sisters know about how you're helping them?"
    sc "Ah not exactly and they MUSTN'T find out about it, so I'll have to change in the car, you don't really mind, right?"

    menu:
        "Put up the privacy screen":
            jump privacy_screen
        "Bring her to a private place, so she can dress more comfortably":
            jump private_place
        "Peep on her":
            jump peep

    label privacy_screen:
        y "Of course, go ahead, I won't be looking. It's not my Job to judge anyone." 
        sc "Thank you, Mister. I appreciate it."
        scene background_video
        show backseats:
            xalign 0.5 yalign 0.5 zpos 1
        show nun:
            xalign 0.45 yalign 10 zpos 0.6
        show frontseat:
            xalign 0.5 yalign 0.5 zpos 0.5
        show mc:
            xalign 0.9999 yalign 0 zpos 0.2
        show dashboard:
            xalign 0.5 yalign 0.5 zpos 0.01
        y "Are you dressed yet? We're arriving."
        sc "Oh yes, I'm decent again. I need to hurry along. May God bless you, good Sir!"
        $ karma += 1
        $ money += 20
        jump stripper_nun_end

    label private_place:
        y "Ah, I don't think that's the best Idea, anyone could see you, a car has windows after all. Why don't I let you get out at a public restroom so you can change?"
        sc "Sure, that'd be alright as well. Oh, I think I see one right ahead. Please wait a second!"
        "she gets out and returns after a few minutes dressed in a habit"
        scene background_video
        show backseats:
            xalign 0.5 yalign 0.5 zpos 1
        show nun:
            xalign 0.45 yalign 10 zpos 0.6
        show frontseat:
            xalign 0.5 yalign 0.5 zpos 0.5
        show mc:
            xalign 0.9999 yalign 0 zpos 0.2
        show dashboard:
            xalign 0.5 yalign 0.5 zpos 0.01
        sc "Thank you for waiting, let's head to the church now."
        y "Of course, sister. We're almost there."
        $ karma += 0
        $ money += 25
        jump stripper_nun_end

    label peep:
        y "Oh sure, I don't mind."
        sc "Thank you, good Sir."
        sc "..."
        y "..."
        sc "Don't you want to put up the privacy screen?"
        y "Oh no, I don't think that's necessary, is it? I promise I won't peek."
        sc "Oh you won't"
        y "Of course not, I need to keep my eyes on the road!"
        sc "Alright then..."
        "Sister Candice gets undressed, and you peep at her through the rear mirror. When she's almost finished dressing, she notices your eyes on her"
        scene background_video
        show backseats:
            xalign 0.5 yalign 0.5 zpos 1
        show nun:
            xalign 0.45 yalign 10 zpos 0.6
        show frontseat:
            xalign 0.5 yalign 0.5 zpos 0.5
        show mc:
            xalign 0.9999 yalign 0 zpos 0.2
        show dashboard:
            xalign 0.5 yalign 0.5 zpos 0.01
        sc "Excuse me! What do you think you're doing?! This is not your private peepshow. You should be ashamed of yourself Stop the car right now and let me get off!"
        y "I didn't think one more guy seeing you in underwear would really make a difference. But as you wish, miss. Then this is your stop."
        "Sister Candice slams open the car door and runs off with an outraged huff"
        $ karma -= 1
        $ money += 0

    label stripper_nun_end:
    jump choose_passenger