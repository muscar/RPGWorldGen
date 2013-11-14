# -*- coding: utf-8 -*-

"""
Fundamentals for creation of Dungeons and Dragons v3.5 characters
"""


from lib import dice
from lib.stat_gen import StatGenBase


phb_races = ["Human", "Dwarf", "Elf", "Half-Elf", "Half-Orc",
             "Halfling", "Gnome"]


class StatGen(StatGenBase):
    """DnD 3.5 stat generator"""
    
    ABILITY_SCORES = ["Strength", "Dexterity", "Consitution", 
                      "Intelligence", "Wisdom", "Charisma"]

    def __init__(self):
        super(StatGen, self).__init__()

    def _roll_stat(self):
        """
        Assumes D&D v3.5 PHB1 default rules:
        Roll 4d6, drop lowest roll, sum the
        rest of the dice for ability score
        """

        return sum(dice.discard(dice.roll("4d6", sorted=True), 1))
    
