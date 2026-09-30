class Item:
    'an Item class for the catalog'
    internal_id = 100
    def __init__(self):
        Item.internal_id += 1
        self.id = Item.internal_id
        self.quantity = 0
        # Other attributes may be defined below. This code is hidden. See the description for details.
        # ...
        
class Catalog:
    'a simple Catalog class'
    
    def __init__(self):
        'the constructor'
        self.items=[]
        
    def add(self, item):
        'add an item to the catalog'
        return self.items.append(item)
    
    def has_style(self, desired_style):
        '''returns true if catalog has an item of the given style'''
        for obj in self.items:
            if obj.style == desired_style:
                return True
        return False
    
    def size(self):
        '''return the number of items in the catalog'''
        return len(self.items)
	# Write the lookup method here:
    