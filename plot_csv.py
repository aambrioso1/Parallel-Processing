"""
Takes a text file of lines of pairs of numbers ss
"""

import plot

with open('mpi_csv_out.txt', 'r') as reader:
	# Read and print the entire file line by line
	x_list = []
	y_list = []
	for line in reader:
		pair = line.split(',')
		x, y = pair
		x = float(x)
		y = float(y)
		x_list.append(x)
		y_list.append(y)
plot.pl(x_list, y_list)