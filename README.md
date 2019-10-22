# Saltine
Saltine is a simple password cracker built in Python. It currently can only crack plain-text passwords
but support for hashed passwords will be later implemented. This is a fun and educational personal project that is 
loosely inspired by [John the Ripper](https://www.openwall.com/john/). 

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

Cracked passwords are printed to the terminal.

## What I Learned
+ How to execute a dictionary attack
+ Practice writing documentation

### Coming soon...
+ Hash passwords before storing them
+ Allow users to register themselves in a textfile database
+ Write cracked passwords to a file instead of printing to terminal
