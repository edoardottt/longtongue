"""

longtongue

Customized Password/Passphrase List inputting Target Info


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
import itertools

# ----- Global variables -----

symbols = [
    ".",
    "-",
    "_",
    "?",
    "!",
    "@",
    "#",
    "+",
    "*",
    "%",
    "&",
    "$",
]
common_pwds = [
    "password",
    "admin",
    "123456",
    "1234567890",
    "qwerty",
    "qwertyuiop",
    "webadmin",
    "1q2w3e4r5t",
    "qwerty123",
    "11111111",
]
leet_chars = {letter: str(index) for index, letter in enumerate("oizeasgtb")}
"""
leet_chars:
{   'a': '4',
    'b': '8',
    'e': '3',
    'g': '6',
    'i': '1',
    'o': '0',
    's': '5',
    't': '7',
    'z': '2',}
"""
directory = "output"
starting_year = 1990
ending_year = 2020
starting_number = 0
ending_number = 99
words_in_passphrase_max = 2  # HIGHLY recommended: don't edit this
items_limit = 200000  # unused now


# ----- Initial swag -----


def banner():
    print("")
    print(r" _                   _                               ")
    print(r"| | ___  _ __   __ _| |_ ___  _ __   __ _ _   _  ___ ")
    print(r"| |/ _ \| '_ \ / _` | __/ _ \| '_ \ / _` | | | |/ _ \\")
    print(r"| | (_) | | | | (_| | || (_) | | | | (_| | |_| |  __/")
    print(r"|_|\___/|_| |_|\__, |\__\___/|_| |_|\__, |\__,_|\___|")
    print(r"               |___/                |___/    ")
    print("")
    print(" + github.com/edoardottt/longtongue")
    print(" + edoardottt ~ edoardoottavianelli.it")
    print(" + GPLv3 License")
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
        "-p", "--person", action="store_true", help="Set the target to be a person"
    )
    group.add_argument(
        "-c",
        "--corporate",
        action="store_true",
        help="Set the target to be a corporate",
    )
    group.add_argument(
        "-v", "--version", action="store_true", help="Show the version of this program"
    )

    group_two = parser.add_mutually_exclusive_group(required=False)
    group_two.add_argument(
        "-l",
        "--leet",
        action="store_true",
        help="Add also complete 1337(leet) passwords",
    )
    group_two.add_argument(
        "-L",
        "--leetall",
        action="store_true",
        help="Add also ALL possible le37(leet) passwords",
    )
    group_three = parser.add_mutually_exclusive_group(required=False)
    group_three.add_argument(
        "-y",
        "--years",
        action="store_true",
        help="Add also years at password. See years range inside longtongue.py",
    )
    group_four = parser.add_mutually_exclusive_group(required=False)
    group_four.add_argument(
        "-n",
        "--numbers",
        action="store_true",
        help="Add also numbers at password. See numbers range inside longtongue.py",
    )

    return parser


# ----- Utils -----


def create_output_folder():
    if not os.path.exists(directory):
        os.makedirs(directory)


def create_output_file(input_filename):

    create_output_folder()
    filename = directory + "/" + input_filename

    if os.path.exists(filename):
        choice = input(
            "[!] {} already exists. Do you want to overwrite? (y/n):".format(
                input_filename
            )
        )
        if str(choice).lower() != "y":
            exit(1)
        # if choice == y: ====> go forward. The file's content will be flushed and overwritten
    else:
        os.mknod(filename)


def prepare_keywords(str_input):
    """
    It outputs None if blank
    It outputs an array if valid
    """
    if not str_input or len(str_input) == 0:
        return None
    temp = str_input.split(",")
    result = []
    for elem in temp:
        if elem.strip() != "":
            result.append(elem.strip())
    return result


def create_permutations_with_repetition(list_input, k):
    """
    It returns all the permutations with repetitions (with k elements) of list_input
    """
    unique_words = set(list_input)
    subsets = [p for p in itertools.product(unique_words, repeat=k)]

    return subsets


def flush_None_values(list_input):
    return [elem for elem in list_input if elem is not None and elem != ""]


def attr_keywords_in_unique_list(target):

    attributes = vars(target)
    attributes = flush_None_values(attributes.values())

    keywords = []
    for elem in attributes:
        if isinstance(elem, list):
            keywords.extend(elem)

    attributes = [elem for elem in attributes if not isinstance(elem, list)]

    attributes.extend(keywords)
    #  now attributes == all attributes + keywords

    result = list(set(attributes))

    return result


def trivial_pwds(attributes, years, numbers, output_file):
    """
    It writes the trivial pwds into output file.
    It doesn't write short pwds (length == 5 ).
    """

    with open(output_file, "w+") as f:

        for elem in attributes:
            f.write(elem + "\n")

            for symbol in symbols:
                """
                Symbol and attribute
                """
                if elem.lower() != elem.capitalize():
                    f.write(elem.lower() + symbol + "\n")
                    f.write(elem.upper() + symbol + "\n")
                    f.write(elem.capitalize() + symbol + "\n")
                else:
                    f.write(elem + symbol + "\n")

                # check length
                if len(elem) > 2 and numbers:
                    for number in range(starting_number, ending_number + 1):
                        """
                        Symbol, attribute and number
                        """
                        if elem.lower() != elem.capitalize():
                            f.write(elem.lower() + symbol + str(number) + "\n")
                            f.write(elem.upper() + symbol + str(number) + "\n")
                            f.write(elem.capitalize() + symbol + str(number) + "\n")
                        else:
                            f.write(elem + symbol + str(number) + "\n")

                if years:
                    for year in range(starting_year, ending_year + 1):
                        """
                        Symbol, attribute and year
                        """
                        if elem.lower() != elem.capitalize():
                            f.write(elem.lower() + symbol + str(year) + "\n")
                            f.write(elem.upper() + symbol + str(year) + "\n")
                            f.write(elem.capitalize() + symbol + str(year) + "\n")
                        else:
                            f.write(elem + symbol + str(year) + "\n")


def permutations(attributes, years, numbers, output_file):
    """
    It writes the combinations between all the elements involved:
    attributes, keywords, numbers, symbols
    """
    subsets = create_permutations_with_repetition(attributes, words_in_passphrase_max)

    with open(output_file, "a+") as f:
        for subset in subsets:

            # ATTENTION - THIS WORKS WITH words_in_passphrase_max = 2 ONLY !
            par1, par2 = subset

            f.write(par1 + par2 + "\n")  # par1 par2

            for symbol in symbols:
                f.write(par1 + symbol + par2 + "\n")  # par1 symbol par2

                if numbers:
                    for number in range(starting_number, ending_number + 1):
                        f.write(
                            par1 + symbol + par2 + str(number) + "\n"
                        )  # par1 symbol par2 number
                        f.write(
                            par1 + par2 + symbol + str(number) + "\n"
                        )  # par1 par2 symbol number

                if years:
                    for year in range(starting_year, ending_year + 1):
                        f.write(
                            par1 + symbol + par2 + str(year) + "\n"
                        )  # par1 symbol par2 year
                        f.write(
                            par1 + par2 + symbol + str(year) + "\n"
                        )  # par1 par2 symbol year

                for symbol2 in symbols:

                    if numbers:
                        for number in range(starting_number, starting_number + 1):
                            f.write(
                                par1 + symbol + par2 + symbol2 + str(number) + "\n"
                            )  # par1 symbol par2 symbol number

                    if years:
                        for year in range(starting_year, ending_year + 1):
                            f.write(
                                par1 + symbol + par2 + symbol2 + str(year) + "\n"
                            )  # par1 symbol par2 symbol year

            if numbers:
                for number in range(starting_number, ending_number + 1):
                    f.write(par1 + par2 + str(number) + "\n")  # par1 par2 number

            if years:
                for year in range(starting_year, ending_year + 1):
                    f.write(par1 + par2 + str(year) + "\n")  # par1 par2 year


def common_passwords(attributes, years, numbers, output_file):
    """
    It writes the common customized passwords:
    password, admin, 12345678 ...
    """
    with open(output_file, "a+") as f:
        for elem in common_pwds:
            f.write(elem + "\n")


def leet_pwds(leetall, output_file):
    """
    1337 passwords
    if leetall ==> all possible combinations
                    e.g. leet -> l3e7
    else:
            ==> switch all chars
                    e.g. leet -> l337
    """
    pwds = []
    with open(output_file, "r+") as f:
        pwds = f.read().split()

    with open(output_file, "a+") as f:

        for elem in pwds:

            continues = False
            for key in leet_chars:
                if key in elem:
                    continues = True
                    break
                else:
                    continues = False

            if continues:
                if leetall:

                    possibles = []

                    for lower in elem.lower():
                        ll = leet_chars.get(lower, lower)
                        possibles.append((lower,) if ll == lower else (lower, ll))

                    leets = ["".join(t) for t in itertools.product(*possibles)]

                    for leet in leets:
                        f.write(leet + "\n")

                else:

                    # copy without passing reference
                    leet = (elem + ".")[:-1]

                    for char in leet_chars.keys():
                        leet.replace(char, leet_chars[char])

                    f.write(leet + "\n")


# ----- Person -----


class Person:
    def __init__(
        self,
        name=None,
        middle_name=None,
        surname=None,
        nickname=None,
        username=None,
        age=None,
        birth_day=None,
        birth_month=None,
        birth_year=None,
        email=None,
        birth_place=None,
        first_pet=None,
        second_pet=None,
        favourite_band=None,
        person_keywords=None,
    ):

        self.name = name
        self.middle_name = middle_name
        self.surname = surname
        self.nickname = nickname
        self.username = username
        self.age = age
        self.birth_day = birth_day
        self.birth_month = birth_month
        self.birth_year = birth_year
        self.email = email
        self.birth_place = birth_place
        self.first_pet = first_pet
        self.second_pet = second_pet
        self.favourite_band = favourite_band
        self.person_keywords = person_keywords


def person(add_leet, years, leetall, numbers):
    print("Targeting a person.\n")
    target = input_person()
    default_output = False

    # output filename
    if target.name and target.name != "":
        create_output_file(target.name + "-" + target.surname + ".txt")

    else:
        create_output_file("longtongue-output.txt")
        default_output = True

    if default_output:
        output_file = "output/" + "longtongue-output.txt"
    else:
        output_file = "output/" + target.name + "-" + target.surname + ".txt"

    # real computation here

    attributes = attr_keywords_in_unique_list(target)

    trivial_pwds(attributes, years, numbers, output_file)

    common_passwords(attributes, years, numbers, output_file)

    permutations(attributes, years, numbers, output_file)

    if add_leet or leetall:
        leet_pwds(leetall, output_file)


def input_person():

    target = Person()

    print(
        "Enter all the information you know. Leave blank and hit enter if you don't know.\n"
    )
    target.name = input("[>] Name: ")
    target.middle_name = input("[>] Middle Name: ")
    target.surname = input("[>] Surname: ")
    target.nickname = input("[>] Nickname: ")
    target.username = input("[>] Username: ")
    target.age = input("[>] Age: ")
    target.birth_day = input("[>] Birth day: ")
    target.birth_month = input("[>] Birth month: ")
    target.birth_year = input("[>] Birth year(YYYY): ")
    target.email = input("[>] Email: ")
    target.birth_place = input("[>] Birth place: ")
    target.first_pet = input("[>] First pet: ")
    target.second_pet = input("[>] Second pet: ")
    target.favourite_band = input("[>] Favourite Band: ")

    person_keywords = input("[>] Useful keywords (separated by comma): ")

    target.person_keywords = prepare_keywords(person_keywords)

    return target


# ----- Corporate -----


class Corporate:
    def __init__(
        self,
        name=None,
        web_domain=None,
        birth_year=None,
        corporate_keywords=None,
    ):

        self.name = name
        self.web_domain = web_domain
        self.birth_year = birth_year
        self.corporate_keywords = corporate_keywords


def corporate(add_leet, years, leetall, numbers):
    print("Targeting a corporate.\n")
    target = input_corporate()
    default_output = False

    # output filename
    if target.name and target.name != "":
        create_output_file(target.name + ".txt")
    else:
        create_output_file("longtongue-output.txt")
        default_output = True

    if default_output:
        output_file = "output/" + "longtongue-output.txt"
    else:
        output_file = "output/" + target.name + ".txt"

    # real computation here

    attributes = attr_keywords_in_unique_list(target)

    trivial_pwds(attributes, years, numbers, output_file)

    common_passwords(attributes, years, numbers, output_file)

    permutations(attributes, years, numbers, output_file)

    if add_leet or leetall:
        leet_pwds(leetall, output_file)


def input_corporate():

    target = Corporate()

    print(
        "Enter all the information you know. Leave blank and hit enter if you don't know.\n"
    )
    target.name = input("[>] Name: ")
    target.web_domain = input("[>] Web domain (without protocol): ")
    target.birth_year = input("[>] Birth year (YYYY): ")

    corporate_keywords = input("[>] Useful keywords (separated by comma): ")
    target.corporate_keywords = prepare_keywords(corporate_keywords)

    return target


# ----- Main function -----


def main():

    banner()

    parser = get_parser()
    args = parser.parse_args()

    if args.version:
        version()
    elif args.corporate:
        corporate(args.leet, args.years, args.leetall, args.numbers)
    elif args.person:
        person(args.leet, args.years, args.leetall, args.numbers)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
