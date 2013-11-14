# -*- coding: utf-8 -*-

"""
Fundamentals for creation of Swords & Wizardry characters
"""


from lib import dice
from lib.stat_gen import StatGenBase


class StatGen(StatGenBase):
    """S&W stat generator"""
    
    ABILITY_SCORES = ["Strength", "Dexterity", "Consitution", 
                      "Intelligence", "Wisdom", "Charisma"]
    
    def __init__(self):
        super(StatGen, self).__init__()

    def _roll_stat(self):
        """
        The first step to creating your character is to roll 3d6 for each of the
        six attribute scores.
        """
        
        return sum(dice.roll("3d6", sorted=True))
