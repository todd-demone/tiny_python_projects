#!/usr/bin/env python3
"""
Author : Todd Demone <tdemone1@gmail.com>
Date   : 2025-11-17
Purpose: Ransom note
"""

import argparse
import os
import random


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Ransom Note",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("text", metavar="text", help="Input text or file")

    parser.add_argument(
        "-s",
        "--seed",
        help="Random seed",
        metavar="int",
        type=int,
        default=None,
    )

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """The main event"""

    args = get_args()
    random.seed(args.seed)

    # USING A FOR LOOP
    # ransom = []
    # for char in args.text:
    #     ransom.append(choose(char))
    # print(''.join(ransom))

    # USING A LIST COMPREHENSION
    # ransom = [choose(char) for char in args.text]
    # print("".join(ransom))

    # USING A MAP()
    ransom = map(choose, args.text)
    print("".join(ransom))


def choose(char):
    return char.upper() if random.choice([0, 1]) else char.lower()


def test_choose():
    state = random.getstate()
    random.seed(1)
    assert choose("a") == "a"
    assert choose("b") == "b"
    assert choose("c") == "C"
    assert choose("d") == "d"
    random.setstate(state)


# --------------------------------------------------
if __name__ == "__main__":
    main()
