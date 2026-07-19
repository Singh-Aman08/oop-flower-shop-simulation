from math import *
from florist import *
from flower import *
from vendor import *
from bouquet import *
# Name: Aman Kumar Singh
# Section: Msc Data Science
# This code file creates a Flower shop Class which contains all the flower shop related information.

class FlowerShop:
    """Represents a flower shop.
    Attributes:
        Class attributes:
            FLORIST_PER_MONTH_WORKING_HOURS (int) = Gives the monthly working limit of a florist.
            FLORIST_PER_HOUR_RATE (float) = Gives the per hour rate of a florist.
            TOTAL_BUDGET (int) = Gives the budget of the flower shop.
            RENT (int) = Gives the monthly rent of the flower shop.

        Object attributes:
            fern_tastic_demand (int): Number of orders of Fern-Tastic.
            be_leaf_demand (int): Number of orders of Be Leaf in Yourself.
            you_rose_demand (int): Number of orders of You Rose to the Occasion.

    Methods:
        Class Methods:
            florist_count: Number of florists in the flower shop.
            florist_name: Name of the florists in the flower shop.

        Object Methods:
            rose_quantity_before_dep: gives number of roses before depreciation.
            daisies_quantity_before_dep: gives number of daisies before depreciation.
            greenery_quantity_before_dep: gives number of greenery before depreciation.
            rose_quantity: gives number of roses after depreciation.
            daisies_quantity: gives number of daisies after depreciation.
            greenery_quantity: gives number of greenery after depreciation.
            total_shop_income: gives total income of the shop.
            total_employee_cost_per_month: gives total salary of florist per month.
            total_green_house_cost: gives total expenditure on greenhouse per month.
            flower_restock_cost: gives expenditure on restocking flower.
            end_of_month_cash_balance: returns the month end balance of the flower shop.
    """

    #class attributes
    FLORIST_PER_MONTH_WORKING_HOURS = 80
    FLORIST_PER_HOUR_RATE=15.50
    TOTAL_BUDGET=7500
    RENT=800

    def __init__(self, fern_tastic_demand, be_leaf_demand, you_rose_demand):
        """Constructor initializes the order placed for Fern-Tastic, Be Leaf in Yourself and
            You Rose to the Occasion."""
        self.fern_tastic_demand = fern_tastic_demand
        self.be_leaf_demand = be_leaf_demand
        self.you_rose_demand = you_rose_demand

    @classmethod #class decorator
    def florist_count(cls):
        """Returns the total florists working in the flower shop"""
        return Florists.total_florists_count()

    @classmethod
    def florist_name(cls):
        """Return the list of names of florists working in the flower shop"""
        return Florists.florists_name()

    def rose_quantity_before_dep(self):
        """Calculates and returns the number of bunches of roses in the greenhouse before depreciation"""

        # calculates the total number of roses in all the three types of bouquets.
        rose_req_in_fern = self.fern_tastic_demand * fern_tastic.roses
        rose_req_in_be_leaf = self.be_leaf_demand * be_leaf_in_yourself.roses
        rose_req_in_you_rose = self.you_rose_demand * you_rose_to_the_occasion.roses
        total_rose_req = rose_req_in_fern + rose_req_in_be_leaf + rose_req_in_you_rose

        # Rose left after deducting sold roses from greenhouse capacity.
        rose_left = rose.greenhouse_capacity - total_rose_req
        return rose_left

    def daisies_quantity_before_dep(self):
        """Calculates and returns the number of bunches of daisies in the greenhouse before depreciation"""

        # calculates the total number of daisies in all the three types of bouquets.
        daisies_req_in_fern = self.fern_tastic_demand * fern_tastic.daisies
        daisies_req_in_be_leaf = self.be_leaf_demand * be_leaf_in_yourself.daisies
        daisies_req_in_you_rose = self.you_rose_demand * you_rose_to_the_occasion.daisies
        total_daisies_req = daisies_req_in_fern + daisies_req_in_be_leaf + daisies_req_in_you_rose

        # Daisies left after deducting sold roses from greenhouse capacity.
        daisies_left = daisies.greenhouse_capacity - total_daisies_req
        return daisies_left

    def greenery_quantity_before_dep(self):
        """Calculates and returns the number of bunches of greenery in the greenhouse before depreciation"""

        # calculates the total number of greenery in all the three types of bouquets.
        greenery_req_in_fern = self.fern_tastic_demand * fern_tastic.greenery
        greenery_req_in_be_leaf = self.be_leaf_demand * be_leaf_in_yourself.greenery
        greenery_req_in_you_rose = self.you_rose_demand * you_rose_to_the_occasion.greenery
        total_greenery_req = greenery_req_in_fern + greenery_req_in_be_leaf + greenery_req_in_you_rose

        # Greenery left after deducting sold roses from greenhouse capacity.
        greenery_left = greenery.greenhouse_capacity - total_greenery_req
        return greenery_left

    def rose_quantity(self):
        """Calculates and returns the number of bunches of roses in the greenhouse after depreciation"""

        # calculates the total number of roses in all the three types of bouquets.
        rose_req_in_fern = self.fern_tastic_demand * fern_tastic.roses
        rose_req_in_be_leaf = self.be_leaf_demand * be_leaf_in_yourself.roses
        rose_req_in_you_rose = self.you_rose_demand * you_rose_to_the_occasion.roses
        total_rose_req = rose_req_in_fern + rose_req_in_be_leaf + rose_req_in_you_rose

        # calculating the depreciated rose and deducting it from the greenhouse capacity at end of the month.
        rose_left = rose.greenhouse_capacity - total_rose_req
        depreciated_rose = rose_left * rose.depreciation
        available_rose = ceil(rose_left - depreciated_rose)
        return available_rose

    def daisies_quantity(self):
        """Calculates and returns the number of bunches of daisies in the greenhouse after depreciation"""

        # calculates the total number of daisies in all the three types of bouquets.
        daisies_req_in_fern = self.fern_tastic_demand * fern_tastic.daisies
        daisies_req_in_be_leaf = self.be_leaf_demand * be_leaf_in_yourself.daisies
        daisies_req_in_you_rose = self.you_rose_demand * you_rose_to_the_occasion.daisies
        total_daisies_req = daisies_req_in_fern + daisies_req_in_be_leaf + daisies_req_in_you_rose

        # calculating the depreciated daisies and deducting it from the greenhouse capacity at end of the month.
        daisies_left = daisies.greenhouse_capacity - total_daisies_req
        depreciated_daisies = daisies_left * daisies.depreciation
        available_daisies = ceil(daisies_left - depreciated_daisies)
        return available_daisies

    def greenery_quantity(self):
        """Calculates and returns the number of bunches of greenery in the greenhouse after depreciation"""

        # calculates the total number of greenery in all the three types of bouquets.
        greenery_req_in_fern = self.fern_tastic_demand * fern_tastic.greenery
        greenery_req_in_be_leaf = self.be_leaf_demand * be_leaf_in_yourself.greenery
        greenery_req_in_you_rose = self.you_rose_demand * you_rose_to_the_occasion.greenery
        total_greenery_req = greenery_req_in_fern + greenery_req_in_be_leaf + greenery_req_in_you_rose

        # calculating the depreciated greenery and deducting it from the greenhouse capacity at end of the month.
        greenery_left = greenery.greenhouse_capacity - total_greenery_req
        depreciated_greenery = greenery_left * greenery.depreciation
        greenery_available = ceil(greenery_left - depreciated_greenery)
        return greenery_available

    def total_shop_income(self):
        """returns the total income of the shop in a month"""
        total_fern_tastic_sp = self.fern_tastic_demand * fern_tastic.price  # total Selling price of Fern-Tastic.
        total_be_leaf_sp = self.be_leaf_demand * be_leaf_in_yourself.price  # total selling price of Be Leaf...
        total_you_rose_sp = self.you_rose_demand * you_rose_to_the_occasion.price  # total selling price of You Rose...
        total = total_be_leaf_sp + total_fern_tastic_sp + total_you_rose_sp  # adding all the selling prices.
        return total

    def total_employee_cost_per_month(self):
        """returns total expenditure on the salary of the florists in a month"""

        # Formula to calculate total employee cost: Total florists * total number of hours worked * per hour rate
        return Florists.FLORISTS_COUNT * FlowerShop.FLORIST_PER_MONTH_WORKING_HOURS * FlowerShop.FLORIST_PER_HOUR_RATE

    def total_green_house_cost(self):
        """returns the total expenditure on storing the flowers in the greenhouse"""

        # added the total cost of storing all types of flower bunches in the greenhouse.
        total = (self.daisies_quantity_before_dep() *
                 daisies.greenhouse_per_bunch_cost + self.rose_quantity_before_dep() *
                 rose.greenhouse_per_bunch_cost + self.greenery_quantity_before_dep() *
                 greenery.greenhouse_per_bunch_cost)
        return total

    def flower_restock_cost(self, vendor_details):
        """returns the total expenditure on restocking cost"""

        # calculating the re stock quantity after deducting sold flowers from the greenhouse capacity.
        rose_restock_quantity = rose.greenhouse_capacity - self.rose_quantity()
        daisies_restock_quantity = daisies.greenhouse_capacity - self.daisies_quantity()
        greenery_restock_quantity = greenery.greenhouse_capacity - self.greenery_quantity()

        # mapping the vendor chosen for the particular flower type. Vendor details is a dictionary which contains
        # vendor types and their rates of flower bunches.
        rose_vendor = vendor_details.get("rose")
        daisies_vendor = vendor_details.get("daisies")
        greenery_vendor = vendor_details.get("greenery")

        # calculating restock cost of each type of flower bunches.
        rose_restock_cost = rose_vendor.rose_bunch_rate * rose_restock_quantity
        daisies_restock_cost = daisies_vendor.daisies_bunch_rate * daisies_restock_quantity
        greenery_restock_cost = greenery_vendor.greenery_bunch_rate * greenery_restock_quantity
        total = rose_restock_cost + daisies_restock_cost + greenery_restock_cost  # adding all the cost
        return total

    def end_of_month_cash_balance(self, vendor_details):
        """calculates and returns the end month balance of the flower shop"""
        income = self.total_shop_income()  # total income of the shop

        # Calculated total expenditure of the flower shop.
        # Formula: greenhouse cost + restocking cost + rent + salary
        outgoings = (self.total_green_house_cost() +
                     self.flower_restock_cost(vendor_details) +
                     FlowerShop.RENT + self.total_employee_cost_per_month())

        # deducted the outgoings from the total budget of the flower shop.
        FlowerShop.TOTAL_BUDGET = FlowerShop.TOTAL_BUDGET - outgoings + income
        return FlowerShop.TOTAL_BUDGET
