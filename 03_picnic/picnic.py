#!/usr/bin/env python3
"""
Author : Todd Demone <tdemone1@gmail.com>
Date   : 2025-11-12
Purpose: Picnic game
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Picnic game",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("items", metavar="str", nargs="+", help="Item(s) to bring")

    parser.add_argument("-s", "--sorted", help="Sort the items", action="store_true")

    parser.add_argument("-n", "--nocomma", help="No oxford comma", action="store_true")

    parser.add_argument(
        "-d",
        "--delimiter",
        help="Character used to separate items",
        default=",",
        type=str,
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """The main event"""

    args = get_args()
    items = args.items
    delimiter = args.delimiter + " "
    num = len(items)

    if args.sorted:
        items.sort()

    bringing = ""
    if num == 1:
        bringing += items[0]
    elif num == 2:
        bringing += " and ".join(items)
    else:
        if args.nocomma:
            bringing += f"{delimiter.join(items[:-1])} and {items[-1]}"
        else:
            bringing += f"{delimiter.join(items[:-1])}{delimiter}and {items[-1]}"

    print(f"You are bringing {bringing}.")


# --------------------------------------------------
if __name__ == "__main__":
    main()
