define biaj = Character("Brain in a jar")

label simulation:

    y "So, how are you today?"
    biaj "Quite well. This under water craft seems equipped for many happenings."
    y "Ok…? Anyway, where would you like to go?"
    biaj " Ah yes, a destination. I suppose Atlantis would do."
    y "I’m not quite sure how to get there. Is the aquarium alright too?"
    biaj "Yes, that’s what I said."
    y "Alrighty then, let’s go."
    biaj "Yes, depart."
    y "(It seems that brain is in a simulation)"
    menu:
        "Take a choice."
        "Tell them the truth":
            jump truth
        "Play along":
            jump play_along
        "Change the parameters":
            jump change_the_parameters
            
    label truth:
        y "Umm, Brain, my friend, are you aware that the world you’re living in is, in fact, a simulation?"
        biaj "Truly? But that can’t be. Everything is so real."
        y "It’s the truth. We are not in a submarine, but on land. Think about it. How would you be able to withstand the pressure of the sea floor in that jar of yours."
        biaj "..."
        biaj "You have a point… What about atlantis?"
        y "Atlantis is a myth. A legend humans came up with."
        biaj "..."
        y "I’ll give you some time to process."
        biaj "..."
        "You stop at the aquarium and the brain gets of the taxi"
        "After getting back to solid ground it just stays still on the walkway."
        "You decide to drive away and continue your day as usual"
        $ karma += 1
        $ money += 0
        jump simulation_end
    
    label play_along:
        y "You know, Atlantis is quite the while away. Are you sure you will be able to afford the trip?"
        biaj " I can. I might not look like it, but I’m a politician on a diplomatic mission. So I earn quite a sum"
        y "That’s nice. Have you ever been to Atlantis? I haven’t."
        biaj "No, but I hear it’s a beautiful place worth seeing."
        y "How nice."
        "You proceed to drive to the aquarium as requested "
        y "We have arrived dear sir."
        "The Brainn exits the taxi, thanks you, pays and leaves leaving you to continue your day as usual."
        $ karma += 0
        $ money += 0
        jump simulation_end
    
    label change_the_parameters:
        "You decide to change the parameters of the simulation"
        biaj "What? What happened, why are we in candyland all of a sudden? How did we get here?"
        y "What do you mean? We’ve always been here."
        biaj "No, we were in the ocean just a minute ago."
        y "Maybe you were dreaming"
        biaj "Perhaps I was…"
        "You decide to change the parameters again"
        biaj "IT HAPPENED AGAIN! Now we’re in hell!"
        y "Are we? I thought you said candyland."
        biaj "What is happening??"
        y "Nothing unusual."
        "You drop the extremely confused brain of at the aquarium and they pay you the normal price."
        "You drive away hoping you didn´t ruin their mental stability to much"
        $ karma -= 1
        $ money += 0
    
    label simulation_end:
    jump choose_passenger