# Old lady with groceries
define ol = Character("Old Lady")

label old_lady:

     ol "Hello there, could you take me to Fedora road 5 please?"
     y "Sure thing"
     "The old lady lifts two heavy looking grocery seperately into the taxi with a bit of effort and you depart soon after."
     ol "Oh what I would do to be young again..."
     y "Those are some heavy looking groceries, what are they for? I doubt you need it all yourself."
     ol "Your guess is completely right. I got some food, halloween decoration and candy for the upcoming holidays."
     ol "My granddaughters are coming over as well so I wanted to prepare some food and other things to make it a pleasent visit for them."
     y "That sounds absolutely lovely, I hope you will have a nice feast!"
     ol "Thank you very much. Im sure you will also have a great time, just be nice and keep working hard and you will have an even better time then me."
     "You arrive at the requested location and the lady steps out of the vehicle but leaves the groceries in the taxi"
     y "Aren´t you going to take your bags with you?"
     ol "Oh yes I am, but I´ll open the doors first so I wont have to work as hard to get them upstairs."

     menu:
          "Help her with the groceries":
               jump help_old_lady
          "Wait for her to finish":
               jump wait_old_lady
          "Steal some food":
               jump steel_food
 
     label help_old_lady:
          y "Let me help you with those bags."
          ol "Oh that is so kind of you sir!"
          "You get out of the car and help the lady carry her groceries up to the fourth floor where she lives"
          ol "Thank you so much for your help! It would have taken me double, no triple as long to carry these here than without your help. How could I repay your kindness?"
          y "You flatter me, all that matters is that you can now prepare the meal for your family earlier than planned."
          ol "Thank you so, so much!"
          y "It is my pleasure, your welcome."
          "You walk back downstairs and get back to driving your taxi"
          jump old_lady_end

     label wait_old_lady:
          "You decide to wait untill the lady returns to pick up her groceries which she does in 4 minutes"
          ol "Thank you for waiting for me. I know people who would have driven away while I wasn´t present. You are a kind person sir and I hope you have a nice holiday."
          y "No problem, you have good holidays as well."
          "As you drive away you wonder what floor the lady lived on for her to take so long to unlock a door"
          jump old_lady_end

     label steel_food:     
          "Deciding that you want to \"burrow\" groceries you step on the gas pedal and drive away."
          "As you turn the corner a block away you barely make out the old woman looking around in a panic in your rear mirror."
          "Congratulations. You have taken the groceries of an old lady. Do you feel proud of yourself?"

     label old_lady_end:
     jump choose_passenger
