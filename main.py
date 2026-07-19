from flower_shop import *
from florist import *
from bouquet import *
from flower import *
from vendor import *
# Name: Aman Kumar Singh
# Section: Msc Data Science
# This is the main file which contains all the important function required to run the simulation.


#------------------------------------------------------------------------------------------------------------#
def florist_hiring_func():
    """operates the hiring of the florist in the flower shop. It takes user inputs and handles
    errors"""
    while True:
        try:
            # asking the owner about how many florist should be hired and breaking the loop if hiring is within
            #the limit.
            florist_hiring = int(input(f"\tHow many florists would you like to hire? :"))
            if florist_hiring in [1, 2, 3, 4] and (florist_hiring + Florists.FLORISTS_COUNT) <= 4:
                break
            # handling error if the hiring exceeds the concept of at least one florist and at most 4 florist.
            elif florist_hiring not in [1, 2, 3, 4]:
                raise Exception("Please enter a numeric value from 1 to 4 for the number of florists.")

            elif (florist_hiring + Florists.FLORISTS_COUNT) > 4:   #handling error
                raise Exception("The total number of florists must not exceed 4.")

        except Exception as t:
            print(t)
    # the loop is asking the name and speciality of the florists proposed to be hired.

    for i in range(florist_hiring):
        while True:
            try:
                florist_details = input("Please input florist name (one at a time) :")  #takes the name of the florist
                Florists(florist_details)  # object creation of Florists class
                break
            except ValueError as t:
                print(t)
        while True:
            try:
                flo_spec = int(input("Does the florist have any speciality? Click 0 for yes else click 1"))
                if flo_spec==0:
                    while True:
                        try:
                            # asking the user about the speciality of the florist and stores this
                            # information in the dictionary, speciality.
                            speciality=int(input("Click 1 for Fern-Tastic, 2 for Be-Leaf in Yourself, 3 for You Rose to the Occasion"))
                            if speciality==1:
                                Florists.SPEC_DICT["Fern-Tastic"]=florist_details
                                break
                            elif speciality==2:
                                Florists.SPEC_DICT["Be-Leaf in Yourself"]=florist_details
                                break
                            elif speciality==3:
                                Florists.SPEC_DICT["You Rose to the Occasion"]=florist_details
                                break
                            else:
                                raise Exception("Only valid inputs is 0 or 1")
                        except Exception as  t:
                            print(t)

                    break
                elif flo_spec==1:
                    break
                else:
                    raise Exception("Only 0 or 1 is valid input")
            except Exception as t:
                print(t)


#-------------------------------------------------------------------------------------------------------------#

def florist_firing_func():
    """operates the firing of the florist in the flower shop. It takes user inputs and handles
    errors"""
    print(f"The list of current staff: {Florists.FLORISTS_NAME}") # florist name from the Florist class.
    while True:
        # asking the owner about the number of florist to be fired.
        try:
            florist_firing = int(input(f"\tHow many florists would you like to fire? :"))
            # handling error if the florist firing exceeds the total florist in the shop.
            if 0 < florist_firing < Florists.FLORISTS_COUNT:
                break
            else:
                raise Exception
        except Exception:
            print("Firing cannot be initiated. Please enter a valid number.")
    # asking the name of the florist to be hired and raising error if the valid name not given.
    for i in range(florist_firing):
        while True:
            flor_name = input("Enter the name of the florist you want to remove")
            if flor_name in Florists.FLORISTS_NAME:
                Florists.FLORISTS_NAME.remove(flor_name)  # removing the name of the florist from the class attribute.
                Florists.FLORISTS_COUNT -= 1 # decreasing the florist count by one.
                for k in list(Florists.SPEC_DICT.keys()):
                    if Florists.SPEC_DICT[k]==flor_name:
                        del Florists.SPEC_DICT[k]
                        break
                break
            else:
                print("Name not found. Please enter the name again.")
#-------------------------------------------------------------------------------------------------------------#

