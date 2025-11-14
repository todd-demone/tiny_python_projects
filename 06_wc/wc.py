#!/usr/bin/env python3
"""
Author : Todd Demone <tdemone1@gmail.com>
Date   : 2025-11-13
Purpose: Emulate wc (word count)
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Emulate wc (word count)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "file",
        metavar="FILE",
        nargs="*",  # 0 or more arguments; result will always be a list data type
        default=[sys.stdin],  # notice the default is in a list, too
        # (Below) Setting the 'type' key to readable text file means...
        # argparse validates they are readable text files
        # argparse provides us a list of OPEN file objects
        type=argparse.FileType("rt"),
        help="Input file(s)",
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """The main event"""

    args = get_args()
    total_lines, total_words, total_bytes = 0, 0, 0
    for fileobj in args.file:
        lines, words, bytes = 0, 0, 0
        for line in fileobj:
            lines += 1
            words += len(line.split())
            bytes += len(line)
        total_lines += lines
        total_words += words
        total_bytes += bytes
        print("{:8}{:8}{:8} {}".format(lines, words, bytes, fileobj.name))

    if len(args.file) > 1:
        print("{:8}{:8}{:8} total".format(total_lines, total_words, total_bytes))


# --------------------------------------------------
if __name__ == "__main__":
    main()
