#!/usr/bin/env python3
 
# --- LIBRARIES --- #
from argparse import ArgumentParser
import collections 
import unicodedata
 
 
# --- MAIN --------------- #
def main():
	parser = ArgumentParser(description = 'Print out every char in a file, its frequency in that file and its unicode codepoint.')
	parser.add_argument('input_file', help='input file, of whatever')
	args = parser.parse_args()
 	
	input_file = args.input_file
	counts = collections.Counter()
 	
	with open(input_file, 'r') as inFile:
		for line in inFile:
			line = line.strip()
			counts += collections.Counter(line)

	sorted_counts = sorted(counts.items(), key=lambda char: (-char[1], char[0]))

	for c in sorted_counts:
		# could also include unicodedata.category(c[0]), 
		print(c[0], '%04x' % ord(c[0]), c[1], unicodedata.name(c[0]), sep="\t")
 	
if __name__ == "__main__":
	main()

