"""

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see http://www.gnu.org/licenses/.

    @Repository:    https://github.com/edoardottt/longtongue

    @Author:        edoardottt, https://www.edoardoottavianelli.it

"""


# ----- Import external libraries -----
import argparse
import os


# ----- Global variables -----

symbols = [
    ",",
    ".",
    "-",
    "_",
    "?",
    "!",
    "@",
    "#",
    "+",
    "*",
    "(",
    ")",
    "%",
    "&",
    "$",
]
directory = "output"
starting_year = 1900
ending_year = 2020
starting_number = 0
ending_number = 99
words_in_passphrase_max = 2

# ----- Initial swag -----


def banner():
    print("LONGTONGUE")
    print("")
    print("edoardottt |- github.com/edoardottt")
    print("           |- edoardoottavianelli.it")
    print("GPLv3 License")
    print("------------------------")


def version():
    print("0.1\n")


# ----- Input -----


def get_parser():
    """Create and return a parser (argparse.ArgumentParser instance) for main()
    to use"""
    parser = argparse.ArgumentParser(
        description="Customized Password/Passphrase List inputting Target Info"
    )
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument(
        "-p", "--person", action="store_true", help="Set the target to be a person."
    )
    group.add_argument(
        "-c",
        "--corporate",
        action="store_true",
        help="Set the target to be a corporate.",
    )
    group.add_argument(
        "-v", "--version", action="store_true", help="Show the version of this program."
    )

    return parser


# ----- Utils -----


def create_output_folder():
    if not os.path.exists(directory):
        os.makedirs(directory)


# def enter_input():


# ----- Person -----


def person():
    print("person\n")


# ----- Corporate -----


def corporate():
    print("corporate\n")


# ----- Main function -----


def main():

    banner()

    parser = get_parser()
    args = parser.parse_args()

    if args.version:
        version()
    elif args.corporate:
        corporate()
    elif args.person:
        person()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
