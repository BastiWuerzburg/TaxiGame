# Scenario 8: K-Drama Plot

define hb = Character("Name Hyun Bong")

label kpop:

    scene background_video
    show backseats:
        xalign 0.5 yalign 0.5 zpos 1
    show frontseat:
        xalign 0.5 yalign 0.5 zpos 0.5
    show mc:
        xalign 0.9999 yalign 0 zpos 0.2
    show bonzai:
        xalign 0 yalign 0 zpos 0.1
    show dashboard:
        xalign 0.5 yalign 0.5 zpos 0.01
    
    hb "To the airport!"
    y "Alright" 
    hb "Please hurry!"
    y "Late to a flight?"
    hb " Yes, yes I am or well it's not my flight."
    y "What's that supposed to mean?"
    hb "Listen, she's my best friend. She's been my best friend since we were kids. But we lost sight of each other after we graduated and recently we met again by coincidence."
    hb "The love of my life is leaving, and I can't let her go. Please, we don't have a moment to lose."
    y "I understand, young man. Don't worry, I'll do my best to get you to the airport on time." 

    menu:
        "Make a choice."
        "Break the speed limit":
            jump break_speed_limit
        "Keep to the speed limit":
            jump speed_limit
        "Drive slowly on purpose":
            jump drive_slowly
    
    label break_speed_limit: 
        hb "You know, Joo-yeon and I have been through so much together. We've shared our dreams, our secrets, and our hopes."
        hb "I can't bear the thought of her leaving without knowing how much I love her. I need to tell her, even if it's the last thing I do."
        hb "Argh, I don't know what she was even thinking!" 
        y "What you're friend?"
        hb "No, my mother! The House servants told me that she and Joo-yeon met and talked and Joo-yeon ran out of the house crying."
        y "That doesn't sound too good."
        hb "And I still don't even know what my mother said, I know she's against us being together, but she won't be able to keep us apart!"
        y "Love is a powerful thing, my friend. I've seen many stories unfold in this taxi. Sometimes, the heart's desire is all that matters."
        y "We're almost at the airport, now go get her!"
        hb "Thank you so much!"
        $ karma += 1
        $ money += 20
        jump kpop_end

    label speed_limit:
        hb "You know, Joo-yeon and I have been through so much together. We've shared our dreams, our secrets, and our hopes."
        hb "I can't bear the thought of her leaving without knowing how much I love her. I need to tell her, even if it's the last thing I do. Can't you drive a bit faster?"
        hb "I can't miss my chance!"
        y "I get it man, but you're no good to her dead, we really need to keep to the speed limit and traffic is terrible this time of day."
        hb "You're right, it's not you're fault, I'm sorry. I'm just so worried I'll never see her again. After what my mother did, I don't even know if Joo-yeon will forgive me."
        y "What's your mother got to do with this?"
        hb "The house servants told me that she and Joo-yeon met and talked and Joo-yeon ran out of the house crying."
        y "That doesn't sound too good"
        hb "And I still don't even know what my mother said, I know she's against us being together, but she won't be able to keep us apart!"
        y "Well whatever she said, I hope you can fix it. We're here now, so good luck, young man!"
        hb "Thank you, Mister!"
        $ karma += 0
        $ money += 30
        jump kpop_end

    label drive_slowly:
        hb "You know, Joo-yeon and I have been through so much together. We've shared our dreams, our secrets, and our hopes."
        hb "I can't bear the thought of her leaving without knowing how much I love her. I need to tell her, even if it's the last thing I do."
        y "Hmmmm." 
        hb "Why are we moving so slow? We really need to hurry, if I miss her, I might never see her again!"
        y "Well if you miss her, then maybe it really wasn't mean to be? Why's she leaving anyway if you're both in love?"
        hb "I Don't really know. All I know is that my mother and her had a talk when suddenly Joo-yeon ran out of there crying."
        hb "I wouldn't even know she's leaving if my mother's assistant hadn't told me about the boarding ticket."
        y "Is there a reason your mother doesn't approve of this girl of yours?"
        hb "Well my mother is very old-fashioned and we don't really come from the same social standing. But that shouldn't matter anymore in this day and age. Can't you go faster?"
        y "I'm going exactly as fast as is reasonable, maybe you should have talked with her before she was heading to an airport."
        hb "I didn't even know, don't make it sound like this is all on me."
        "Akward silence"
        y "…. Well we're here now, so good luck."
        hb "Yeah, the flight just left. I'll go check anyway, but I don't think I'll catch her thanks to you. Thanks for nothing, I guess."
        $ karma -= 1
        $ money += 40

    label kpop_end:
    jump choose_passenger