def bouquet_order():
    """takes the bouquet order and raise error if order exceeds the demand and
    returns a tuple of quantities of the ordered bouquets."""
    # taking order for Fern-Tastic
    while True:
        try:
            fern = int(input("Fern-tastic:"))
            if 0 <= fern <= 175:
                break
            else:
                # raising error if the demand for the given bouquet type exceeds.
                raise ValueError("This does not fit within the demand for Fern-tastic.")
        except ValueError as t:
            print(t)

    # taking order for Be Leaf...
    while True:
        try:
            be_leaf = int(input("Be-Leaf in Yourself:"))
            if 0 <= be_leaf <= 100:
                break
            else:
                # raising error if the demand for the given bouquet type exceeds.
                raise ValueError("This does not fit within the demand for Be-Leaf in Yourself.")
        except ValueError as t:
            print(t)

    # taking order for You Rose...
    while True:
        try:
            you_rose = int(input("You Rose to the Occasion:"))
            if 0 <= you_rose <= 250:
                break
            else:
                # raising error if the demand for the given bouquet type exceeds.
                raise ValueError("This does not fit within the demand for You Rose to the Occasion")
        except ValueError as t:
            print(t)
    return fern, be_leaf, you_rose   # returns a tuple of quantities of the ordered bouquets.
#-------------------------------------------------------------------------------------------------------------#


def total_time_req_for_fern(fern_demand, dict1):
    """calculates and returns the total time required for preparing the order for Fern-Tastic
    Parameters:
        fern_demand: total order placed
        dict1: Dictionary of specialist florist which contains name and specialization"""

    # If there is a specialist for Fern-tastic
    if "Fern-Tastic" in dict1:

        special_cap = Florists.SPECIALIST_DETAILS["Fern-Tastic"][0]
        special_time = Florists.SPECIALIST_DETAILS["Fern-Tastic"][1]  # half-time
        normal_time = fern_tastic.time_to_prepare_bouquet()  # full-time

        # if the specialist florist is not able to complete the order, then the normal
        # florist completes the order.
        if fern_demand > special_cap:

            extra_demand = fern_demand - special_cap

            total_time = ((special_cap * special_time) + (extra_demand * normal_time))

        else:
            # specialist can finish it fully
            total_time = fern_demand * special_time

    else:
        # if there is no specialist
        total_time = fern_demand * fern_tastic.time_to_prepare_bouquet()

    return total_time


def total_time_req_for_be_leaf(be_leaf_demand, dict1):
    """calculates and returns the total time required for preparing the order for Be Leaf...
    Parameters:
        be_leaf_demand: total order placed
        dict1: Dictionary of specialist florist which contains name and specialization"""

    # If there is a specialist for Be Leaf...
    if "Be-Leaf in Yourself" in dict1:

        special_cap = Florists.SPECIALIST_DETAILS["Be-Leaf in Yourself"][0]
        special_time = Florists.SPECIALIST_DETAILS["Be-Leaf in Yourself"][1]  # half-time
        normal_time = be_leaf_in_yourself.time_to_prepare_bouquet()  # full-time

        # if the specialist florist is not able to complete the order, then the normal
        # florist completes the order.
        if be_leaf_demand > special_cap:

            extra_demand = be_leaf_demand - special_cap

            total_time = ((special_cap * special_time) + (extra_demand * normal_time))

        else:
            # specialist can finish it fully
            total_time = be_leaf_demand * special_time

    else:
        # if there is no specialist
        total_time = be_leaf_demand * be_leaf_in_yourself.time_to_prepare_bouquet()

    return total_time


