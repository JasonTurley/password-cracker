# Registers an individual's username and password into the database

import sys

def print_usage():
    """Prints the correct way to run the program."""
    print("Registers an individual's username and password into the database.")
    print()
    print("Usage: python3 {} cred_file".format(sys.argv[0]))


if len(sys.argv) != 2:
    print_usage()
    sys.exit()

with open(sys.argv[1], "a") as f:
    username = input("Enter your username: ")
    plaintext = input("Enter your password: ")

    # TODO encrypt password

    line = "{}:{}".format(username, plaintext)

    f.write(line)
    f.write("\n")
