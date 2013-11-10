"""
Fundamentals for creation of Dungeons and Dragons v3.5 characters
"""


from random import *

ability_scores = ["Strength", "Dexterity", "Consitution", 
					"Intelligence", "Wisdom", "Charisma"]

phb_races = ["Human", "Dwarf", "Elf", "Half-Elf", "Half-Orc",
				"Halfling", "Gnome"]

def roll_d6():
	"""
	Returns a random integer on [1, 6]
	"""
	return randrange(1, 7)

def roll_stat():
	"""
	Assume D&D v3.5 PHB1 default rules:
	Roll 4d6, drop lowest roll, sum the
	rest of the dice for ability score
	"""
	dice_rolls = []

	for i in range(4):
		dice_rolls.append(roll_d6())

	dice_rolls.sort()
	dice_rolls.pop(0)

	return sum(dice_rolls)

def roll_ability_scores():
	"""
	Rreturns a dictionary mapping ability scores to
	values drawn from roll_stat() 
	"""
	scores = {}

	for score in ability_scores:
		scores[score] = roll_stat()

	return scores