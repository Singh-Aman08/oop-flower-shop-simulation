# Name: Aman Kumar Singh
# Section: Msc Data Science
# This code file creates a Bouquet Class which contains all the bouquet related information.

class Bouquet:
    """Represents a bouquet.
    Attributes:
        greenery (int): Gives the number of bunches of greenery in the bouquet.
        roses (int): Gives the number of bunches of roses in the bouquet.
        daisies (int): Gives the number of bunches of daisies in the bouquet.
        price (float): Gives the price of the bouquet.
        time_to_prepare (float): Gives the time required to make this bouquet.

    Method:
        bouquet_price: Returns the price of the bouquet.
        time_to_prepare_bouquet: Returns the time required to prepare a bouquet.
    """

    def __init__(self,greenery, roses, daisies, price, time_to_prepare):
        """ Constructor which initializes the number of bunches of greenery, roses, daisies
             required to prepare a bouquet. It also initializes the price and time required
            to prepare a bouquet."""
        self.greenery = greenery
        self.roses = roses
        self.daisies = daisies
        self.price = price
        self.time_to_prepare = time_to_prepare


    def bouquet_price(self):
        """Returns the price of the bouquet."""
        return self.price

    def time_to_prepare_bouquet(self):
        """Returns the time required to prepare the bouquet."""
        return self.time_to_prepare


# Object creation of bouquet types: Fern-Tastic, Be_Leaf_in_Yourself, You Rose to the occasion
fern_tastic=Bouquet(4,0,2,18.50,20)
be_leaf_in_yourself=Bouquet(2,1,3,17.75,30)
you_rose_to_the_occasion=Bouquet(2,4,2,32.50,45)
