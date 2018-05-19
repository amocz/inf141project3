from collections import defaultdict
from collections import Counter


class IndexBuilder:

    def __init__(self):
        self.inverted_index = {}

    def build_inverted_index(self, dict_of_wordcount_dict):
        print('called build_inverted_index')
        '''
        calculate tf for all tokens
        Counter is basically a subclass of dict. We can still do everything we'd normally do with dict.
        '''
        tf = Counter({})
        for i in dict_of_wordcount_dict:
                tf = tf + Counter(dict_of_wordcount_dict[i])
        print(tf.items())