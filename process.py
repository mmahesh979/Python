''' This python code takes dictionary.txt from the current directory and generates 
	anadict.txt to be saved in the same directory. It considers words of length 2-8
	and ignores letters that have apostrophise or other special characters'''


f = open('dictionary.txt')
d = {}
lets = set('abcdefghijklmnopqrstuvwxyz\n')										#ignore special characters
for word in f:
	if len(set(word) - lets) == 0 and len(word) > 2 and len(word) < 9:			#set word length
		word = word.strip()
		key = ''.join(sorted(word))
		if key in d:
			d[key].append(word)
		else:
			d[key] = [word]
f.close()
anadict = [' '.join([key]+value) for key, value in d.iteritems()]
anadict.sort()
f = open('anadict.txt','w')														#save anadict.txt
f.write('\n'.join(anadict))
f.close()