# Verlorener Geldbeutel
define wo = Character("Wallet Owner")

label wallet:

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

    "You notice a wallet on the back seat"
    y "Oh, someone left their wallet. I wonder what to do with it."

    menu:
        "Make a choice."
        "deliver it to the address you found in it":
            jump address
        "Call the number in it so the owner can come fetch it":
            jump number
        "Keep it":
            jump keep

    label address:
        y "Well, let's see…gift cards, business cards, and an address, sure, I can bring it there."
        "you drive to the address and leave it in the mailbox"
        $ karma += 0
        $ money += 0
        jump wallet_end

    label number:
        y "It seems the wallet has contact information."
        "you call the number"
        y "Hello? I found this wallet with this phone number."
        wo "Really? Thank goodness, I was in the middle of panicking about not finding it."
        y "Well, good thing I found it then. I'll leave it for you at the police station in top-hat street."
        wo "Thank you so much!"
        $ karma += 1
        $ money += 0 
        jump wallet_end

    label keep:
        y "Hmm, this has a good sum in it…"
        y "I do need a little change. The gas prices are rising after all."
        y "I'm going to keep this, but maybe I'll leave the cards at the next mail station."
        "you keep the wallet"
        $ karma -= 1
        $ money += 100
    
    label wallet_end:
    jump choose_passenger