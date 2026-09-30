class RealEstateSystem:
    def __init__(self):
        """ (RealEstateSystem)
        Initialize the homes list
        """
        self.homes = []
        
    def add_home(self, home):
        """ (RealEstateSystem, Home) -> NoneType
        Adds a home to our system
        """
        self.homes.append(home)
    
    def extract_minimum_price(self):
        """ (RealEstateSystem) -> int
        Return the lowest priced home in the system, or -1 if there are no houses in the system
        """
        # complete this code


class Home:
    """ An instance of a home """
    def __init__(self, price):
        """ (Home, float)
        Initialize a home
        """
        self.price = price