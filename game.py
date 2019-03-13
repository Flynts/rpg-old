import rpg 

"""set up rooms"""
kitchen = rpg.Room("Kitchen")
kitchen.set_description ("A dank and dirty room buzzing with flies.")

dining_hall = rpg.Room("Dining Hall")
dining_hall.set_description ("A large room with ornate golden decorations on each wall.")

ball_room = rpg.Room("Ball Room")
ball_room.set_description ("A vast room with a shiney wooden floor.")

"""set up room interlinks"""
kitchen.link_room (dining_hall, "south")
ball_room.link_room (dining_hall, "east")
dining_hall.link_room (kitchen, "north")
dining_hall.link_room (ball_room, "west")

"""set up items"""
club = rpg.Item ("club")
club.set_description ("a heavy wooden club")
dining_hall.set_item (club)

bread = rpg.Item ("bread")
bread.set_description ("a loaf of rough milled bread.")
kitchen.set_item(bread)

cheese = rpg.Item ("cheese")
cheese.set_description ("a large wedge of tasty looking cheese.")
ball_room.set_item (cheese)

"""set up characters"""
dave = rpg.Enemy("Dave", "A smelly zombie")
dave.set_conversation("Errrrgh, Brains!")
dave.set_weakness("cheese")
dining_hall.set_character(dave)

graham = rpg.Enemy ("Graham", "A lurching skeleton")
graham.set_conversation("Clatter, creak.")
graham.set_weakness("club")
ball_room.set_character(graham)

burt = rpg.Friend ("Burt", "An old man, who is sitting, sadly in the corner.")
burt.set_conversation("I have been stuck here for so long, give me a hug?")
burt.set_gift("The zombie hates cheese and there is no point stabbin'the skinny fella, it needs a good solid whackin'.")
kitchen.set_character(burt)

#end of setting up, start of main code.

"""initilise conditions"""
current_room = kitchen     
backpack = []
dead = False

"""main code"""
while dead == False:		
    print("\n")         
    current_room.get_details() 
    # Get and display room discription and inhabitants
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_room.get_item()
    if item is not None:
        item.describe()

    command = input.lower("> ")

    # Check whether a direction was typed
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)

    #check if an item is taken
    elif command == "take":
        if item is not None:
            backpack.append(item.name)
            print("You have added", item.name, "to your backpack.")
            current_room.item = None
            
    # display backpack contents            
    elif command == "inventory":
        for thing in backpack:
            print ("In the backpack is", thing)


    # Check if talk was selected
    elif command == "talk":
        inhabitant.talk()

    # Check if fight was selected
    elif command == "fight":
        decide = True
        while decide == True:
            fight_with = input("What will you fight with?")
            if fight_with in backpack:
                decide = False
            else:
                print("There is not one of those in your pack.")
                decision = input ("Do you want to choose again?")
                if decision == "no":
                    decide = False

        if  inhabitant.fight(fight_with) == True:
            print("well done, you won the fight.")
            current_room.character=None
            if inhabitant.get_defeated() == 2:
                print("Congratulations, you have vanquished the enemy horde!")
                dead = True
        else:
            print("oh, dear. You lost!\nGame over.")
            dead = True


    elif command == "give gift":
        gift_item = input ("What do you give your new friend.")
        inhabitant.give_gift(gift_item)

    else:
        print("I don't know how to " + command)




