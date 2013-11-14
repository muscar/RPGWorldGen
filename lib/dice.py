# -*- coding: utf-8 -*-

"""
Library for simulating dice throws.
"""

import random

def roll_die(faces=6):
    """Simulates the roll of a die with a given number of faces."""

    return random.randrange(1, faces + 1)

def roll(exp, sorted=False):
    """Simulates the roll of some dices expressed with the dice notation."""

    parts = exp.split('d')

    if len(parts) != 2 or not parts[1].isdigit():
        raise ValueError("Invalid dice expression")
    count = int(parts[0] or 1)
    faces = int(parts[1])

    rolls = [roll_die(faces) for _ in range(count)]

    if sorted:
        rolls.sort()

    return rolls

def discard(rolls, count):
    if count > len(rolls):
        raise ValueError("Can't discard more dice than there are in a throw")
    return rolls[count:]

def sum_roll(exp):
    """Returns the sumf of a roll of some dices expressed with the dice
    notation."""

    return sum(roll(exp))

def percentile_roll(exp):
    """Returns the result of rolling two dices expressed with the dice notation,
    and interpreted as a percentage."""

    results = roll(exp)

    if len(results) != 2:
        raise ValueError("Percentile roll must use two dice")

    return results[0] * 10 + results[1]
