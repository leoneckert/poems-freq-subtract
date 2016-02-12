import sys
import math
import os


# YOU RUN THIS LIKE THIS:
# python swap_most_frequent_words.py input_texts/frost.txt input_texts/sea_rose.txt


replace_factor = 0.4  
# from 0 to 1, 0 doesnt replce anywords, 1 replaces all words from of the text 
# with fewer words and the same amount of the text with more words

# retrieve information to specify an output-file-path 
# to store both the final output and in the two input files
filename1 = sys.argv[1].split(".")[0].split("/")[1]
filename2 = sys.argv[2].split(".")[0].split("/")[1]

outputPath = "outputs_replace_frequent/" + filename1 + "_and_" + filename2
if not os.path.exists(outputPath):
    os.makedirs(outputPath)




# LET'S SORT the words of TEXT 1 by frequency:
word_freq1 = {}
# here is the text:
text1 = open(sys.argv[1])

for line in text1:
	line = line.strip() 
	words = line.split()
	for w in words:
		if w != '':	
			if w in word_freq1:
				word_freq1[w] = word_freq1[w]+1
			else:
				word_freq1[w] = 1

# word_freq1 is  adictairy with an entry for each word as well as a number of the amount of times it appears
# now we use the function below to make an array with the words in order
sortedArray1 = []
lis = sorted(word_freq1.items(), key = lambda x:x[1], reverse = True)
for word,freq in lis:
	sortedArray1.append(word)

# ----------
# HERE EXACTLY THE SAME WITH TEXT 2, I'll leave the comments away:

word_freq2 = {}
text2 = open(sys.argv[2])
for line in text2:
	line = line.strip()
	words = line.split()
	for w in sorted(words):
		if w != '':	
			if w in word_freq2:
				word_freq2[w] = word_freq2[w]+1
			else:
				word_freq2[w] = 1
sortedArray2 = []
lis = sorted(word_freq2.items(), key = lambda x:x[1], reverse = True)
for word,freq in lis:
	sortedArray2.append(word)

# ----------
# LETS CONTINUE
# ----------
# we want to swap the most frequent word of each text with the 
# most frequent word from the other and the second frequent and so on.
# we can only do that as long as one of the two array we created above "runs out"
# let's check which one is the shorter on of the two:
short_length = 0
if len(sortedArray2) > len(sortedArray1):
	short_length = len(sortedArray1)
else:
	short_length = len(sortedArray2)
# ----

# now lets print the first text with the replacement:
# here is the text again (do i always need to open that again?)
first_text = open(sys.argv[1])

# initialise writer to write to an output file:
writer = open(outputPath + "/out_1.txt", 'w')

for line in first_text:
	line = line.strip()
	words = line.split()
	newLine = ""
	for w in words:
		# we only go as deep into the frequency array as specified way on top of this script:
		for i in range (int(math.floor(short_length * replace_factor))):
			# if the currently inspected word is in that section of the array
			if w == sortedArray1[i]:
				# then we replace it with the equivalent word of the other array:			
				w = sortedArray2[i]
		# and add it to the current line of the output poem
		newLine = newLine + " " + w
	# finally we both print the current line and write it to our ouput file, too
	print newLine
	writer.write(newLine + "\n")

# save the output file:
writer.close() 

# ------
# lets print a divider
print "-"*40

# same for the second text
second_text = open(sys.argv[2])
writer = open(outputPath + "/out_2.txt", 'w')

for line in second_text:
	line = line.strip()
	words = line.split()
	newLine = ""
	for w in words:
		for i in range (int(math.floor(short_length * replace_factor))):
			if w == sortedArray2[i]:	
				w = sortedArray1[i]
		newLine = newLine + " " + w
	print newLine
	writer.write(newLine + "\n")
writer.close() 



# For documentation reasons, we also make copies of the two input files 
# and put them into the same folder as the output files

writer_input1 = open(outputPath + "/" + filename1 + "_input1.txt", 'w')
input1 = open(sys.argv[1])
for line in input1:
	writer_input1.write(line)
writer_input1.close()

writer_input2 = open(outputPath + "/" + filename2 + "_input2.txt", 'w')
input2 = open(sys.argv[2])
for line in input2:
	writer_input2.write(line)
writer_input2.close()

