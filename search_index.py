from ast import literal_eval

def _find_valid_documents(search_query, database):
    valid_records = set()
    cursor = database.find()
    for document in cursor:
        for key, value in document.items():
            for term in search_query:
                if term in key.encode('UTF-8') or term == key.encode('UTF-8'):
                    valid_records.add((key, value))

    return valid_records


def search(search_query, database):
    ranked_list = []
    valid_records = _find_valid_documents(search_query, database)

    for record in valid_records:
        print(record)
'''
Basically now we need to sum the tf-idf scores for each term in the search query for each document
search query: people get info

results: 
(u'get', u"{'13/481': 10.0, '13/480': 2.5}")
(u'information', u"{'4/214': 5.0}")
(u'forget', u"{'13/481': 5.0}")
(u'people', u"{'4/214': 1.6666666666666667, '13/481': 5.0, '13/480': 1.6666666666666667}")
(u'bioinformatics', u"{'13/480': 10.0}")

steps: 
'''



'''
   for search_term, key, documents_and_tfidf in valid_records:
        doc_dict = literal_eval(documents_and_tfidf.encode('UTF-8'))

        summed_tfidf = sum(doc_dict.values())

        print(summed_tfidf)

        ranked_list.append((valid_records, summed_tfidf))

    print ranked_list
'''