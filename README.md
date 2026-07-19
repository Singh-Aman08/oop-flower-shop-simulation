# Flower shop Simulation (Part 1)

## Overview

This project implements a **text-based Flower Shop Simulation System** using **Python and Object-Oriented Programming (OOP)** principles. The simulation models the day-to-day operations of a flower shop, including managing florists, creating bouquets, handling inventory, selecting vendors, processing sales, and tracking financial transactions.

The program simulates shop operations over multiple months, allowing the owner to make decisions related to staffing, production, sales, and resource management. The simulation continuously monitors income and expenses and terminates automatically when the shop becomes financially unsustainable.

## Objectives

The main objectives of this project were:

- Apply core **Object-Oriented Programming concepts** such as encapsulation, inheritance, abstraction, and modular design.
- Design a maintainable software structure by separating different components of the application into independent Python modules.
- Simulate real-world business operations including inventory management, employee management, sales processing, and financial tracking.
- Implement reusable classes for flowers, bouquets, vendors, florists, and shop operations.
- Develop a simulation system that demonstrates decision-making, resource management, and object interactions in a real-world scenario.

## Code Design and Structure
This project is separted into several Python files, each one of them represents a part of the flower shop. This design of creating multiple python files as modules helps in maintaing the code.
#### Following python files are created for this project.
1. #### bouquet.py
  - This file contains the Bouquet class `Bouquet` class, which represents a specific type of bouquet sold in the shop. Each bouquet object contains the quantities of flowers required (roses, daisies, greenery), the price of the bouquet, and the time required to prepare it. This class also has two key methods:`bouquet_price()` which returns the price of the bouquet, and another one is `time_to_prepare_bouquet()` to return the time required to prepare the bouquet. The motive to create this class was to allow easy addition of new bouquet types without modifying other parts of the program.
2. #### florist.py
- This file defines the `Florist` class, which handles the florists working in the shop. It contains class attributes like `FLORISTS_COUNT` for the total number of florists working the shop and `FLORISTS_NAME` which is the list of names of the florists working in the shop. There is an object attribute `name_of_florist` which takes the name of the florist which is entered by the shop owner. Two class methods `total_florists_count()` and `florists_name()` provides information about the total number of florist and their names. This class helps in tracking of all florists which provides flexibility to add or remove the florist.
3. #### flower.py
- This file contains `Flower` class which represents the inventory of different flower types in the greenhouse. Each object of this class stores the flower name, greenhouse capacity, depreciation rate, and the cost of a flower bunch. This class creation helps in tracking supplies of each flower types (rose, daisies, greenery). It also gives flexibility of having future extensions like adding new flower types without major changes. This class also helps in querrying flower level details like cost, depreciation, greenhouse cost etc.
4. #### vendor.py
- This file contains the `Vendor` class which represents the supplier providing flowers to the shop. The object stores the name of the vendor and per bunch pricing for all types of flowers (roses, daisies, greenery). It also contains a class method `vendor_catalogue()` which returns a dictionary of all vendors and their pricing. This class allows the shop to query vendor rates of different prices efficiently.
5. #### flower_shop.py
- This file contains the flowershop class. It integrates florists, bouquets, flowers, and vendors to handle shop operations. Its responsibilities include managing staff, handling inventory, calculating outgoings and process bouquet sales. This class acts as the backbone of the simulation.
 - Following are the attributes and the methods of the class.
  - Class attributes:
    - `FLORIST_PER_MONTH_WORKING_HOURS` = Gives the monthly working limit of a florist.
    - `FLORIST_PER_HOUR_RATE` = Gives the per hour rate of a florist.
    - `TOTAL_BUDGET` = Gives the budget of the flower shop.
    - `RENT` = Gives the monthly rent of the flower shop.

  - Object attributes:
    - `fern_tastic_demand`: Number of orders of Fern-Tastic.
    - `be_leaf_demand`: Number of orders of Be Leaf in Yourself.
    - `you_rose_demand`: Number of orders of You Rose to the Occasion.

  - Class Methods:
    - `florist_count()`: Number of florists in the flower shop.
    - `florist_name()`: Name of the florists in the flower shop.

  - Object Methods:
    - `rose_quantity_before_dep()`: gives number of roses before depreciation.
    - `daisies_quantity_before_dep()`: gives number of daisies before depreciation.
    - `greenery_quantity_before_dep()`: gives number of greenery before depreciation.
    - `rose_quantity()`: gives number of roses after depreciation.
    - `daisies_quantity()`: gives number of daisies after depreciation.
    - `greenery_quantity()`: gives number of greenery after depreciation.
    - `total_shop_income()`: gives total income of the shop.
    - `total_employee_cost_per_month()`: gives total salary of florist per month.
    - `total_green_house_cost()`: gives total expenditure on greenhouse per month.
    - `flower_restock_cost()`: gives expenditure on restocking flower.
    - `end_of_month_cash_balance()`: returns the month end balance of the flower shop.

