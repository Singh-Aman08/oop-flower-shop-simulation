# Name: Aman Kumar Singh
# Section: Msc Data Science
# This code file creates a Florist Class which contains all the florist related information.


class Florists:
    """ Represents a florist.
        Attributes:
            class attributes:
                FLORISTS_COUNT (int): Counts the number of florists.
                FLORISTS_NAME (list): A list which stores florist's name.
                SPECIALIST_DETAILS (dict): A dictionary which contains specialist florist details.
                SPEC_DICT (dict): for specialized florists
            object attributes:
                name_of_florist (str): the florist's name.

        Methods:
            total_florists_count: A class method which returns the total number of
            florist.
            florists_name: A class method which returns the list of florists name.
    """
    FLORISTS_COUNT = 0
    FLORISTS_NAME = []
    SPEC_DICT= {}
    # Dictionary: SPECIALIST_DETAILS = { Bouquet type : ( monthly bouquet capacity, time to create one bouquet)}
    SPECIALIST_DETAILS = {"Fern-Tastic": (480, 10), "Be-Leaf in Yourself": (320, 15),
                          "You Rose to the Occasion": (214, 22.5)}

    def __init__(self, florist_name):
        """ Constructor which initializes the florist name.
        """
        # Handles errors for the florist name.
        if not florist_name.isalpha(): # handles errors in names.
            raise ValueError("Florist name must contain only letters.")
        if florist_name in Florists.FLORISTS_NAME: # raises an error if the name of a florist already exist.
            raise ValueError("Florist name already exist")

        self.name_of_florist = florist_name  #florist_name

        # It increments the FLORISTS_COUNT by 1 each time a new florist is hired.
        Florists.FLORISTS_COUNT += 1

        # It appends the list "FLORISTS_NAME" each time a new florist is hired.
        Florists.FLORISTS_NAME.append(self.name_of_florist)

    @classmethod #  a class decorator
    def total_florists_count(cls):
        """
        A class method which returns the total number of florists at any moment.
        """
        return cls.FLORISTS_COUNT

    @classmethod
    def florists_name(cls):
        """
        A class method which returns the list of names of florists at any moment.
        """
        return cls.FLORISTS_NAME