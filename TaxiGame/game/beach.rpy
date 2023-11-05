# Scenario 4: Beach-Trip Character Name Ariel
define ar = Character("Ariel")

label beach:

    scene background_video
    show backseats:
        xalign 0.5 yalign 0.5 zpos 1
    show frontseat:
        xalign 0.5 yalign 0.5 zpos 0.5
    show mc:
        xalign 0.9999 yalign 0 zpos 0.2
    show beach:
        xalign 0 yalign 0 zpos 0.1
    show dashboard:
        xalign 0.5 yalign 0.5 zpos 0.01

    ar "Are you free?"
    y "Sure. Where to?"
    ar "To the beach! It's been forever since I've seen the ocean…"
    y "Are you planning on swimming?"
    ar "Of course, I just love the water, but it's been so many years. Ever since I got married there really hasn't been the chance to go."

    menu:
        "Make a choice."
        "Advise its too cold to swim":
            jump too_cold
        "say nothing":
            jump say_nothing
        "Encourage them so they get sick":
            jump get_sick

    label too_cold:
        y "I'll take you to the beach, but don't you think it's too cold to swim? It's freezing out there."
        ar "Oh, you think so? But I really want to, I miss it so much and who knows when I'll get another chance to."
        y "What's keeping you?"
        ar "Everything really. Housework and the kids, and my husband just doesn't seem to understand that I miss the ocean."
        ar "And of course what he doesn't deem important can't possibly be important to anyone else. Who does he even think he is? The prince?"
        y "Maybe you should talk with him about that?"
        ar "Oh sure. But then he tells me that sure I can do whatever I want, but also doesn't really make an effort to coordinate our schedules, to make it actually possible."
        y "Sounds like you really need this time to yourself."
        ar "Exactly so I'm going to the Beach. I will take my time and just enjoy the calm and quiet."
        y "The sea sure is peaceful compared to the busy citylife, but you should take care not to get sick."
        ar "It's so kind of you to worry, but really just dipping my toes in the water can't be that bad."
        y "If you're sure that's what you want just be sure to keep yourself warm, miss. Here you are, enjoy your time at the beach."
        ar "Thanks, I will."
        $ karma += 1
        $ money += 20
        jump beach_end

    label say_nothing:
        y "I see. Does the ocean mean a lot to you then?"
        ar "Oh definitely. My family used to live right at the beach and my Grandpa would take boat trips with me all the time when I was a kid."
        ar"The gentle sea, the salty breeze, a blue sky and nothing but the seagulls cries breaking the peaceful sound of the waves. It really was magical time."
        y "That sounds lovely. Then why haven't you been in so long?"
        ar "Oh just the city keeps me. After my grandparents died, my family moved into the city and I got married and I've just been too busy."
        ar "My mom is getting older, and needs help a lot. Lately she even has trouble just carrying the groceries."
        ar "I guess it will eventually get better when our kids grow up a little."
        y "How old are your kids?"
        ar "We've got two little girls, they're turning seven in a month. I love them to death but it's really stressful too, you know?"
        ar "My husband really doesn't put in a lot of effort to coordinate our schedules." 
        ar "Maybe I should just bring the girls with me next time I want to go to the beach."
        ar "Oh do you see that little cabin? Just let me get off there, that's where we used to keep our boats." 
        y "I see. There you go, enjoy your time here."
        $ karma += 0
        $ money += 20
        jump beach_end

    label get_sick:
        y "Oh it's just great to swim in the ocean, isn't it? Nevermind the weather, I'm suuure you won't get sick."
        ar "You don't think it's a bit too cold? I really couldn't afford to get sick, I barely had time to go out today."
        y "You won't, you won't! Don't worry so much, miss. In fact swimming in cold water is supposed to be healthy, right?"
        y"I think I've seen a lot of people doing that ice-bathing thing lately."
        ar "Ice-bathing? I guess it'll really be fine then. I was worried, but when I was a kid, I was never really cold out on the water."
        ar "All I remember is how I enjoyed it, so I wanted to relive that feeling."
        y "You see? Of course you're gonna have a great time. There we are, the beach and doesn't the water just look lovely?"
        ar "Oh, absolutely, yes it does! Thanks for taking me."
        y "You enjoy your time and be sure to stay in the water for a while!"
        $ karma -= 1
        $ money += 20

    label beach_end:
    jump choose_passenger