# Name: Aman Kumar Singh
# Section: Msc Data Science
# This code file creates a Flower Class which contains all the flower related information.

class Flower:
    """
    Represents a flower
    Attributes:
        name (str): Name of a flower.
        greenhouse_capacity (int): The capacity of the greenhouse to store a particular flower.
        depreciation (float): Depreciation of the flower in the greenhouse.
        greenhouse_per_bunch_cost (float): Gives the greenhouse cost of a flower bunch.
    """
    def __init__(self,name, greenhouse_capacity, depreciation, greenhouse_per_bunch_cost):
        """Constructor which initializes name, depreciation, greenhouse capacity and
        greenhouse bunch rate of a flower"""
        self.name = name
        self.greenhouse_capacity = greenhouse_capacity
        self.depreciation = depreciation
        self.greenhouse_per_bunch_cost = greenhouse_per_bunch_cost



# Object creation of flowers like roses, daisies and greenery.
rose = Flower("Roses",200,0.4,1.50)
daisies = Flower("Daisies",250,0.15,0.80)
greenery = Flower("Greenery",400,0.05,0.20)