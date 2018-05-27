from collections import defaultdict
from collections import Counter

#def count_

class IndexBuilder:

    def __init__(self):
        self.inverted_index = {}

    def build_inverted_index(self, dict_of_token_frequency, number_of_documents):
        '''
        calculate tf for all tokens
        Counter is basically a subclass of dict. We can still do everything we'd normally do with dict.
        '''
        for token, file_and_tf_dict in dict_of_token_frequency.items():
            _documents_with_token = len(file_and_tf_dict.keys())
            _inverse_document_frequency =  float(number_of_documents) / _documents_with_token
            for url, _token_frequency in file_and_tf_dict.items():
                _tf_idf = _token_frequency * _inverse_document_frequency
                file_and_tf_dict[url] = _tf_idf

        #print(dict_of_token_frequency.items())
        
        with open('index_file.txt', 'w') as out_file:
            for token, file_and_tf_dict in sorted(dict_of_token_frequency.items()):
                out_file.write(str(token) + str(file_and_tf_dict))
                out_file.write("\n")
        
        print('Index wrote to index_file.txt')
        print("Total number of unique token: " + str(len(dict_of_token_frequency)))
        #print(type(dict_of_token_frequency))
        return dict_of_token_frequency
        # tf = Counter({})
        # for i in dict_of_wordcount_dict:
        #         tf = tf + Counter(dict_of_wordcount_dict[i])
        # print(tf.items())
