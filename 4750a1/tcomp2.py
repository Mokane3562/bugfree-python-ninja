#########################################################
##  CS 4750 (Fall 2014), Assignment #1, Question #2    ##
##   Script File Name: tcomp2.py                       ##
##       Student Name: Michael Singleton               ##
##         Login Name: mnjs51                          ##
##              MUN #: 201103561                       ##
#########################################################
import sys, getopt, string

def sim(set1, set2):
	return 1.0 - (float(len(set1-set2)+len(set2-set1)) / float(len(set1)+len(set2)))

def file_to_word_set(filepath): # creates an ngram frequency table from a file
	read_file = open(filepath)
	file_as_string = read_file.read()
	file_as_string = file_as_string.translate(string.maketrans("",""), string.punctuation)
	word_set = set(file_as_string.split())
	read_file.close()
	return word_set

# main method
def main(argv):
	# START COMMAND LINE ARGUMENT HANDLER
	master_file = ''
	comp_files = []
	
	try:
		opts, args = getopt.getopt(argv,"hm:c:",["masterfile=", "compfiles="])
	# Prints usage if the format is wrong
	except getopt.GetoptError:
		print 'tcomp2.py --masterfile=<masterfile> --compfiles=<\'compfile1 compfile2 compfile3 etc\' (must have at least 2)>'
		sys.exit(2)
	# Decodes the arguments
	for opt, arg in opts:
		if opt == '-h':
			print 'tcomp2.py --masterfile=<masterfile> --compfiles=<\'compfile1 compfile2 compfile3 etc\' (must have at least 2)>'
			sys.exit()
		elif opt in ("--masterfile", '-m'):
			master_file = arg
		elif opt in ("--compfiles", '-c'):
			comp_files = arg.split()
	# END COMMAND LINE ARGUMENT HANDLER
	
	master_word_set = file_to_word_set(master_file)
	most_similar_name = ''
	most_similar_score = 0.0
	
	for comp_file in comp_files:
		comp_word_set = file_to_word_set(comp_file)
		sim_score = sim(master_word_set, comp_word_set)
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
