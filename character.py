class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    # Describe this character
    def describe(self):
        print( self.name + " is here!" )
        print( self.description )

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True

#creates Enemy as a subclass of character
class Enemy(Character):

    enemies_defeated = 0

    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None


    # Set what this characters weakness is
    def set_weakness(self, weakness):
        self.weakness = weakness

    def get_defeated(self):
        return Enemy.enemies_defeated

    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("You fend " + self.name + " off with the " + combat_item )
            Enemy.enemies_defeated += 1
            return True
        else:
            print(self.name + " crushes you, puny adventurer")
            return False


#creates Friend as a subclass of character
class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.gift = None

    def set_gift(self, gift):
        self.gift = gift

    # Set what happens if you give it a gift
    def give_gift(self,giftitem):
        if giftitem == self.gift
            print ("Listen to me well. " + self.gift)
        print("God luck in there!")