6. #### main.py
 - The orchestration of entire simulation is done from this main.py file. It imports all the classes and handles user input, such as the number of month to simulate, florists to add or remove, vendor choice, and the number of bouquets to sell. Creating a main.py file helps separting if from class definitions which improves readbility and allows easy reuse of classes in other projects.
  - Following are the methods used in the main.py file.

   - `florist_hiring_func()`: Operates the hiring of the florist in the flower shop. It takes user inputs and handles errors. It also incorporates the hiring of a specialist florist.
   - `florist_firing_func()`: Operates the firing of the florist in the flower shop. It takes user inputs and handles errors.
   - `bouquet_order()`: Takes the bouquet order and raise error if order exceeds the demand, supplies and labour constraints.
   - `total_time_req_for_fern()`: Calculates the total time required for preparing the order for Fern-Tastic.
   - `total_time_req_for_be_leaf()`: Calculates the total time required for preparing the order for Be Leaf in Yourself.
   - `total_time_req_you_rose()`: Calculates the total time required for preparing the order for You Rose to the Occasion.
   - `total_employee_time()`: Calculates total employee time.
   - `vendor_booking_details()`: It takes the input from the owner about vendor selection for each type of flower bunches and also handles the error.
   - `simulator()`: This is the function which simulates the whole operation of the flower shop. It uses the different functions  prepared in the beginning.
   - `number_of_months()`: Runs the simulations for the given number of months.

## Requirements
- Python must be installed.
- No external libraries required, only python standard libraries are used.

## Usage
- Enter the number of months to simulate (default is 6).
- At the start of each month, choose how many florist to add or remove. Give the name and specialization of the florist if any.
- Enter the number of bouquets to sell for each type, ensuring supply, labor, and demand constraints are met.
- The program calculates the salaries, greenhouse cost, income, flowers left in the greenhouse etc.
- Choose the vendor you want to restock your flowers from.
- The simulation gives the restocking cost and at the end provides the money left in the shop. The simulation is end after the specified number of months or if the shop goes bankrupt.

## Example Run
```-------------------------------------------------------
Welcome to the FlowerShop Simulator!
-------------------------------------------------------
How many months would you like to run the game? Enter 0 to use the default (six months)-g
Enter the month as a natural number.
How many months would you like to run the game? Enter 0 to use the default (six months)-8
Enter the month as a natural number.
How many months would you like to run the game? Enter 0 to use the default (six months)2
Month: 1
Before the months starts, there are some owner actions for you to carry out. First, review the number of staff, then decide how many bouquets to sell.
Current number of florists: 0
	How many florists would you like to hire? :2
Please input florist name (one at a time) :Aman
Does the florist have any speciality? Click 0 for yes else click 10
Click 1 for Fern-Tastic, 2 for Be-Leaf in Yourself, 3 for You Rose to the Occasion1
Please input florist name (one at a time) :Singh
Does the florist have any speciality? Click 0 for yes else click 11
Current staff:
	['Aman', 'Singh']

How much of each bouquet would you like to sell?

Fern-tastic:40
Be-Leaf in Yourself:10
You Rose to the Occasion:10

-------------------------------------------------------
Month in progress....
-------------------------------------------------------

End of month calculations:

Cash Balance, Month start: £7500
	Income: £1242.5 
	Outgoings:
		Employee_cost: £2480.0
		Greenhouse_cost: £361.0
		Rent: £800

Current Shop Status:
	Current staff: ['Aman', 'Singh']
	
	Greenhouse quantity:
		Roses: 90
		Daisy: 102
		Greenery: 190
The greenhouse has spare capacity and needs to be restocked....

Do you want to purchase rose from Evergreen Essentials (0), or FloraGrowDistributors (1)? 
Press (i) if you would like to see price information from either supplier.
0
Do you want to purchase daisies from Evergreen Essentials (0), or FloraGrowDistributors (1)? 
Press (i) if you would like to see price information from either supplier.
0
Do you want to purchase greenery from Evergreen Essentials (0), or FloraGrowDistributors (1)? 
Press (i) if you would like to see price information from either supplier.
0
	Flower restock costs: £729.5
	End of month Cash Balance: £4372.0
Month: 2
Before the months starts, there are some owner actions for you to carry out. First, review the number of staff, then decide how many bouquets to sell.
Current number of florists: 2
Enter 1 to hire a florist or 2 to fire a florist.2
The list of current staff: ['Aman', 'Singh']
	How many florists would you like to fire? :Singh
Firing cannot be initiated. Please enter a valid number.
	How many florists would you like to fire? :1
Enter the name of the florist you want to removeSingh
Current staff:
	['Aman']

How much of each bouquet would you like to sell?

Fern-tastic:40
Be-Leaf in Yourself:20
You Rose to the Occasion:30

-------------------------------------------------------
Month in progress....
-------------------------------------------------------

End of month calculations:

Cash Balance, Month start: £4372.0
	Income: £2070.0 
	Outgoings:
		Employee_cost: £1240.0
		Greenhouse_cost: £158.0
		Rent: £800

Current Shop Status:
	Current staff: ['Aman']
	
	Greenhouse quantity:
		Roses: 36
		Daisy: 43
		Greenery: 133
The greenhouse has spare capacity and needs to be restocked....

Do you want to purchase rose from Evergreen Essentials (0), or FloraGrowDistributors (1)? 
Press (i) if you would like to see price information from either supplier.
0
Do you want to purchase daisies from Evergreen Essentials (0), or FloraGrowDistributors (1)? 
Press (i) if you would like to see price information from either supplier.
0
Do you want to purchase greenery from Evergreen Essentials (0), or FloraGrowDistributors (1)? 
Press (i) if you would like to see price information from either supplier.
0
	Flower restock costs: £1023.35
	End of month Cash Balance: £3220.65
**********************************************************************
Congratulations! You have completed the simulation! 
```

## Repository Structure

```text

├── bouquet.py          # Defines bouquet-related classes and operations
├── florist.py          # Handles florist-related functionality and management
├── flower.py           # Contains flower classes and attributes
├── flower_shop.py      # Implements core flower shop operations and management logic
├── main.py             # Entry point of the application
└── vendor.py           # Handles vendor-related classes and interactions
```



   













