#!/usr/bin/env python3
 
# --- LIBRARIES --- #
from argparse import ArgumentParser
 
# --- VARIABLES --- #
HEAD_INDEX = 0
PRON_INDEX = 1
 
# --- OBJECTS ----- #
class Entry():
def __init__(self, head, pron, rank):
	self.head = head
	self.pron = pron
	self.rank = rank
 
# --- HELPER FUNCTIONS --- #
# none yet
 
# --- MAIN --------------- #
def main():
	# create parser
	parser = ArgumentParser(description = 'help text for script')
	# add arguments to parser
	parser.add_argument('lexicon', help='3-col lexicon')
	parser.add_argument('-w', '--word', help='col of headword, default = 1', default = 1)
	# collate/parse arguments
	args = parser.parse_args()
 	
	# read in lexicon
	lexicon = args.lexicon
	currentLexicon = []
 	
	with open(lexicon, 'r') as inFile:
		for line in inFile:
			currentLexicon.append(line.strip())
			inFile.close()
 	
	print(currentLexicon)
 	
if __name__ == "__main__":
main()

