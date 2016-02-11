import sys

# make array of all words in first text
text1 = open(sys.argv[1])
all_words1 = []
for line in text1:
	line = line.strip()
	words = line.split()
	for w in sorted(words):
		if w != '':		
			all_words1.append(w)

# make array of all words in second text
text2 = open(sys.argv[2])
all_words2 = []
for line in text2:
	line = line.strip()
	words = line.split()
	for w in sorted(words):
		if w != '':	
			all_words2.append(w)



# to print a nice table:
row_format ="{:>20}" * 2
print row_format.format("text1", "text2")
print row_format.format("---", "---")
# check if botha arrays have the same amout of words
print row_format.format(str(len(all_words1)) + " words", str(len(all_words2)) + " words")
print row_format.format("---", "---")
# then, in order, print the words of each text, one by one, next to each other
for w1, w2 in zip(sorted(all_words1), sorted(all_words2)):
    print row_format.format(w1, w2)
