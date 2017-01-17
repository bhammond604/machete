# Import modules
import machete_md5
import machete_sha1
import machete_sha256
import machete_sha512
import machete_dsa
import machete_whirlpool

# Define open_list() function
def open_list(wordlist):
	# Function: open_list()
	# Purpose: Open wordlist and dump contents to list
	
	# Attempt to open wordlist file
	try:
		f = open(wordlist, "r")
	except IOError:
		# Display error message and exit
		print("[E] Error opening wordlist")
		exit(0)
	
	# Display optimizing message
	print("[I] Optimizing wordlist...")
	
	# Dump wordlist to list structure
	flist = f.readlines()
	
	# Return flist
	return flist

# Define split_list() function
def split_list(flist):
	# Function: split_list()
	# Purpose: Split flist into several smaller lists for threading
	
	# Set list_size
	list_size = 1000000
	
	# Split into 2d list
	for i in range(0, len(flist), list_size):
		yield flist[i:i + list_size]
		
# Define determine_algorithm() function
def determine_algorithm(algorithm):
	# Function: determine_algorithm()
	# Purpose: Determine algorithm to use
	
	# If md5
	if algorithm == "md5":
		# Set attack decorator to machete_md5()
		attack = machete_md5.crack
	
	# If SHA-1
	elif algorithm == "sha1":
		# Set attack decorator to machete_sha1
		attack = machete_sha1.crack
		
	# If SHA-256
	elif algorithm == "sha256":
		# Set attack decorator to machete_sha256
		attack = machete_sha256.crack
		
	# If SHA-512
	elif algorithm == "sha512":
		# Set attack decorator to machete_sha512
		attack = machete_sha512.crack
		
	# If DSA
	elif algorithm == "dsa":
		# Set attack decorator to machete_dsa
		attack = machete_dsa.crack
		
	# If Whirlpool
	elif algorithm == "whirlpool":
		# Set attack decorator to machete_whirlpool
		attack = machete_whirlpool
		
	# Return attack
	return attack
		
