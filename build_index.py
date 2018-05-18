from collections import defaultdict


class IndexBuilder:

    def __init__(self):
        self.inverted_index = {}

    def build_inverted_index(self, dict_of_wordcount_dict):
        print('called build_inverted_index')