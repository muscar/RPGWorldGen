"""
Random generation of dwarf names.
Content from the D&D v3.5 sourcebook Races of Stone
"""
from random import *

with open("__txt__/dwarf_prefixes.txt", 'r') as f:
	dwarf_prefixes = f.read().splitlines()

with open("__txt__/dwarf_male_suffixes.txt", 'r') as f:
	dwarf_male_suffixes = f.read().splitlines()

with open("__txt__/dwarf_female_suffixes.txt", 'r') as f:
	dwarf_female_suffixes = f.read().splitlines()

with open("__txt__/dwarf_house_suffixes.txt", 'r') as f:
	dwarf_house_suffixes = f.read().splitlines() 

def simple_male_dwarf_name_1():
	first = choice(dwarf_prefixes)
	last  = choice(dwarf_male_suffixes)

	return "{}{}".format(first, last)

def simple_male_dwarf_name_2():
	first = simple_male_dwarf_name_1()
	last  = choice(dwarf_male_suffixes)

	return "{}{}".format(first, last)

def ornate_male_dwarf_name_1():
	first = simple_male_dwarf_name_1()
	last  = choice(dwarf_male_suffixes)

	return "{}-{}".format(first, last)

def ornate_male_dwarf_name_2():
	first = simple_male_dwarf_name_1()
	last  = simple_male_dwarf_name_2()

	return "{}-{}".format(first, last)

def simple_female_dwarf_name_1():
	first = choice(dwarf_prefixes)
	last  = choice(dwarf_female_suffixes)

	return "{}{}".format(first, last)

def simple_female_dwarf_name_2():
	first = simple_female_dwarf_name_1()
	last  = choice(dwarf_female_suffixes)

	return "{}{}".format(first, last)

def ornate_female_dwarf_name_1():
	first = simple_female_dwarf_name_1()
	last  = choice(dwarf_female_suffixes)

	return "{}-{}".format(first, last)

def ornate_female_dwarf_name_2():
	first = simple_female_dwarf_name_1()
	last  = simple_female_dwarf_name_2()

	return "{}-{}".format(first, last)

def simple_dwarf_house_name_1():
	first = choice(dwarf_prefixes)
	last  = choice(dwarf_house_suffixes)

	return "{}{}".format(first, last)

def simple_dwarf_house_name_2():
	first = simple_dwarf_house_name_1()
	last  = choice(dwarf_house_suffixes)

	return "{}{}".format(first, last)

def ornate_dwarf_house_name_1():
	first = choice(dwarf_prefixes)
	last  = simple_dwarf_house_name_1()

	return "{}-{}".format(first, last)

def ornate_dwarf_house_name_2():
	first = simple_dwarf_house_name_1()
	last  = simple_dwarf_house_name_2()

	return "{}-{}".format(first, last)


def is_male_name(name):
	b = False

	for suf in dwarf_male_suffixes:
		if name.endswith(suf):
			b = True

	return b

def is_female_name(name):
	return not is_male_name(name)

def dwarf_name_gramatical_gender(name):

	gender = "" # should never return this

	if is_male_name(name):
		gender = "male"
	else:
		gender = "female"

	return gender

def random_male_dwarf_first_name():
	n    = randrange(1, 1000)
	name = ""

	while name == "":
		if n % 2 == 0:
			name = simple_male_dwarf_name_1()
		elif n % 3 == 0:
			name = simple_male_dwarf_name_2()
		elif n % 5 == 0:
			name = ornate_male_dwarf_name_1()
		elif n % 11 == 0:
			name = ornate_male_dwarf_name_2()
		else:
			n = randrange(1000)


	return name

def random_female_dwarf_first_name():
	n    = randrange(1, 1000)
	name = ""

	while name == "":
		if n % 2 == 0:
			name = simple_female_dwarf_name_1()
		elif n % 3 == 0:
			name = simple_female_dwarf_name_2()
		elif n % 5 == 0:
			name = ornate_female_dwarf_name_1()
		elif n % 11 == 0:
			name = ornate_female_dwarf_name_2()
		else:
			n = randrange(1000)

	return name

def random_dwarf_house_name():
	n    = randrange(1, 1000)
	name = ""

	while name == "":
		if n % 2 == 0:
			name = simple_dwarf_house_name_1()
		elif n % 3 == 0:
			name = simple_dwarf_house_name_2()
		elif n % 5 == 0:
			name = ornate_dwarf_house_name_1()
		elif n % 11 == 0:
			name = ornate_dwarf_house_name_2()
		else:
			n = randrange(1000)

	return name

def random_male_dwarf_name():
	first = random_male_dwarf_first_name()
	last  = random_dwarf_house_name()

	return "{} {}".format(first, last)

def random_female_dwarf_name():
	first = random_female_dwarf_first_name()
	last  = random_dwarf_house_name()

	return "{} {}".format(first, last)
