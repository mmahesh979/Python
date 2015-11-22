''' Process.py takes an input string and the returns optimum word to be played so as to maximize the scrabble 
	score given a rack of 8 words. The program returns words of minimum length 2 and a maximum length 8.
	Any numbers/special characters entered are removed. It automatically converts input to lower case.
	Usage:python scrabble.py <yourrack>	'''


# include dependencies
from itertools import combinations
import collections
import os.path
from time import time



#load_anagrams() loads th anadict.txt file. It creates anadict.txt if it is not available 
#if process.py and dictionary.txt are present in the current directory.
def load_anagrams():
	if not os.path.isfile('./anadict.txt'):								#check if anadict.txt is present
		if not os.path.isfile('./dictionary.txt'):
			print 'Dictionary not found. Please include dictionary.txt in the current directory'
			exit()
		if not os.path.isfile('./process.py'):							#check if process.py is present
			print 'file: process.py not found. Please make sure it is present in the current directory'
			exit()
		execfile('process.py')											#run process.py
	anagrams = collections.defaultdict(list)
	with open('anadict.txt', 'r') as file_handle:						#open anadict.txt
		for line in file_handle:
			words = line.split()
			anagrams[tuple(words[0])] = words[1:]
	return anagrams
	

	
# the scorecard as provided
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10} 


#score_word calculates the score according to the given scorecard		 
def score_word(word):
  return sum([score[c] for c in word])									#calculate the sum
  
  

 #find_words finds words whose keys are a subset of the given rack
def find_words(board, anagrams):
    board = ''.join(sorted(board))
    target_words = []													#array to store matches
    for word_length in range(2, len(board) + 1):
        for combination in combinations(board, word_length):
            if combination in anagrams:
                target_words += anagrams[combination]					#add matches to array
    return target_words													#return the array


	
if __name__ == "__main__":
	import sys
	if len(sys.argv) == 2:
		rack = sys.argv[1].lower().strip()								#convert input to lower case
		rack = ''.join([i for i in rack if i.isalpha()])				#remove any input that is not an alphabet
	else:
		print """Invalid Command\t\tUsage:python scrabble.py <yourrack>
				eg:python scrabble.py aeiouqen"""
		exit()
	t = time()															#start timer
	anagrams = load_anagrams()
	target_words = set(find_words(rack, anagrams))
	scored = [(score_word(word), word) for word in target_words]
	for score, word in scored:											#print the list of matches
		print "%d\t%s" % (score,word)
	if 	not scored:
		print "No words found\t Score: 0"
	else:
		print "Answer:\t"+ str(max(scored))								#return the best answer
	print "Time elapsed:", (time()-t)									#find time elapsed
	