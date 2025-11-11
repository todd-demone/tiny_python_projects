#!/usr/bin/env python3
"""tests for crowsnest.py"""

import os
from subprocess import getstatusoutput, getoutput

prg = "./crowsnest.py"
consonant_words = [
    "brigantine",
    "clipper",
    "dreadnought",
    "frigate",
    "galleon",
    "haddock",
    "junk",
    "ketch",
    "longboat",
    "mullet",
    "narwhal",
    "porpoise",
    "quay",
    "regatta",
    "submarine",
    "tanker",
    "vessel",
    "whale",
    "xebec",
    "yatch",
    "zebrafish",
]
vowel_words = ["aviso", "eel", "iceberg", "octopus", "upbound"]
template = "Ahoy, Captain, {} {} off the larboard bow!"

nonalpha_words = ["123kid", "!peligro!"]


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ["-h", "--help"]:
        rv, out = getstatusoutput(f"{prg} {flag}")
        assert rv == 0
        assert out.lower().startswith("usage")


# --------------------------------------------------
def test_consonant():
    """brigantine -> a brigantine"""

    for word in consonant_words:
        out = getoutput(f"{prg} {word}")
        assert out.strip() == template.format("a", word)


# --------------------------------------------------
def test_consonant_upper():
    """brigantine -> a Brigatine"""

    for word in consonant_words:
        out = getoutput(f"{prg} {word.title()}")
        assert out.strip() == template.format("a", word.title())


# --------------------------------------------------
def test_vowel():
    """octopus -> an octopus"""

    for word in vowel_words:
        out = getoutput(f"{prg} {word}")
        assert out.strip() == template.format("an", word)


# --------------------------------------------------
def test_vowel_upper():
    """octopus -> an Octopus"""

    for word in vowel_words:
        out = getoutput(f"{prg} {word.upper()}")
        assert out.strip() == template.format("an", word.upper())


# fmt: off
# def test_vowel_upper_match_case():
    # """Octopus -> An Octopus"""
#
    # for word in vowel_words:
        # out = getoutput(f"{prg} {word.upper()}")
        # assert out.strip() == template.format("An", word.upper())
# fmt: on


# fmt: off
# def test_consonant_upper_match_case():
    # """Brigantine -> A Brigantine"""
#
    # for word in consonant_words:
        # out = getoutput(f"{prg} {word.upper()}")
        # assert out.strip() == template.format("A", word.upper())
# fmt: on


# fmt: off
# def test_starboard():
    # """--side starboard"""
# 
    # for word in consonant_words:
        # out = getoutput(f"{prg} {word} --side starboard")
        # assert out.strip() == "Ahoy, Captain, {} {} off the {} bow!".format(
            # "a", word, "starboard"
        # )
# fmt: on


def test_non_alpha():
    """123kid -> 'Try again."""
    for word in nonalpha_words:
        out = getoutput(f"{prg} {word}")
    assert out == "Try again."
