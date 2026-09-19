# Flower Shop Simulation

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

This project is separated into several Python files, with each file representing a component of the flower shop. Using multiple Python files as modules helps maintain the code and improves its organisation and readability.

### Following Python files are created for this project.

1. ### `bouquet.py`

   - This file contains the `Bouquet` class, which represents a specific type of bouquet sold in the shop. Each bouquet object contains the quantities of flowers required (roses, daisies, greenery), the price of the bouquet, and the time required to prepare it.
   - The class contains two key methods:
     - `bouquet_price()` – Returns the price of the bouquet.
     - `time_to_prepare_bouquet()` – Returns the time required to prepare the bouquet.
   - The purpose of this class is to allow easy addition of new bouquet types without modifying other parts of the program.

2. ### `florist.py`

   - This file defines the `Florist` class, which manages the florists working in the shop.
   - It contains class attributes such as:
     - `FLORISTS_COUNT` – Stores the total number of florists working in the shop.
     - `FLORISTS_NAME` – Stores the names of the florists working in the shop.
   - The object attribute `name_of_florist` stores the name of an individual florist entered by the shop owner.
   - Two class methods are provided:
     - `total_florists_count()` – Provides information about the total number of florists.
     - `florists_name()` – Provides the names of the florists.
   - This class helps track the florists in the shop and provides flexibility to add or remove staff.

3. ### `flower.py`

   - This file contains the `Flower` class, which represents different flower types in the greenhouse.
   - Each object stores the flower name, greenhouse capacity, depreciation rate, and cost per bunch.
   - This class helps track supplies of different flower types, such as roses, daisies, and greenery.
   - It also provides flexibility for future extensions, such as adding new flower types without major changes to the rest of the program.
   - The class provides access to flower-level details such as cost, depreciation, and greenhouse-related costs.

4. ### `vendor.py`

   - This file contains the `Vendor` class, which represents suppliers providing flowers to the shop.
   - Each object stores the vendor name and per-bunch pricing for different flower types, including roses, daisies, and greenery.
   - It also contains the class method `vendor_catalogue()`, which returns a dictionary containing the available vendors and their pricing.
   - This class allows the shop to efficiently query vendor rates for different flower types.

5. ### `flower_shop.py`

   - This file contains the `FlowerShop` class. It integrates florists, bouquets, flowers, and vendors to handle the main operations of the flower shop.
   - Its responsibilities include managing staff, handling inventory, calculating outgoings, and processing bouquet sales.
   - This class acts as the backbone of the simulation.

   #### Class Attributes

   - `FLORIST_PER_MONTH_WORKING_HOURS` – Defines the monthly working limit of a florist.
   - `FLORIST_PER_HOUR_RATE` – Defines the hourly rate of a florist.
   - `TOTAL_BUDGET` – Defines the budget of the flower shop.
   - `RENT` – Defines the monthly rent of the flower shop.

   #### Object Attributes

   - `fern_tastic_demand` – Number of orders for Fern-Tastic.
   - `be_leaf_demand` – Number of orders for Be Leaf in Yourself.
   - `you_rose_demand` – Number of orders for You Rose to the Occasion.

   #### Class Methods

   - `florist_count()` – Returns the number of florists in the flower shop.
   - `florist_name()` – Returns the names of the florists in the flower shop.

   #### Object Methods

   - `rose_quantity_before_dep()` – Returns the number of roses before depreciation.
   - `daisies_quantity_before_dep()` – Returns the number of daisies before depreciation.
   - `greenery_quantity_before_dep()` – Returns the number of greenery before depreciation.
   - `rose_quantity()` – Returns the number of roses after depreciation.
   - `daisies_quantity()` – Returns the number of daisies after depreciation.
   - `greenery_quantity()` – Returns the number of greenery after depreciation.
   - `total_shop_income()` – Returns the total income of the shop.
   - `total_employee_cost_per_month()` – Returns the total monthly salary cost of the florists.
   - `total_green_house_cost()` – Returns the total monthly greenhouse expenditure.
   - `flower_restock_cost()` – Returns the expenditure on restocking flowers.
   - `end_of_month_cash_balance()` – Returns the month-end cash balance of the flower shop.

