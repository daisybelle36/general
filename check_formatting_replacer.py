#!/usr/bin/env python3
"""
This script checks that the formatting of the replacer script is okay.
It also checks for duplicates:
- Does col 1 contain duplicates, but col 2 is different? (ie A -> B, then A -> C)
- Does col 2 appear in col 1 with a different col 2 (ie A -> B, then B -> C, or B -> A)
- Is col 2 the same as col 1? (Optional flag)
"""

# --- LIBRARIES --- #
from argparse import ArgumentParser

# --- HELPER FUNCTIONS --- #


def check_contains_tab(line, line_number):
    # Does every line contain at least one tab?
    if "\t" not in line:
        print("ERROR: Line {} does not have enough columns: {}".
              format(line_number, line))


def check_patterns(replacer_dict, line, pattern, replacement, line_number):
    # Does A -> B and A -> C?
    if pattern in replacer_dict:
        print("ERROR: Line {} pattern \"{}\" is already on line {}:".
              format(line_number, pattern, replacer_dict[pattern][0][1]))
        print("Line", replacer_dict[pattern][0][1], pattern, "\t", replacer_dict[pattern][0][0])
        print("Line", line_number, line)
        vals = replacer_dict[pattern]
        vals.append((replacement, line_number))
        replacer_dict[pattern] = vals
    else:
        replacer_dict[pattern] = [(replacement, line_number)]

    return replacer_dict


def print_check_replacements(replacer_dict, line, replacement, line_number):
    print("ERROR: Line {} replacement \"{}\" also occurs as a pattern on line {}:".
          format(line_number, replacement, replacer_dict[replacement][0][1]))
    print("Line", replacer_dict[replacement][0][1], replacement, "\t", replacer_dict[replacement][0][0])
    print("Line", line_number, line)


def check_replacements(replacer_dict, line, pattern, replacement, line_number, pattern_is_replacement_is_error):
    # Does A -> B and B -> A or C?
    if pattern_is_replacement_is_error:
        if replacement in replacer_dict or replacement == pattern:
            print_check_replacements(replacer_dict, line, replacement, line_number)
    else:
        if replacement in replacer_dict:
            print_check_replacements(replacer_dict, line, replacement, line_number)


# --- MAIN --------------- #
def main():
    # create parser
    parser = ArgumentParser(description='help text for script')
    # add arguments to parser
    parser.add_argument('replacerfile', help='2-col file: pattern, replacement')
    parser.add_argument('-f', '--flagpatternreplace', action='store_true',
                        help='pattern == replacement is an error; Default: not an error')
    # collate/parse arguments
    args = parser.parse_args()

    # pattern == replacement is error: True/False
    pattern_is_replacement_is_error = args.flagpatternreplace

    # read in replacerfile
    replacerfile = args.replacerfile
    replacer_dict = {}

    with open(replacerfile, 'r') as inFile:
        line_number = 1
        for line in inFile:
            line = line.strip()
            check_contains_tab(line, line_number)
            try:
                pattern = line.split("\t")[0]
                replacement = line.split("\t")[1]
            except IndexError:
                replacement = ""
            replacer_dict = check_patterns(replacer_dict, line, pattern, replacement, line_number)
            check_replacements(replacer_dict, line, pattern, replacement, line_number, pattern_is_replacement_is_error)

            line_number += 1
        inFile.close()


if __name__ == "__main__":
    main()
