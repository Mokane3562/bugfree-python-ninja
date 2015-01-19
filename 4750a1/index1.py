#########################################################
##  CS 4750 (Fall 2014), Assignment #1, Question #3    ##
##   Script File Name: index.py                        ##
##       Student Name: Michael Singleton               ##
##         Login Name: mnjs51                          ##
##              MUN #: 201103561                       ##
#########################################################

import sys, getopt, string

def file_to_word_list(filepath): # creates an ngram frequency table from a file
	read_file = open(filepath)
	file_as_string = read_file.read()
	file_as_string = file_as_string.translate(string.maketrans("",""), string.punctuation)
	word_list = file_as_string.split()
	return word_list

# main method
def main(argv):
	# START COMMAND LINE ARGUMENT HANDLER
	master_file = ''
	n = 0
	comp_files = []
	
	try:
		opts, args = getopt.getopt(argv,"h",["ignored=", "text=", "index="])
	# Prints usage if the format is wrong
	except getopt.GetoptError:
		print 'index.py --ignored=<ignoredfile> --text=<textfile> --index=<indexfile>'
		sys.exit(2)
	# Decodes the arguments
	for opt, arg in opts:
		if opt == '-h':
			print 'index1.py --ignored=<ignoredfile> --text=<textfile> --index=<indexfile>'
			sys.exit()
		elif opt == "--ignored":
			ignored_filepath = arg
		elif opt == "--text":
			text_filepath = arg
		elif opt == "--index":
			index_filepath = arg
	# END COMMAND LINE ARGUMENT HANDLER
	
	ignored_word_list = file_to_word_list(ignored_filepath)
	text_file = open(text_filepath)
	index_file = open(index_filepath, 'w')
	word_dict = {}
	
	line_num = 1
	for line in text_file:
		line_word_list = (line.translate(string.maketrans("",""), string.punctuation)).split()
		for word in line_word_list:
			if word not in ignored_word_list:
				try:
					word_dict[word].append(line_num)
				except KeyError:
					word_dict.setdefault(word, [line_num])
		line_num += 1
	
	for key in sorted(word_dict):
		line = key + ': '
		for num in word_dict[key]:
			line += str(num) + ' '
		print line
		index_file.write(line + '\n')
	
if __name__ == "__main__":
	main(sys.argv[1:])