6. ### `main.py`

   - The orchestration of the entire simulation is handled in this `main.py` file.
   - It imports the required classes and handles user input, including the number of months to simulate, florists to add or remove, vendor selection, and the number of bouquets to sell.
   - Separating the simulation logic into `main.py` keeps it separate from the class definitions, improving readability and allowing the classes to be reused in other parts of the project.

   #### Functions Used in `main.py`

   - `florist_hiring_func()` – Handles the hiring of florists in the flower shop. It takes user input and handles errors, including the hiring of a specialist florist.
   - `florist_firing_func()` – Handles the removal of florists from the flower shop. It takes user input and handles errors.
   - `bouquet_order()` – Takes bouquet orders and raises errors if an order exceeds demand, supply, or labour constraints.
   - `total_time_req_for_fern()` – Calculates the total time required to prepare the Fern-Tastic order.
   - `total_time_req_for_be_leaf()` – Calculates the total time required to prepare the Be Leaf in Yourself order.
   - `total_time_req_you_rose()` – Calculates the total time required to prepare the You Rose to the Occasion order.
   - `total_employee_time()` – Calculates the total employee working time.
   - `vendor_booking_details()` – Takes input from the owner regarding vendor selection for each type of flower bunch and handles errors.
   - `simulator()` – Simulates the complete operation of the flower shop using the functions defined above.
   - `number_of_months()` – Runs the simulation for the specified number of months.

## Requirements

- Python must be installed.
- No external libraries are required; only Python standard libraries are used.

## Usage

- Enter the number of months to simulate. The default is 6 months.
- At the start of each month, choose how many florists to add or remove. Enter the name and specialisation of the florist, if applicable.
- Enter the number of bouquets to sell for each type, ensuring that supply, labour, and demand constraints are met.
- The program calculates salaries, greenhouse costs, income, remaining flowers in the greenhouse, and other financial information.
- Choose the vendor from whom you want to restock your flowers.
- The simulation calculates the restocking cost and provides the remaining shop balance at the end of each month.
- The simulation ends after the specified number of months or if the shop becomes financially unsustainable.

## Example Run

```text
-------------------------------------------------------
Welcome to the FlowerShop Simulator!
-------------------------------------------------------
How many months would you like to run the game? Enter 0 to use the default (six months)
Enter the month as a natural number.
How many months would you like to run the game? Enter 0 to use the default (six months)
2
Month: 1
Before the month starts, there are some owner actions for you to carry out. First, review the number of staff, then decide how many bouquets to sell.
Current number of florists: 0
    How many florists would you like to hire? :2
Please input florist name (one at a time) :Aman
Does the florist have any speciality? Click 0 for yes else click 1
Click 1 for Fern-Tastic, 2 for Be-Leaf in Yourself, 3 for You Rose to the Occasion
Please input florist name (one at a time) :Singh
Does the florist have any speciality? Click 0 for yes else click 1
Current staff:
    ['Aman', 'Singh']

How much of each bouquet would you like to sell?

Fern-Tastic:40
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
Before the month starts, there are some owner actions for you to carry out. First, review the number of staff, then decide how many bouquets to sell.
Current number of florists: 2
Enter 1 to hire a florist or 2 to fire a florist.
2
The list of current staff: ['Aman', 'Singh']
    How many florists would you like to fire? :Singh
Firing cannot be initiated. Please enter a valid number.
    How many florists would you like to fire? :1
Enter the name of the florist you want to remove
Singh
Current staff:
    ['Aman']

How much of each bouquet would you like to sell?

Fern-Tastic:40
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
## Author

**Aman Kumar Singh**  
MSc Data Science  
University of Bristol













