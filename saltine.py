#!/usr/bin python

"""
Saltine is a simple brute force password cracker. It is a toy program I created for educational purposes.
"""

import sys
import hashlib

__program__ = "saltine"
__version__ = "1.0.1"
__author__  = "Jason T"
__github__  = "https://github.com/JasonTurley/saltine"


def print_usage():
    print(__doc__)
    print("author: " + __author__)
    print("github: " + __github__)
    print()
    print("Usage: python3 {} <hashes> <wordlist>".format(sys.argv[0]))


def crack():
    total_cracked = 0

    with open(sys.argv[1], "r") as hash_file:
        with open(sys.argv[2], "r") as wordlist:

            for target in hash_file:
                # Need to remove the newline characters ('\n')
                target = target[:-1]

                for word in wordlist:
                    word = word[:-1]

                    # hashlib algorithms take bytes instead of strings in Python3
                    word_as_bytes = word.encode("utf-8")

                    # TODO: default is sha256, add option to select others
                    m = hashlib.sha256(word_as_bytes).hexdigest()  

                    if m == target:
                        print("[+] Cracked hash {}:{}".format(target, word))
                        total_cracked += 1
                        continue

                # Return to the start of the wordlist for each iteration
                wordlist.seek(0, 0)

            # If failed to crack hash
            print("[-] Failed to crack hash {} with given wordlist :(".format(target))

    # Print results
    print("Cracked a total of {} hashes".format(total_cracked))

    # TODO print total runtime

def main():
    if len(sys.argv) != 3:
        print_usage()
        exit(0)

    crack()


if __name__ == "__main__":
    main()
