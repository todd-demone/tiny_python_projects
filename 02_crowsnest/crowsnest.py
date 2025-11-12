#!/usr/bin/env python3
"""
Author : Todd Demone <tdemone1@gmail.com>
Date   : 2025-11-11
Purpose: Choose the correct article
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Crow's Nest -- choose the correct article",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("word", metavar="word", help="A word")

    #
    # Going further, part 2: accept param that changes larboard to starboard.
    #
    # parser.add_argument(
    # "-s", "--side", metavar="str", default="larboard", help="Side of the boat",
    # choices=['starboard', 'larboard']
    # )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.word
    if word[0].isalpha():
        # side = args.side
        article = "an" if word[0].lower() in "aeiou" else "a"
        #
        # Going further, part 1: match case of incoming word (for example,
        # 'an octopus' and 'An Octopus'.
        #
        # article = article.capitalize() if word[0].isupper() else article

        print(f"Ahoy, Captain, {article} {word} off the larboard bow!")
        # print(f"Ahoy, Captain, {article} {word} off the {side} bow!")
    else:
        print("Try again.")


# --------------------------------------------------
if __name__ == "__main__":
    main()
