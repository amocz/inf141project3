## Project 3
## Erin Cheong, Zachary Little, Chris Zhao

import json
from bs4 import BeautifulSoup
from collections import defaultdict
from nltk.tokenize import RegexpTokenizer
import lxml


class Milestone_1:

        def __init__(self):
                self.file_count = 0
                self.list_of_keys = []
                self.word_dict = {}
                self.tokenized_files = {}

        def read_bookkeeping(self):
                '''reads the bookkeeping.txt and loads it into a dict'''
                file_1 = open("bookkeeping.json")
                json_str = file_1.read()
                json_dict = json.loads(json_str)
                for j in json_dict:
                        self.file_count = self.file_count + 1
                        self.list_of_keys.append(j)

        def tokenizer(self, file_path):
                '''Tokenizes input HTML files and returns a word_dict dictionary
                with each word as the key and its frequency in which it appears
                on the HTML webpage as the values
                '''
                token = RegexpTokenizer(pattern="\\w+")
                html_file = open(file_path).read()
                all_text = BeautifulSoup(html_file, "lxml").get_text()
        
                for word in token.tokenize(all_text):
                        if word.lower() in self.word_dict.keys():
                                self.word_dict[word.lower()] += 1
                        else:
                                self.word_dict[word.lower()] = 1
                return self.word_dict

        def tokenize_files(self):
                '''Goes through and calls each HTML folder/file path with
                tokenizer() and returns a dict of dicts with the key being
                the file path and the values are the word_dict dictionary
                '''                
                for path in self.list_of_keys:
                        self.tokenized_files[path] = self.tokenizer(path)
                        print("Tokenizing: ", path)
                        ## All the 'u' in front of the path just represents that
                        ##    the output from BeautifulSoup is in Unicode.
                        ##    Nothing bad about this. Don't worry.
                return self.tokenized_files


if __name__ == "__main__":
        meh = Milestone_1()
        meh.read_bookkeeping()
        meh.tokenize_files()

