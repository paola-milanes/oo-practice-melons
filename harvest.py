############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, name, code, first_harvest, color, is_seedless, is_bestseller, 
    ):
        """Initialize a melon."""
        self.name = name
        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = True
        self.is_bestseller = is_bestseller
        



        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings = self.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        
        self.code = new_code

def make_melon_types():
    """Returns a list of current melon types."""
    
    all_melon_types = []
    musk = MelonType(
    "musk",
    "Muskmelon",
    1998,
    "green",
    True,
    True
)
    musk.add_pairing("mint")
    all_melon_types.append("musk")

    casaba = MelonType(
        "cas",
        "2003",
        "orage",
        "false"
        "false"
        )
    casaba.add_pairing("mint, Strawberry")
    all_melon_types.append("casaba")

    crenshaw = MelonType(
        "cren",
        "1997",
        "green",
        "False",
        "False"
        )

    crenshaw.add_pairing("prosciutto")
    all_melon_types.append("crenshaw")

    yellow_watermelon = MelonType(
        "yw",
        "2013",
        "yellow",
        "False",
        "False"
        )
    yellow_watermelon.add_pairing("ice cream")
    all_melon_types.append("yellow_watermelon")

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    for melon in melon_types:
        print(f"{melon.name}")
        for pair in melon.pairings:
            print(f"pairs with {melon.pairing}")
      # Fill in the rest


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    dictonary = {}
    for melon in melon_types:
        if melon.code not in dictonary:
            dictonary[melon]= melon


    # Fill in the rest


############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""
    def __init__(self, type, shape, color, harvest, harvest_by):
        self.type = type
        self.shape = shape
        self.color = color
        self.harvest = harvest
        self.harvest_by = harvest_by
        
    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def is_sellable(self):
        return self.shape and self.color > 5 and self.hardvest != 3
           

def make_melons(melon_types):
    """Returns a list of Melon objects."""
    melon_objects = []
    melons_by_id = make_melon_type_lookup(melon_types)
    melon_1 = Melon(melons_by_id["yw"],8, 7, 2, "sheila")
    melon_2 = Melon(melons_by_id["yw"], 3, 4, 2, "sheila")
    melon_3 = Melon(melons_by_id["yw"], 9, 8, 3, "shela")
    melon_4 = Melon(melons_by_id["cas"], 10, 6, 35, "shela")
    melon_5 = Melon(melons_by_id["cren"], 8, 9, 35, "Michael")
    melon_6 = Melon(melons_by_id["cre"], 8,2,35, "Michael")
    melon_7 = Melon(melons_by_id["cre"], 2,3,4, "Michael")
    melon_8 = Melon(melons_by_id["musk"], 6,7,4, "Michael")
    melon_9 = Melon(melons_by_id["yw"], 7,10,3, "Sheila")

    melon_objects.extend(melon_1,melon_2,melon_3,melon_4,melon_5,melon_6,melon_7,melon_8,melon_9)
    return melon_objects
    
    # Fill in the rest


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""
    for melon in melons:
        if melon.is_sellable():
            print(f"{melon.type} is sellable")

    # Fill in the rest
