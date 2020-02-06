############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, name, first_harvest, color, is_seedless,
                 is_bestseller):
        """Initialize a melon."""

        self.pairings = []

        self.code = code
        self.name = name
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []
    musk = MelonType("musk", "Muskmelon", 1998, "green", True, True)
    musk.add_pairing('mint')
    all_melon_types.append(musk)

    cas = MelonType("cas", "Casaba", 2003, "orange", False, False)
    cas.add_pairing('strawberries')
    cas.add_pairing('mint')
    all_melon_types.append(cas)

    cren = MelonType("cren", "Crenshaw", 1996, "green", False, False)
    cren.add_pairing('proscuitto')
    all_melon_types.append(cren)

    yw = MelonType("yw", "Yellow Watermelon", 2013, "yellow", False, True)
    yw.add_pairing('ice cream')
    all_melon_types.append(yw)

    print(all_melon_types)

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    for melon in melon_types:
        print(f"{melon.name} pairs with - {melon.pairings}")


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_reporting_code = {}

    for melon in melon_types:
        melon_reporting_code[melon.code] = melon.name

    return melon_reporting_code

############
# Part 2   #
############
class Melon(object):
    """A melon in a melon harvest."""
    # Needs __init__ and is_sellable methods
    def __init__(self, melon_type, shape_rating, color_rating,
                 harvested_from_field, harvested_by):
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvested_from_field = harvested_from_field
        self.harvested_by = harvested_by

    def is_sellable(shape_rating, color_rating, harvested_from_field):

        if shape_rating > 5 and color_rating > 5:
            if harvested_from_field != 3:
                return True

        return False


def make_melons(melon_types):
    """Returns a list of Melon objects."""
    list_of_melon_objects = []

    melon_1 = Melon("yw", 8, 7, 2, "Sheila")
    melon_2 = Melon("yw", 3, 4, 2, "Sheila")
    melon_3 = Melon("yw", 9, 8, 3, "Sheila")
    melon_4 = Melon("cas", 10, 6, 35, "Sheila")
    melon_5 = Melon("cren", 8, 9, 35, "Michael")
    melon_6 = Melon("cren", 8, 2, 35, "Michael")
    melon_7 = Melon("cren", 2, 3, 4, "Michael")
    melon_8 = Melon("musk", 6, 7, 4, "Michael")
    melon_9 = Melon("yw", 7, 10, 3, "Sheila")

    # for i in range(1, 10):
    #     list_of_melon_objects.append(melon_i)
    list_of_melon_objects.append(melon_1)
    list_of_melon_objects.append(melon_2)
    list_of_melon_objects.append(melon_3)
    list_of_melon_objects.append(melon_4)
    list_of_melon_objects.append(melon_5)
    list_of_melon_objects.append(melon_6)
    list_of_melon_objects.append(melon_7)
    list_of_melon_objects.append(melon_8)
    list_of_melon_objects.append(melon_9)

    return list_of_melon_objects


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""
    for melon in melons:
        if is_sellable(melon):
            print(print(f"Harvested by {melon.harvested_by} from Field {melon.harvested_from_field}. (CAN BE SOLD")
        else:
            print(f"Harvested by {melon.harvested_by} from Field, {melon.harvested_from_field}. (NOT SELLABLE)")