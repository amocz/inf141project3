## Project 3
## Erin Cheong, Zachary Little, Chris Zhao

import json
import itertools
from bs4 import BeautifulSoup
from collections import defaultdict
from nltk.tokenize import RegexpTokenizer
from nltk.stem.snowball import EnglishStemmer
import lxml


##file_0 = open("bookkeeping.json")
##json_string = file_0.read()
##json_d = json.loads(json_string)
####print(json_dict["1/1"])
##
##keys_list = ['1/351', '10/183', '10/316', '13/378', '15/365', '17/28', '17/330',
##             '19/22', '19/404', '2/46', '20/58', '21/392', '27/284', '27/332', '27/335',
##             '27/69', '30/151', '32/139', '35/149', '35/334', '35/38', '37/85', '38/381',
##             '4/191', '41/223', '42/221', '42/371', '43/239', '43/323', '43/436', '45/365',
##             '46/301', '49/191', '50/451', '51/189', '54/227', '54/264', '56/48', '61/414',
##             '61/444', '63/295', '63/481', '65/378', '66/141', '68/440', '69/263',
##             '73/348', '73/462', '74/210', '8/333']
##
##for k in keys_list:
##        for j in json_d:
##                if k == j:
##                        print(json_d[j])

class Milestone_1:

        def __init__(self):
                self.file_count = 0
                self.list_of_keys = []

        def read_bookkeeping(self):
                '''reads the bookkeeping.txt and loads it into a dict'''
                file_1 = open("bookkeeping.json")
                json_str = file_1.read()
                json_dict = json.loads(json_str)
                for j in json_dict:
                        self.file_count = self.file_count + 1
                        self.list_of_keys.append(j)


##html_parse():
##    """iterates through every HTML file in every folder in WEBPAGES_RAW folder
##    and parses it using BeautifulSoup and tokenizing it"""
##
##    
##    for i in range(len(folder)):
##            for j in range(len(folder_files)):
##                string_format(directory)
##                access(directory) -- meaning open("directory") and beautifulsoup iter


##with open("//Users//EC//Documents//CS121//Project 3//WEBPAGES_RAW//7//6") as fp:
##    soup = BeautifulSoup(fp, "lxml")

##soup = BeautifulSoup("<html>data</html>", "lxml")

##html_file = open("//Users//EC//Documents//CS121//Project 3//WEBPAGES_RAW//7//6")   
##soup = BeautifulSoup(html_file, 'html.parser')
##print(soup.prettify())

##folder_path = open("//Users//EC//Documents//CS121//Project 3//WEBPAGES_RAW")

if __name__ == "__main__":
        meh = Milestone_1()
        meh.read_bookkeeping()

