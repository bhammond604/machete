# Machete Hash Cracker
By Brandon Hammond

---

## About
Machete is a hash breaking tool written in Python for Linux. It uses a dictionary attack to
find the plaintext, but unlike other dictionary attack scripts, Machete dumps the contents
of the wordlist to a list structure. This is because accessing items from a list is far 
faster than reading line-by-line from an external file. Currently, Machete supports MD5, SHA-1,
SHA-224, SHA-512, DSA, and Whirlpool hashes, but more are going to be added in later versions.

---

## Usage
    $ machete [options] [arguments]
#### Options:
-h or --help ::: Display help message

-v or --version ::: Display version message

-a or --alg {algorithm} ::: Set algorithm to use

-t or --hash {hash} ::: Set hash to crack

-w or --wordlist {wordlist} ::: Set wordlist to use

-m or --threading ::: Specify that you want to use multithreading
