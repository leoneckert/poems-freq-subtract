import sys
import os

# YOU RUN THIS LIKE THIS:
# python subtract_two_texts.py input_texts/frost.txt input_texts/sea_rose.txt

# getting the two input files
main_text = open(sys.argv[1])
second_text = open(sys.argv[2])

# retrieve information to specify an output-file-path 
# to store both the final output and in the two input files
filename1 = sys.argv[1].split(".")[0].split("/")[1]
filename2 = sys.argv[2].split(".")[0].split("/")[1]

outputPath = "outputs_subtraction/" + filename1 + "_and_" + filename2
if not os.path.exists(outputPath):
    os.makedirs(outputPath)

# make a list with all the words from second input text
words_second_text = []

for line in second_text:
	# words = line.split(" ")
	words = line.split()
	for w in words:
		# if w != "":
		words_second_text.append(w)


# initialise writer to write to an output file:
writer = open(outputPath + "/out_1.txt", 'w')

for line in main_text:
	line = line.strip()

	words = line.split(" ")
	newLine = ""
	# go through all individual words in the current line
	for w in words:
		# if a word also appears in the second text list...
		if w in words_second_text:
			# then we take out ever instance of it from the list:
			for wo in words_second_text:
				if wo == w:
					words_second_text.remove(wo)
			# and add it to the current line of the output poem
			newLine = newLine + " " + w
	# finally we both print the current line and write it to our ouput file, too
	print newLine
	writer.write(newLine + "\n")

# save the output file:
writer.close() 


# lets print a divider
print "-"*40

# HERE WE DO EXACTLY THE SAME, JUST THE OTHER WAY ROUND, 
# NOTE WE ONLY exchange the input path in the first two lines of code here.
# i'll leave the comment out this time, because it's exactly the same
main_text = open(sys.argv[2])
second_text = open(sys.argv[1])
words_second_text = []
for line in second_text:
	words = line.split()
	for w in words:
		words_second_text.append(w)
writer = open(outputPath + "/out_2.txt", 'w')
for line in main_text:
	line = line.strip()
	words = line.split(" ")
	newLine = ""
	for w in words:
		if w in words_second_text:
			for wo in words_second_text:
				if wo == w:
					words_second_text.remove(wo)
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



