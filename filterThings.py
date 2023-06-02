#!/usr/bin/env python3
# filter two files, and return either matches, OR things in file 1 but NOT in file 2
# use first column (delimited by tab) as key
 
# --- LIBRARIES --- #
from argparse import ArgumentParser
 
# --- VARIABLES --- #
 
# --- OBJECTS ----- #
 
# --- HELPER FUNCTIONS --- #
 
def return_matches(file1, items_file2):
	with open(file1, 'r') as inFile:
		for line in inFile:
			if line.strip().split("\t")[0] in items_file2:
				print(line.strip())

def return_missing(file1, items_file2):
	with open(file1, 'r') as inFile:
		for line in inFile:
			if line.strip().split("\t")[0] not in items_file2:
				print(line.strip())


# --- MAIN --------------- #
def main():
	# create parser
	parser = ArgumentParser(description = 'help text for script')
	# add arguments to parser
	parser.add_argument('file1', help='reference file, output will be in this file')
	parser.add_argument('operator', help='use "and" or "not" to decide which lines will be output')
	parser.add_argument('file2', help='comparison file, output will be, or will NOT be, in this file')
	# collate/parse arguments
	args = parser.parse_args()
 	
	# read in files and operator
	file1 = args.file1
	file2 = args.file2
	operator = args.operator
	items_file2 = []
 	
	with open(file2, 'r') as inFile:
		for line in inFile:
			items_file2.append(line.strip().split("\t")[0])
 	
	if operator == "and":
		return_matches(file1, items_file2)
	if operator == "not":
		return_missing(file1, items_file2)
 	
if __name__ == "__main__":
	main()

