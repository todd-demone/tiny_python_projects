#!/usr/bin/env python3
"""
Author : Todd Demone <tdemone1@gmail.com>
Date   : 2025-11-14
Purpose: Lookup tables
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Gashlycrumb",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "letter", metavar="letter", help="Letter(s)", type=str, nargs="+"
    )

    parser.add_argument(
        "-f",
        "--file",
        help="Input file",
        metavar="FILE",
        type=argparse.FileType("rt"),
        default="gashlycrumb.txt",
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """The main event"""

    args = get_args()

    lookup = {line[0].upper(): line.rstrip() for line in args.file}
    # lookup = {}
    # for line in args.file:
    #     lookup[line[0].upper()] = line.rstrip()

    for letter in args.letter:
        print(lookup.get(letter.upper(), f'I do not know "{letter}".'))
        # print(
        #     lookup[letter.upper()]
        #     if letter.upper() in lookup
        #     else f'I do not know "{letter}".'
        # )


# --------------------------------------------------
if __name__ == "__main__":
    main()
