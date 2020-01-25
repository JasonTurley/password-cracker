# Saltine
Saltine is a simple password cracker built in Python. It currently can only crack plain-text passwords
but support for hashed passwords will be later implemented. This is a fun and educational personal project that is
loosely inspired by [John the Ripper](https://www.openwall.com/john/) and
[cheetah](https://github.com/shmilylty/cheetah).

## How to install
Clone the repo
```
git clone https://github.com/JasonTurley/password-cracker
```

## How to use
The program needs to be supplied with a password file and user credential file in order run.
```
python3 cracker.py [PASSWORD-LIST] [CREDS-LIST]
```

Cracked passwords are printed to the terminal as well to an output file labeled *results*.

## What I Learned
+ How to execute a basic dictionary attack
+ Opening and closing files in Python
+ Practice writing documentation

### Coming soon...
+ Support for hashing passwords
+ A test suite
