import csv
import random
import copy

width = 10
height = 13

no_of_fabrics = 4

row_previous = []
row_current = []

write_filename = "quilt-pattern.csv"

# create the first row
for i in range(width):

	# For first in the first row just randomly add one
	if i == 0:
		row_current.append(random.randint(1, no_of_fabrics))
	else:
		choice_loop = random.randint(1, no_of_fabrics)
		while choice_loop == row_current[i-1]:
			choice_loop = random.randint(1, no_of_fabrics)
		row_current.append(choice_loop)

with open(write_filename, "a") as File:
	FileWriter = csv.writer(File)
	FileWriter.writerow(row_current)

row_previous = copy.deepcopy(row_current)

print("row_current", row_current)

# Do all the other rows
for _ in range(height-1):

	row_current = []

	# Do all the columns in this row
	for i in range(width):
		choice_loop = random.randint(1, no_of_fabrics)

		# For the first row
		if i == 0:
			while choice_loop == row_previous[i]:
				choice_loop = random.randint(1, no_of_fabrics)
			row_current.append(choice_loop)		

		# for the rest of the rows
		else:
			while choice_loop == row_previous[i] or choice_loop == row_current[i-1]:
				choice_loop = random.randint(1, no_of_fabrics)
			row_current.append(choice_loop)

	with open(write_filename, "a") as File:
		FileWriter = csv.writer(File)
		FileWriter.writerow(row_current)

	row_previous = copy.deepcopy(row_current)
