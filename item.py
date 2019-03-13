class Item():
    def __init__(self, item_name):
        self.name = item_name
        self.description = None

    def set_description (self, item_description):
        self.description = item_description

    def get_description(self):
        return self.description

    def get_details(self):
        print (self.name,"\n---------------\n",self.description,"\n")

            # Describe this item
    def describe(self):
        print( "In the room is a", self.description  )
