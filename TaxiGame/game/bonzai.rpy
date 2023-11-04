# BonzaiSzenario

define bo = Character("Bonzai Tree")

label bonzai:
    y "My my, a Bonsai, haven’t had a plant in a while."
    bo "Yeah, I spruced myself of for a root-ine meeting."
    y "Where would you like to go, my friend?"
    bo "The woods, please, in just a few sTreets. The latest project has leafed my team a bit stumped."
    y "Well, I hope things will be resolved at the meeting."
    bo "Yeah, last time time was online and the oak had a bit of trouble logging in."
    y "Good thing it’s not online anymore then."
    bo "Quite, sometimes the stupidity in our branch makes me want to be able to face palm."
    y "It cant be helped. "
    bo "Actually, wood you have some water for me, I happen to be quite thirsty."

    menu:
        "Give them your water":
            jump give_water
        "Bring them to a public water fountain":
            jump public_water_fountain
        "Turn up the heat":
            jump heat

    label give_water:
        y "Yes, I always carry a water bottle in my cab."
        bo "That is indeed a good thing this nice Sap-timber."
        y "Here, have some water. Load up your baTree. I know it's a great pine to be thirsty. you give the tree your water bottle"
        bo "Many thanks. Now I might tree able to focus and find the root of the problem. Great progress for the indus-tree."
        y "You're very welcome. We should be arriving momentariTree, just after that leaf-t turn."
        bo "Oak-ay! Here, have some oxygen, no twigs attached."
        $ karma += 2
        $ money += 0
        jump bonzai_end

    label public_water_fountain:
        y "I’d like to keep my water bottle, so I’ll drive you to the park for a quick break. There should be a fountain there."
        bo "Excellent! I couldn’t stand the sappy comments from the Tree-o, especially Acorn. It’s nuts!"
        y "The park is right over there. I’ll wait for you while you go get a drink."
        bo "Thank you. I live for rest."
        $ karma += 1
        $ money += 1
        jump bonzai_end

    label heat:
        y "Sorry, I don’t have any water for you. You turn up the heat"
        bo "My, what a shame. If I can’t focus, the others are going to throw shade at me."
        bo "Hmm, is it just me, or am I drying out a bit?"
        y "It got a bit cold, so I turned up the heat."
        bo "I can’t be-leaf it! How could you? What tree- chery! I could get sick!"
        y "Really? But it’s no issue, we’ll be at your destination before that happens."
        bo "That’s a re-leaf. What horrible tree-tment."
        $ karma -= 5
        $ money += 0

    label bonzai_end:
    jump choose_passenger
