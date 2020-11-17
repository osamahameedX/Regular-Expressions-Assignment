# SI 206
# HW6 - Regular Expressions
# Name:  Elaina Tiller


import re
import os
import unittest


def read_file(filename):
    """ Return a list of the lines in the file with the passed filename """

    # Open the file and get the file object
    source_dir = os.path.dirname("C:\\Users\\Muhammad Usama\\Fiverr Projects\\p4\\")  # <-- directory name
    full_path = os.path.join(source_dir, filename)
    try:
        file = open(full_path, 'r', encoding='utf-8')
        #       # Read the lines from the file object into a list
        # lines = file.readlines()
        lines = file.read()
        lines = " ".join(lines.split())

        #         # return the list of lines
        file.close()
    except IOError:
        print("File not found or path is incorrect")

    return lines


def count_char(string_list, char):
    pattern = r'''(?ix)           # ignore case, verbose mode
              \b{letter}      # start with letter
              \w*             # zero or more additional word characters
              [^{letter}\W]\b # ends with a word character that isn't letter
              |               #    OR
              \b # does not start with a non-word character or letter
              \w*             # zero or more additional word characters
              {letter}\b      # ends with letter
              '''.format(letter=char)
    char = re.findall(pattern, string_list)
    return char


def find_dates(string_list):
    regex = re.findall(r'(?:\d{1,2}[- \/.])(?:\d{1,2}[- \/.])(?:\d{2,4})', str(string_list))
    date = []
    for s in regex:
        date.append(s)
    return date


def find_time(string_list):
    time = re.findall(r'\s(\d{2}\:\d{2}\s?(?:am|pm))', string_list)
    return time


def find_urls(string_list):
    """ Return a list of valid urls in the list of strings """

    # loop through each line of the string list

    # find all the domains that match the regular expression in each line

    # loop through the found domains
    urls = re.findall(r"(http[]?://|http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)",
                      string_list)

    # return the list of domains
    return urls


# Implement your own tests.    
class TestAllMethods(unittest.TestCase):

    def test_find_times(self):
        # read the lines from the file into a list of strings
        string_list = read_file('alice_in_wonderland.txt')
        time_list = find_time(string_list)
        self.assertEqual(len(time_list),5)

    def test_find_urls(self):
        # read the lines from the file into a list of strings
        string_list = read_file('alice_in_wonderland.txt')
        domain_list = find_urls(string_list)
        print(domain_list)
        self.assertEqual(len(domain_list),5)

    def test_find_dates(self):
        string_list = read_file('alice_in_wonderland.txt')
        dates_list = find_dates(string_list)
        self.assertEqual(len(dates_list),7)

       
    def test_count_char(self):
        string_list = read_file('alice_in_wonderland.txt')
        char_list = count_char(string_list, 'B')
        self.assertEqual(len(char_list),1099)
        pass




def main():
	# Use main to test your function. 
    # Run unit tests, but feel free to run any additional functions you need
	unittest.main(verbosity = 2)

if __name__ == "__main__":
	main()
    
    
    
    
    
    

