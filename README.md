# Machete Hash Cracker
Machete is a super fast, multiprocessed and multithreaded hash cracker that supports MD5, SHA1, SHA256, SHA512, DSA, and Whirlpool hashes. It uses a highly optimized algorithm to generate child processes and threads to distribute the workload, allowing you to process wordlists of even several hundred million lines in just a few minutes. 
## Getting Started
#### Prerequisites
To get started with Machete, you'll need Python 3 and GIT. If you do not already have these packages, you can install them with: <br />
**Debian/Ubuntu/Kali Linux:** <br />
```$ sudo apt-get install python3 git``` <br />
**Redhat/CentOS Linux:** <br />
```$ sudo yum install python3 git``` <br />
**Arch Linux:** <br />
```$ sudo pacman -S python3 git```
#### Installation
Once you make sure you have these dependencies installed, you can proceed to download Machete's GIT repository to your machine. You can do this by using: <br />
```$ git clone https://github.com/bhammond604/machete.git``` <br />
This will create the directory ```machete/``` to which you will change to. Once you're in the ```machete/``` directory, you can use ```$ python3 machete.py -v``` to make sure it works.
## Basic Usage
Machete, despite its complexity, is rather simple to use. You only need to specify the hash you want to crack, the algorithm it uses, and the wordlist you're using to crack the hash. Basic usage is: <br />
```$ python3 machete.py -t TARGET HASH -a ALGORITHM -w WORDLIST``` <br />
This will attempt to crack the hash using a dictionary attack. For more information on Machete's various functions, use: <br />
```$ python3 machete.py -h```
## Credits
**Author** Brandon Hammond <br />
**Author Email** bhammond604@gmail.com <br />

