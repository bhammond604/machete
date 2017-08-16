# This module provides the main logic for cracking
# the targeted hash. It's ran as a child process, 
# and spawns threads to split the load.

# Import required module
import os
import sys
import threading
import hashlib
import core.worker_thread

# Define split_list() function
def split_list(wordlist):
	# Function: split_list()
	# Purpose: Split wordlistlist into several smaller lists for threading
	
	# Set the list size
	list_size = 10000
	
	# Split the main list into a 2D list
	for i in range(0, len(wordlist), list_size):
		yield wordlist[i:i + list_size]

# Define the main() function
def main(local_wordlist, algorithm, target_hash):
	# Function: main()
	# Purpose: Provide main workflow for the child process and spawn worker threads
	
	# Split the wordlist into smaller lists
	thread_lists = list(split_list(local_wordlist))
	
	# Using the algorithm, create a decorator
	if algorithm == "md5":
		cracker = hashlib.md5
	elif algorithm == "sha1":
		cracker = hashlib.sha1
	elif algorithm == "sha256":
		cracker = hashlib.sha256
	elif algorithm == "sha512":
		cracker = hashlib.sha512
	
	# Build a for loop to create threads
	for i in range(0, len(thread_lists)):
		# Define the thread
		new_thread = threading.Thread(target = core.worker_thread.crack, args = (thread_lists[i], cracker, target_hash))
		
		# Start the thread
		new_thread.start()
