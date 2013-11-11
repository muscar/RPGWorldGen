"""
Fundamentals for creation of Dungeons and Dragons v3.5 characters
"""


from lib import dice

ability_scores = ["Strength", "Dexterity", "Consitution", 
                  "Intelligence", "Wisdom", "Charisma"]

phb_races = ["Human", "Dwarf", "Elf", "Half-Elf", "Half-Orc",
             "Halfling", "Gnome"]

def roll_stat():
    """
    Assumes D&D v3.5 PHB1 default rules:
    Roll 4d6, drop lowest roll, sum the
    rest of the dice for ability score
    """

    return sum(dice.discard(dice.roll("4d6", sorted=True), 1))

def roll_ability_scores():
    """
    Rreturns a dictionary mapping ability scores to
    values drawn from roll_stat() 
    """

    return dict((score, roll_stat()) for score in ability_scores)
