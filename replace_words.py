#!/usr/bin/env python3
"""
This script replaces user-defined strings in text files.
Replacement strings are defined in a 2-col, tab-delimited "replacer" file.
Column 1 = pattern to search for.
Column 2 = replacement to make.
Line 1 replacements occur before line 2 replacements.
"""

# --- LIBRARIES --- #
from argparse import ArgumentParser
from collections import OrderedDict
import sys


# --- MAIN --------------- #
def main():
    # create parser
    parser = ArgumentParser(description='help text for script')
    # add arguments to parser
    parser.add_argument('textfile', help='text file containing text to be replaced')
    parser.add_argument('-r', '--replacefile', help='2-col file: pattern, replacement')
    # collate/parse arguments
    args = parser.parse_args()

    # read in replacefile
    replacefile = args.replacefile
    replace_dict = OrderedDict()

    if replacefile is None:
        sys.exit("ERROR: Please include a -r REPLACEFILE")

    with open(replacefile, 'r') as inFile:
        for line in inFile:
            line = line.strip()
            pat_rep = line.split("\t")[0:2]
            replace_dict[pat_rep[0]] = pat_rep[1]
        inFile.close()

    # read in text file, make changes, and print it out again
    textfile = args.textfile
    with open(textfile, 'r') as inFile:
        for line in inFile:
            for pattern, replacement in replace_dict.items():
                line = line.replace(pattern, replacement)
            print(line.strip())


if __name__ == "__main__":
    main()
