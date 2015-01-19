#########################################################
##  CS 4750 (Fall 2014), Assignment #1, Question #1    ##
##   Script File Name: tcomp1.py                       ##
##       Student Name: Michael Singleton               ##
##         Login Name: mnjs51                          ##
##              MUN #: 201103561                       ##
#########################################################

import sys, getopt, string

def sim(dict1, dict2):
	diff = 0.0
	dict2_copy = dict2
	for key in dict1:
		if key in dict2:
			diff += abs(dict1[key] - dict2[key])
			del dict2_copy[key]
		else:
			diff += dict1[key]
	for key in dict2_copy:
		diff += dict2_copy[key]
	return 1.0 - (diff/2.0)


def file_to_word_list(filepath): # creates an ngram frequency table from a file
	read_file = open(filepath)
	file_as_string = read_file.read()
	file_as_string = file_as_string.translate(string.maketrans("",""), string.punctuation)
	word_list = file_as_string.split()
	read_file.close()
	return word_list

def word_list_to_ngram_dict(word_list, n):
	ngram_dict = {}
	num_ngrams = 0.0
	
	for word in word_list:
		i = 0
		while i <= len(word)-n:
			ngram = word[i:i+n]
			if ngram in ngram_dict:
				ngram_dict[ngram] += 1.0
			else:
				ngram_dict.setdefault(ngram, 1.0)
			num_ngrams += 1.0
			i += 1	
	for key in ngram_dict:
		ngram_dict[key] /= num_ngrams
	return ngram_dict

# main method
def main(argv):
	# START COMMAND LINE ARGUMENT HANDLER
	master_file = ''
	n = 0
	comp_files = []
	
	try:
		opts, args = getopt.getopt(argv,"hm:n:c:",["masterfile=", "n=", "compfiles="])
	# Prints usage if the format is wrong
	except getopt.GetoptError:
		print 'tcomp1.py --masterfile=<masterfile> --n=<n> --compfiles=<\'compfile1 compfile2 compfile3 etc\' (must have at least 2)>'
		sys.exit(2)
	# Decodes the arguments
	for opt, arg in opts:
		if opt == '-h':
			print 'tcomp1.py --masterfile=<masterfile> --n=<n> --compfiles=<\'compfile1 compfile2 compfile3 etc\' (must have at least 2)>'
			sys.exit()
		elif opt in ("--masterfile", '-m'):
			master_file = arg
		elif opt in ("--n", '-n'):
			n = int(arg)
		elif opt in ("--compfiles", '-c'):
			comp_files = arg.split()
	# END COMMAND LINE ARGUMENT HANDLER
	
	master_ngram_dict = word_list_to_ngram_dict(file_to_word_list(master_file), n)
	most_similar_name = ''
	most_similar_score = 0.0
	
	for comp_file in comp_files:
		comp_ngram_dict = word_list_to_ngram_dict(file_to_word_list(comp_file), n)
		sim_score = sim(master_ngram_dict, comp_ngram_dict)
		print 'Sim(' + master_file + ', ' + comp_file + ') = ' + '%.3f' % sim_score
		if most_similar_name != '':
			if sim_score > most_similar_score:
				most_similar_score = sim_score
				most_similar_name = comp_file
		else:
			most_similar_name = comp_file
			most_similar_score = sim_score
	print 'File ' + most_similar_name + ' is the most similar to file ' + master_file
	
if __name__ == "__main__":
	main(sys.argv[1:])
