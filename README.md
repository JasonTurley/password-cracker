# Saltine
Saltine is a simple password cracker built in Python. It currently can only crack plain-text passwords
but support for hashed passwords will be later implemented. This is a fun and educational personal project that is
loosely inspired by [John the Ripper](https://www.openwall.com/john/) and
[cheetah](https://github.com/shmilylty/cheetah).

## How to install
Clone the repo
```
git clone https://github.com/JasonTurley/saltine
```

## How to run
Execute the program with a list of passwords to crack and a word list. 
```
python3 saltine.py <hashed-passwords> <wordlist>
```


## What I Learned
+ How to implement a basic dictionary style password cracking attack
+ How to hash plaintext in python
+ How to open and close files in python

### Coming soon...
+ More cracking options than just SHA-256