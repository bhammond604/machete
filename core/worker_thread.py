# Import required modules
import os
import sys
import threading
import hashlib

# Define the crack() function
def crack(wordlist, cracker, target_hash):
	# Function: crack()
	# Purpose: Crack the hash
	
	# Build a for loop to iterate through the wordlist
	for word in wordlist:		
		# Determine if the word matches the target hash
		if hashlib.md5(bytes(word.encode("utf-8").strip())).hexdigest() == target_hash:
			# Display the found message
			print("[I] Plaintext Found: {}".format(word))
	
