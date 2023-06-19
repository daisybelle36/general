#!/usr/bin/env python3
 
# --- LIBRARIES --- #
from argparse import ArgumentParser
import collections 
import unicodedata
 
# --- VARIABLES --- #
 
# --- OBJECTS ----- #
 
# --- HELPER FUNCTIONS --- #
# none yet
 
# --- MAIN --------------- #
def main():
	# create parser
	parser = ArgumentParser(description = 'Print out every char in a file, its frequency in that file and its unicode codepoint.')
	# add arguments to parser
	parser.add_argument('input_file', help='input file, of whatever')
	#parser.add_argument('-w', '--word', help='col of headword, default = 1', default = 1)
	# collate/parse arguments
	args = parser.parse_args()
 	
	# read in input_file
	input_file = args.input_file
	counts = collections.Counter()
 	
	with open(input_file, 'r') as inFile:
		for line in inFile:
			#counts.append(line.strip())
			line = line.strip()
			counts += collections.Counter(line)
	print(counts)
	sorted_counts = sorted(counts.items(), key=lambda char: (-char[1], char[0]))
	#for c in sorted_counts:
		#print(c[0], \uc[0], c[1], sep="\t")

	for c in sorted_counts:
		# could also include unicodedata.category(c[0]), 
		print(c[0], '%04x' % ord(c[0]), c[1], unicodedata.name(c[0]), sep="\t")
 	
	#print(counts)
 	
if __name__ == "__main__":
	main()

