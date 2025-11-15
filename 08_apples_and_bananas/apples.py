#!/usr/bin/env python3
"""
Author : Todd Demone <tdemone1@gmail.com>
Date   : 2025-11-14
Purpose: Apples and Bananas
"""

import argparse
import os
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Apples and Bananas",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("text", metavar="text", help="Input text or file")

    parser.add_argument(
        "-v",
        "--vowel",
        help="The vowel to substitute",
        metavar="vowel",
        type=str,
        default="a",
        choices=list("aeiou"),
    )

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text, "rt").read().rstrip()

    return args


# --------------------------------------------------
def main():
    """The main event"""

    args = get_args()
    vowel = args.vowel

    # METHOD 1: ITERATING THROUGH EVERY CHARACTER
    # new_text = []
    # for char in args.text:
    #     if char in "aeiou":
    #         new_text.append(vowel)
    #     elif char in "AEIOU":
    #         new_text.append(vowel.upper())
    #     else:
    #         new_text.append(char)
    # text = "".join(new_text)
    # print(text)

    # METHOD 2: USING THE STR.REPLACE() METHOD
    # for v in "aeiou":
    #     text = args.text.replace(v, vowel).replace(v.upper(), vowel.upper())
    # print(text)

    # METHOD 3: USING THE STR.TRANSLATE() METHOD
    trans = str.maketrans("aeiouAEIOU", vowel * 5 + vowel.upper() * 5)
    text = args.text.translate(trans)
    print(text)

    # METHOD 4: USING A LIST COMPREHENSION
    # new_text = [
    #     vowel if c in "aeiou" else vowel.upper() if c in "AEIOU" else c for c in args.text
    # ]
    # text = "".join(new_text)
    # print(text)

    # METHOD 5: USING A LIST COMPREHENSION WITH A FUNCTION (new_char(c) is A CLOSURE)
    # def new_char(c):
    #     return vowel if c in "aeiou" else vowel.upper() if c in "AEIOU" else c

    # text = "".join([new_char(c) for c in args.text])
    # print(text)

    # METHOD 6: USING THE MAP() FUNCTION
    # text = map(
    #     lambda c: vowel if c in "aeiou" else vowel.upper() if c in "AEIOU" else c,
    #     args.text,
    # )
    # print("".join(text))

    # METHOD 7: USING MAP() WITH A NAMED FUNCTION
    # def new_char(c):
    #     return vowel if c in "aeiou" else vowel.upper() if c in "AEIOU" else c

    # print("".join(map(new_char, args.text)))

    # METHOD 8: USEING REGULAR EXPRESSIONS
    # text = args.text
    # text = re.sub("[aeiou]", vowel, text)
    # text = re.sub("[AEIOU]", vowel.upper(), text)
    # print(text)


# --------------------------------------------------
if __name__ == "__main__":
    main()
