# Import modules
import os
import sys
import threading
import hashlib

# Define crack() class
class crack(threading.Thread):
	# Class: crack()
	# Purpose: Crack specified hash
	# Functions: __init__(), run()
	
	# Define __init__() function
	def __init__(self, wordlist, target_hash):
		# Function: __init__()
		# Purpose: Set variables

		# Set variables
		threading.Thread.__init__(self)
		self.wordlist = wordlist
		self.target_hash = target_hash
		
	# Define run() function
	def run(self):
		# Function: run()
		# Purpose: Attack target hash
		
		# Get length of wordlist
		list_length = len(self.wordlist)
		
		# Create base for loop
		for i in range(0, list_length):
			# Flush the buffer (Needs to be flushed each
			# time, as update() adds on to testhash, not
			# change its value)
			testhash = hashlib.sha1()
			
			# Encode current word
			encword = self.wordlist[i].encode("utf-8")
			
			# Cut the trailing \n
			encword = encword.strip()
			
			# Hash the current word
			testhash.update(encword)
			
			# Check if testhash matches target hash
			if testhash.hexdigest() == self.target_hash:
				# If match, display plaintext and exit
				print("[I] Hash cracked!")
				print("[I] Plaintext: {}".format(self.wordlist[i]))
				exit(0)
			
		# If for loop is exited without triggering the if
		# statement, plaintext has not been found
		exit(0)
