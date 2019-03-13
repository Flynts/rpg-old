class Room():
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None

# Getters and setters
# For room description
    def set_description (self, room_description):
        self.description = room_description
    def get_description(self):
        return self.description

# For character in room
    def set_character (self, room_character):
        self.character = room_character
    def get_character(self):
        return self.character

# For room name
    def set_name (self, room_name):
        self.name = room_name
    def get_name(self):
        return self.name

# For room item
    def set_item (self, item_name):
        self.item = item_name
    def get_item (self):
        return self.item

# set room description
    def describe(self): 
        print( self.description )

# set links to other rooms
    def link_room (self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link

# describe room
    def get_details(self):
        print (self.name,"\n---------------\n",self.description,"\n")
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print( "The " + room.get_name() + " is to the " + direction)

# move to adjacent room
    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self

