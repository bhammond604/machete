# Machete Hash Cracker
# Version 1.0.0
# By Brandon Hammond

# Set the version and author
__version__ = "1.0.1"
__author__ = "Brandon Hammond"

# Import required modules
import os
import sys
import time
import getopt
import string
import threading
import core.misc as machete
import core.machete_md5 as machete_md5
import core.machete_sha1 as machete_sha1
import core.machete_sha256 as machete_sha256
import core.machete_sha512 as machete_sha512
import core.machete_dsa as machete_dsa
import core.machete_whirlpool as machete_whirlpool

# Define main() function
def main():
	# Function: main()
	# Purpose: Parse user input
	
	# Start parsing user input
	
	# Attempt to call getopt.getopt()
	try:
		opts, args = getopt.getopt(sys.argv[1:], "hva:t:w:m", ["help", "version", "alg=", "hash=", "wordlist=", "threading"])
	except getopt.GetoptError:
		# Display error message and exit
		print("[E] Error parsing options")
		
	# Predefine variables
	algorithm = None
	target_hash = None
	wordlist = None
	use_threading = None
	
	# Build for loop to parse options
	for opt, arg in opts:
		# If -h or --help option used
		if opt in ("-h", "--help"):
			# Print help message and exit
			print("USAGE:")
			print("\tmachete [-h] [-v] [-m] [-a ALGORITHM] [-t HASH] [-w WORDLIST]")
			print("")
			print("Crack a hash using a wordlist attack. Supports MD5, SHA1, SHA256, SHA512, DSA, and Whirlpool hashes.")
			print("")
			print("REQUIRED ARGUMENTS:")
			print("\t-a, --algorithm ALGORITHM\tSpecify the algorithm to use")
			print("\t-t, --hash HASH\tSpecify the hash to crack")
			print("\t-w, --wordlist WORDLIST\tSpecify the wordlist to use")
			print("")
			print("OPTIONAL ARGUMENTS:")
			print("\t-h, --help\tDisplay this message and exit")
			print("\t-v, --version\tDisplay version info and exit")
			print("\t-m, --threading\tEnable threading. Off by default"
			exit(0)
		
		# If -v or --version option is used
		elif opt in ("-v", "--version"):
			# Print version message and exit
			print("Machete Hash Cracker")
			print("Version {}".format(__version__))
			print("By {}".format(__author__))
			exit(0)
		
		# If -a or --alg option is used
		elif opt in ("-a", "--alg"):
			# Set hash algorithm to use
			algorithm = arg
		
		# If -t or --hash option is used
		elif opt in ("-t", "--hash"):
			# Set hash to crack
			target_hash = arg
		
		# If -w or --wordlist option is used
		elif opt == "-w" or opt == "--wordlist":
			# Set wordlist to use
			wordlist = arg
			
		# If -m or --threading option is used
		elif opt in ("-m", "--threading"):
			# Set use_threading
			use_threading = True
			
	# End of parsing input

	# Use machete.determine_algorithm()
	attack = machete.determine_algorithm(algorithm)
	
	# If use_threading is True, handle thread creation
	if use_threading == True:
		# Display status message
		print("[I] Starting multithreaded attack...")
		
		# Dump wordlist to list
		flist = machete.open_list(wordlist)
		
		# Split flist into several lists using machete.split_list()
		thread_lists = list(machete.split_list(flist))
		
		# Build for loop to create and start threads
		for i in range(0, len(thread_lists)):
			# Define thread
			attack_thread = attack(thread_lists[i], target_hash)
			
			# Start thread
			attack_thread.start()

	# If use_threading is not true, simply execute the attack using only 1 thread
	else:
		# Display status message
		print("[I] Starting attack...")
		
		# Open wordlist
		flist = machete.open_list(wordlist)
		
		# Create thread
		attack_thread = attack(flist, target_hash)
		
		# Start thread
		attack_thread.start()

# Make sure not running as module and call main()
if __name__ == "__main__":
	main()
