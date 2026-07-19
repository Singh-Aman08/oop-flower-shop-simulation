# Name: Aman Kumar Singh
# Section: Msc Data Science
# This code file creates a Vendor Class which contains all the vendor related information.

class Vendor:
    """ Represents a vendor who sells flowers.
        Attributes:
            vendor_name (str):  The name of the vendor.
            rose_bunch_rate(float): The price of a bunch of rose.
            daisies_bunch_rate (float): The price of a bunch of daises.
            greenery_bunch_rate (float): The price of a bunch of greenery

        Methods:
            vendor_catalogue : A class method which returns the catalog of all flower
            vendors managed by this class.
    """
    def __init__(self, vendor_name, roses_rate, daisies_rate, greenery_rate):
        """ This is a constructor method to initialize the name of the
        vendor and the bunch rate of rose, daisies and greenery.
        """
        self.vendor_name = vendor_name
        self.rose_bunch_rate = roses_rate
        self.daisies_bunch_rate = daisies_rate
        self.greenery_bunch_rate = greenery_rate

    @classmethod  #class method decorator
    def vendor_catalogue(cls):
        """
        A class method which returns the  nested dictionary which contains the vendor name
        and the flowers bunch rate.
        """

        return  {"Evergreen Essentials": {"Roses_rate": 2.80, "Daisies_rate": 1.50, "Greenery_rate": 0.95},
                             "FloraGrow Distributors": {"Roses_rate": 1.60, "Daisies_rate": 1.20, "Greenery_rate": 1.80}}

# Object creation of vendors like Evergreen Essentials and Flora Grow Distributors.
evergreen_essentials = Vendor("Evergreen Essential",2.80,1.50,0.95)
flora_grow_distributors = Vendor("Flora Grow",1.60,1.20,1.80)