def total_time_req_you_rose(you_rose_demand,dict1):
    """calculates and returns the total time required for preparing the order for You Rose...
    Parameters:
        you_rose_demand: total order placed
        dict1: Dictionary of specialist florist which contains name and specialization"""

    # If there is a specialist for You Rose...
    if "You Rose to the Occasion" in dict1:

        special_cap = Florists.SPECIALIST_DETAILS["You Rose to the Occasion"][0]
        special_time = Florists.SPECIALIST_DETAILS["You Rose to the Occasion"][1]  # half-time
        normal_time = you_rose_to_the_occasion.time_to_prepare_bouquet()  # full-time

        # if the specialist florist is not able to complete the order, then the normal
        # florist completes the order.
        if you_rose_demand > special_cap:

            extra_demand = you_rose_demand - special_cap

            total_time = ((special_cap * special_time) + (extra_demand * normal_time))

        else:
            # specialist can finish it fully
            total_time = you_rose_demand * special_time

    else:
        # if there is no specialist
        total_time = you_rose_demand * you_rose_to_the_occasion.time_to_prepare_bouquet()

    return total_time
#-------------------------------------------------------------------------------------------------------------#

def total_employee_time():
    """calculates and returns total employee time"""
    total_time = Florists.FLORISTS_COUNT * 80 * 60  # 80 hours per month
    return total_time  # gives time in minutes
#-------------------------------------------------------------------------------------------------------------#

def vendor_booking_details():
    """it takes the input from the owner about vendor selection for each type of flower bunches and also
    handles the error and returns a dictionary called vendor details which store vendor
    and flower type"""
    vendor_details = {}  # dictionary which stores vendor and flower type

    for i in ["rose", "daisies", "greenery"]:
        while True:
            try:
                # gives choices of different vendors to the shop owner.
                print(f"Do you want to purchase {i} from Evergreen Essentials (0), or FloraGrow"
                      "Distributors (1)? ")
                print("Press (i) if you would like to see price information from either supplier.")
                owner_input = input()
                if owner_input == "i":
                    print(Vendor.vendor_catalogue())
                    continue
                elif owner_input == "0":
                    vendor_details[i] = evergreen_essentials
                    break
                elif owner_input == "1":
                    vendor_details[i] = flora_grow_distributors
                    break
                else:
                    raise ValueError("Input should only be either 'i', '0', or '1'.")

            except ValueError as t:  # handles the error
                print(t)
    return vendor_details
# -------------------------------------------------------------------------------------------------------------------#

