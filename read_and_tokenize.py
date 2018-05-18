## Project 3
## Erin Cheong, Zachary Little, Chris Zhao

import json
import lxml
import build_index
from bs4 import BeautifulSoup
from collections import defaultdict, Iterable
from nltk.tokenize import RegexpTokenizer
from pymongo import MongoClient

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

                for path in self.list_of_keys runs through all 37k items and is too large for testing

                for path in self.list_of_keys[:15] will allow me to reduce index size of testing
                '''
                for path in self.list_of_keys[:15]:
                        self.tokenized_files[path] = self.tokenizer(path)
                        print("Tokenizing: " + path)
                        #print(self.tokenized_files)
                        ## All the 'u' in front of the path just represents that
                        ##    the output from BeautifulSoup is in Unicode.
                        ##    Nothing bad about this. Don't worry.
                return self.tokenized_files


if __name__ == "__main__":
        try:
            client = MongoClient()
            client = MongoClient("mongodb://localhost:27017/")
            print('Connected to MongoDB successfully!!')
        except:
            print('Could not connect to MongoDB')

        my_database = client['inverted_index_storage']
        my_collection = my_database['inverted_index_table']

        '''
        The following code can be used to delete all records from a pymongo table in order to restart
        and avoid duplicate entries
        
        my_collection.delete_many({}) or my_collection.remove({})         
        '''

        '''
        The following code can be used to check all records in a pymongo table

        cursor = my_collection.find()
        for record in cursor:
            print(record)        
        '''

        driver = Milestone_1()
        driver.read_bookkeeping()
        print(driver.file_count, driver.list_of_keys)

        dict_of_dicts = driver.tokenize_files()
        print(dict_of_dicts.items())

        '''
        The following code can be used to add a record to the pymongo table
        
        record = my_database.inverted_index_table.insert(dict_of_dicts)
        '''
        index_builder = build_index.IndexBuilder()
        index_builder.build_inverted_index(dict_of_dicts)
