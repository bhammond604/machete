# Machete Hash Cracker
# Version 2.0.0
# By Brandon Hammond

# Define the version and author
__version__ = "2.0.0"
__author__ = "Brandon Hammond" 

# Import required modules
import os
import sys
import getopt
import multiprocessing
import threading
import hashlib
from core import child

# Define split_list() function
def split_list(wordlist):
	# Function: split_list()
	# Purpose: Split wordlist into several smaller lists for threading
	
	# Set the list size
	list_size = 1000000
	
	# Split the main list into a 2D list
	for i in range(0, len(wordlist), list_size):
		yield wordlist[i:i + list_size]

# Define the main() function
def main():
	# Function: main()
	# Purpose: Process command line arguments and provide base workflow
	
	# Attempt to call getopt.getopt() to read and parse command line arguments
	try:
		opts, args = getopt.getopt(sys.argv[1:], "hva:t:w:", ("help", "version", "algorithm=", "hash=", "wordlist="))
	except getopt.GetoptError:
		# Display error message and exit
		print("[E] An error occured processing command line arguments!")
		exit(0)
		
	# Predefine important variables with their default values
	algorithm = None
	target_hash = None
	wordlist = None
	
	# Build a for loop to process the command line arguments one at a time
	for opt, arg in opts:
		# If the -h or --help option is used
		if opt in ("-h", "--help"):
			# Display the help message and exit
			print("USAGE:")
			print("\tmachete [-h] [-v] [-a ALGORITHM] [-t TARGET HASH] [-w WORDLIST]")
			print("")
			print("Crack a hash taking advantage of multiprocessing. Uses a hyper-efficient")
			print("algorithm that supports MD5, SHA1, SHA256, and SHA512 algorithms.")
			print("")
			print("REQUIRED ARGUMENTS:")
			print("\t-a, --algorithm ALGORITHM\tSpecify the algorithm to use when cracking the hash.")
			print("\t-t, --hash TARGET HASH\tSpecify the hash to be cracked.")
			print("\t-w, --wordlist WORDLIST\tSpecify the wordlist to be used in the attack.")
			print("")
			print("OPTIONAL ARGUMENTS:")
			print("\t-h, --help\tDisplay this message and exit.")
			print("\t-v, --version\tDisplay version message and exit.")
			exit(0)
			
		# If the -v or --version option is used
		elif opt in ("-v", "--version"):
			# Display the version message and exit
			print("Machete Hash Cracker")
			print("Version {}".format(__version__))
			print("By {}".format(__author__))
			exit(0)
			
		# If the -a or --algorithm option is used
		elif opt in ("-a", "--algorithm"):
			# Make sure the specified algorithm is valid
			if arg in ("md5", "sha1", "sha256", "sha512", "dsa", "whirlpool"):
				# The specified algorithm is supported, set it
				algorithm = arg
			else:
				# The specified algorithm is not supported, display an error message
				print("[!] Unsupported algorithm: {}".format(arg))
				exit(0)
				
		# If the -t or --hash option is used
		elif opt in ("-t", "--hash"):
			# Specify the target hash
			target_hash = arg
			
		# If the -w or --wordlist option is used
		elif opt in ("-w", "--wordlist"):
			# Specify the wordlist
			wordlist = arg
			
		# If an invalid option was used
		else:
			# Display an error message and exit
			print("[!] Invalid option: {}".format(opt))
			exit(0)
	
	# Display the introduction message
	print("==============================")
	print("Machete Hash Cracker")
	print("==============================")
	print("[*] Target Hash: {}".format(target_hash))
	print("[*] Algorithm: {}".format(algorithm))
	print("[*] Wordlist: {}".format(wordlist))
	print("==============================")
	
	# Attempt to open the wordlist and dump it into RAM
	try:
		open_wordlist = open(wordlist, "r")
	except IOError:
		# Display an error message and exit
		print("[E] Could not open the wordlist!")
		exit(0)
		
	# Split the wordlist into several smaller lists
	process_lists = list(split_list(open_wordlist.readlines()))
	
	# Build a for loop to spawn the child processes
	for i in range(0, len(process_lists)):
		
		# Create the object for the new child process
		child_process = multiprocessing.Process(target = child.main, args = (process_lists[i], algorithm, target_hash,))

		# Start the new child process
		child_process.start()

# Make sure not running as a module and call main()
if __name__ == "__main__":
	main()