def simulator():
    """this is the function which simulates the whole operation of the flower shop. It uses the different
    functions  prepared in the beginning and returns end balance"""
    print("Before the months starts, there are some owner actions for "
          "you to carry out. First, review the number of staff, then decide how many "
          "bouquets to sell.")
    print(f"Current number of florists: {Florists.FLORISTS_COUNT}")

    # gives only option of hiring and not firing the florist because of florist count constraints.
    if Florists.FLORISTS_COUNT == 0 or Florists.FLORISTS_COUNT == 1:
         florist_hiring_func()   # calling the florist_hiring function

    # if there are appropriate number of florists, now allows firing along with hiring.
    else:
        while True:
            try:
                # give options whether to hire or fire the florist.
                opt1 = input("Enter 1 to hire a florist or 2 to fire a florist.")
                if opt1 in ["1", "2"]:
                    break
                else:
                    raise ValueError("Please enter a valid number.")
            except ValueError as t:
                print(t)
        # if option "1", then florist_hiring function is called.
        if opt1 == "1":
            florist_hiring_func()
        # if option "2", then florist firing function is called.
        elif opt1 == "2":
            florist_firing_func()

    print(f"Current staff:\n\t{Florists.FLORISTS_NAME}\n") # gives the list of current florist's name.

    print("How much of each bouquet would you like to sell?\n")

    while True:
        # takes the bouquet orders and return the quantity.
        fern, be_leaf, you_rose = bouquet_order()
        # calculates the total time required to prepare the ordered bouquet.
        total_time_req_to_prepare_bouquet = (total_time_req_for_fern(fern, Florists.SPEC_DICT) + total_time_req_for_be_leaf(be_leaf, Florists.SPEC_DICT) +
                                             total_time_req_you_rose(you_rose, Florists.SPEC_DICT))
        # raise error if total time required to prepare the ordered bouquet exceeds the labour constraints.
        if total_time_req_to_prepare_bouquet > total_employee_time():
            print("The demand exceeds the labour constraint")
            continue
        # calculates the quantity of total rose, daisies, greenery in the bouquets.
        total_rose = (fern * fern_tastic.roses + be_leaf * be_leaf_in_yourself.roses + you_rose *
                      you_rose_to_the_occasion.roses)
        total_daisies = (fern * fern_tastic.daisies + be_leaf * be_leaf_in_yourself.daisies +
                         you_rose * you_rose_to_the_occasion.daisies)
        total_greenery = (fern * fern_tastic.greenery + be_leaf * be_leaf_in_yourself.greenery +
                          you_rose * you_rose_to_the_occasion.greenery)

        # raises error if the order exceeds the supply.
        if (total_rose > rose.greenhouse_capacity or
                total_daisies > daisies.greenhouse_capacity or
                total_greenery > greenery.greenhouse_capacity):
            print("The demand exceeds the supply")
            continue

        break

    print()
    # it retrieves the information from the flower shop and other modules and gives to the owner.
    flower_shop=FlowerShop(fern, be_leaf, you_rose)  # gives the quantity of ordered flowers
    print("-------------------------------------------------------")
    print("Month in progress....")
    print("-------------------------------------------------------\n")
    print("End of month calculations:\n")
    print(f"Cash Balance, Month start: £{FlowerShop.TOTAL_BUDGET}")  # total budget of the shop
    print(f"\tIncome: £{flower_shop.total_shop_income()} ")  # total income of the shop
    print(f"\tOutgoings:")
    print(f"\t\tEmployee_cost: £{flower_shop.total_employee_cost_per_month()}")  # total salaries
    print(f"\t\tGreenhouse_cost: £{flower_shop.total_green_house_cost()}")  # total greenhouse cost
    print(f"\t\tRent: £{flower_shop.RENT}\n")  # flower shop rent
    print(f"Current Shop Status:")
    print(f"\tCurrent staff: {Florists.FLORISTS_NAME}\n\t")  # list of florist's name
    print(f"\tGreenhouse quantity:")
    print(f"\t\tRoses: {flower_shop.rose_quantity()}")  # flower quantity
    print(f"\t\tDaisy: {flower_shop.daisies_quantity()}")
    print(f"\t\tGreenery: {flower_shop.greenery_quantity()}")
    print(f"The greenhouse has spare capacity and needs to be restocked....\n")

    vendor_details = vendor_booking_details() # calls the function to place orders to the vendors
    end_balance = flower_shop.end_of_month_cash_balance(vendor_details) # gives end of the month balance
    print(f"\tFlower restock costs: £{flower_shop.flower_restock_cost(vendor_details)}")  # restock cost
    print(f"\tEnd of month Cash Balance: £{end_balance}")  # gives end of the month cash balance
    return end_balance
# -----------------------------------------------------------------------------------------------------------------#


def number_of_months(months=6):
    """runs the simulations for the given number of months"""
    for i in range(months):
        print(f"Month: {i + 1}")
        cash_balance = simulator() # calling simulator function
        if cash_balance < 0:
            print("The flower shop is now bankrupt, and the simulation ends.")
            break
    else:
        print("**********************************************************************")
        print("Congratulations! You have completed the simulation! ")
#-------------------------------------SIMULATION BEGINS-----------------------------------------------------------#
# from here the simulation begins.
print("-------------------------------------------------------")
print("Welcome to the FlowerShop Simulator!")
print("-------------------------------------------------------")
while True:
    try:
        total_months = int(input("How many months would you like to run the game? Enter 0 to use the default (six months)"))
        if total_months == 0:
            number_of_months()  # the default is six months
            break
        if 0 < total_months:
            break
        else:
            raise Exception
    except Exception:
        print("Enter the month as a natural number.")
number_of_months(total_months)
# ------------------------------------SIMULATION ENDS--------------------------------------------------------------#

