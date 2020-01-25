#!/usr/bin python

"""
Saltine is a simple brute force password cracker. It is a toy program I created for educational purposes.
"""

# User file format
# username:password

import sys

__program__ = "saltine"
__version__ = "1.0.1"
__author__  = "Jason T"
__github__  = "https://github.com/JasonTurley/saltine"


def print_usage():
    print(__doc__)
    print("author: " + __author__)
    print("github: " + __github__)
    print()
    print("Usage: python3 {} <users_file> <dict_file>".format(sys.argv[0]))

def crack():
    with open(sys.argv[1], "r") as user_file:
        with open(sys.argv[2], "r") as dict_file:

            # Get the current username and the password to crack
            for line in user_file:
                username, password = line.split(":")  # ["user", "password"]
                password = password.replace("\n", "")

                # Execute the dictionary attack
                for attempt in dict_file:
                    attempt = attempt.replace("\n", "")

                    if attempt == password:
                        print("The password for {} is {}".format(username, attempt))
                        break

                # Need to seek to start of dictionary file
                dict_file.seek(0, 0)

def main():
    if len(sys.argv) != 3:
        print_usage()
        exit(0)

    crack()

if __name__ == "__main__":
    main()
