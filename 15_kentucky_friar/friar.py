#!/usr/bin/env python3
"""
Author : Todd Demone <tdemone1@gmail.com>
Date   : 2025-11-23
Purpose: Kentucky Friar
"""

import argparse
import os
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Southern fry text",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("text", metavar="text", help="Input text or file")

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read()

    return args


# --------------------------------------------------
def main():
    """The main event"""

    args = get_args()

    for line in args.text.splitlines():
        print(line.split())


# --------------------------------------------------
if __name__ == "__main__":
    main()
