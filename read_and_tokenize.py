## Project 3
## Erin Cheong, Zachary Little, Chris Zhao

import json
import lxml
import build_index
import get_input
from bs4 import BeautifulSoup
from collections import defaultdict, Iterable
from nltk.tokenize import RegexpTokenizer
from pymongo import MongoClient

file_limit = 5

class Milestone_1:

        def __init__(self):
                self.file_count = 0
                self.list_of_keys = []
                self.tokenized_files = {}

        def read_bookkeeping(self):
                '''reads the bookkeeping.txt and loads it into a dict'''
                file_1 = open("bookkeeping.json")
                json_str = file_1.read()
                json_dict = json.loads(json_str)
                for j in json_dict:
                        self.file_count = self.file_count + 1
                        self.list_of_keys.append(j.encode("utf-8"))

        def tokenizer(self, file_path):
                '''Tokenizes input HTML files and returns a word_dict dictionary
                with each word as the key and its frequency in which it appears
                on the HTML webpage as the values
                '''
                token = RegexpTokenizer(pattern=r'[a-zA-Z0-9]+')
                html_file = open(file_path).read()
                all_text = BeautifulSoup(html_file, "lxml")
                #tag.decompose() for tag in all_text
                for script in all_text(["script", "style"]):
                        script.extract()
                '''
                for tag in all_text:
                        for attribute in ["class", "id", "name", "style"]:
                                del tag[attribute]
                '''
                all_text = all_text.get_text().encode("utf-8")

                _word_dict = {}
                for word in token.tokenize(all_text):
                        if word.lower() in _word_dict.keys():
                                _word_dict[word.lower()] += 1
                        else:
                                _word_dict[word.lower()] = 1
                return _word_dict

        def tokenize_files(self):
                '''Goes through and calls each HTML folder/file path with
                tokenizer() and returns a dict of dicts with the key being
                the file path and the values are the word_dict dictionary

                for path in self.list_of_keys runs through all 37k items and is too large for testing

                for path in self.list_of_keys[:15] will allow me to reduce index size of testing
                '''
                count = 0
                for path in self.list_of_keys[:file_limit]:
                        if path == "39/373" or path =="35/269":
                                continue
                        self.tokenized_files[path] = self.tokenizer(path)
                        count += 1
                        print("Tokenizing: " + path + "\t" + str(count) + "/" + str(driver.file_count))
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
        print("Total file count: " + str(driver.file_count))
        #print(driver.list_of_keys)
        dict_of_dicts = driver.tokenize_files()

        #print(dict_of_dicts.values()) # this contain the url as a key and then the word and word count as key value pairs

        dict_of_token_frequency = {} # after construction, this contains the word as a key and the url:tf as a kv pair
        for url in dict_of_dicts:
            for word in dict_of_dicts[url]:
                if word not in dict_of_token_frequency:
                    dict_of_token_frequency[word] = {url:dict_of_dicts[url][word]}
                else:
                    dict_of_token_frequency[word].update({url:dict_of_dicts[url][word]})
        #print(dict_of_token_frequency)

        index_builder = build_index.IndexBuilder()
        final_dict = index_builder.build_inverted_index(dict_of_token_frequency, file_limit)
        print(type(final_dict))

        final_dict = {k: unicode(v).encode("utf-8") for k,v in final_dict.iteritems()}
        record1 = my_database.inverted_index_table.insert_one(final_dict)

        cursor = my_collection.find()
        '''
        for record in cursor:
                print(record)
                print("\n")
        '''

        query = get_input.query()
        a = query.trim_query()
        print(a)
        
