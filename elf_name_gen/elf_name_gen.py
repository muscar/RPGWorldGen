"""
Random names for elves in Dungeons and Dragons v3.5.
Content drawn from Races of the Wild sourcebook
"""

from random import *

with open("elf_name_prefixes.txt", 'r') as f:
	elf_name_prefixes = f.read().splitlines()

with open("elf_name_suffixes.txt", 'r') as f:
	elf_name_suffixes = f.read().splitlines()

with open("elf_house_name_prefixes.txt", 'r') as f:
	elf_house_prefixes = f.read().splitlines()

with open("elf_house_name_suffixes.txt", 'r') as f:
	elf_house_suffixes = f.read().splitlines()


female_suffixes = ["a", "ith", "ae"] # Exclusive to female-suffixed names
male_suffixes   = ["r", "am", "im"]  # Exclusive to male-suffixed names

def simple_elf_name_1():
	first = choice(elf_name_prefixes)
	last  = choice(elf_name_suffixes)

	return "{}{}".format(first, last)

def simple_elf_name_2():
	first  = choice(elf_name_prefixes)
	second = choice(elf_name_suffixes)
	last   = choice(elf_name_suffixes)

	return "{}{}{}".format(first, second, last)

def ornate_elf_name_1():
	first  = choice(elf_name_prefixes)
	second = choice(elf_name_suffixes)
	third  = choice(elf_name_prefixes)
	fourth = choice(elf_name_suffixes)
	last   = choice(elf_name_suffixes)

	return "{}{}'{}{}{}".format(first, second, third, fourth, last)

def ornate_elf_name_2():
	first  = choice(elf_name_suffixes).title()
	second = choice(elf_name_prefixes)
	third  = choice(elf_name_suffixes)
	last   = choice(elf_name_suffixes)

	return "{}'{}{}{}".format(first, second, third, last)

def simple_elf_house_name_1():
	first = choice(elf_house_prefixes)
	last  = choice(elf_house_suffixes)

	return "{}{}".format(first, last)

def simple_elf_house_name_2():
	first = simple_elf_name_1()
	last  = choice(elf_name_suffixes)

	return "{}{}".format(first, last)

def ornate_elf_house_name_1():
	first = simple_elf_house_name_1()
	last  = choice(elf_name_suffixes).title()

	return "{}'{}".format(first, last)

def ornate_elf_house_name_2():
	first = choice(elf_house_suffixes).title()
	last  = simple_elf_house_name_1()

	return "{}'{}".format(first, last)

def elf_name_grammatical_gender(name):
	"""
	returns 'male', 'female', or 'neuter':
	the grammatical gender of name. Should
	'neuter' not be desired, use
	resolve_gender_neutrality()
	to randomly assign a gender
	to name	 
	"""
	name = str(name).split()[0]
	gender = "neuter"

	f_sufs = (suf for suf in female_suffixes)
	m_sufs = (suf for suf in male_suffixes)

	if any(name.endswith(suf) for suf in f_sufs):
		gender = "female"
	elif any(name.endswith(suf) for suf in m_sufs):
		gender = "male"

	return gender

def resolve_gender_neutrality(name):
	"""
	Randomly assigns a 'male' or 'female'
	gender to a name which returns 'neuter'
	through elf_name_grammatical_gender()
	"""
	gender = elf_name_grammatical_gender(name)

	if gender == "neuter":
		n = randrange(1, 101)
		if n % 2 == 0:
			gender = "male"
		else:
			gender = "female"

	return gender

def random_elf_first_name():
	name = ""
	n = randrange(1000)
	
	if n % 2 == 0:
		name = simple_elf_name_1()
	elif n % 3 == 0:
		name = simple_elf_name_2()
	elif n % 5 == 0:
		name = ornate_elf_name_1()
	elif n % 7 == 0:
		name = ornate_elf_name_2()
	else:
		name = random_elf_name()

	return name

def random_elf_house_name():
	name = ""
	n = randrange(1000)
	
	if n % 2 == 0:
		name = simple_elf_house_name_1()
	elif n % 3 == 0:
		name = simple_elf_house_name_2()
	elif n % 5 == 0:
		name = ornate_elf_house_name_1()
	elif n % 7 == 0:
		name = ornate_elf_house_name_2()
	else:
		name = random_elf_house_name()

	return name

def random_elf_name():
	first = random_elf_first_name()
	last  = random_elf_house_name()

	return "{} {}".format(first, last)