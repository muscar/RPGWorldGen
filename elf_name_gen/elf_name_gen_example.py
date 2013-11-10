from elf_name_gen import *

for i in range(10):
	print(random_elf_name())

print

for i in range(10):
	name   = random_elf_name()
	gender = elf_name_grammatical_gender(name)

	print(name, gender)

print

for i in range(10):
	name   = random_elf_name()
	gender = elf_name_grammatical_gender(name)

	if gender == 'neuter':
		gender = resolve_gender_neutrality(name)
		
	print(name, gender)
