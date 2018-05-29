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


def search(search_query, database, url_dict):
    #ranked_list = []
    score_dict = {}
    docID_dict = {}
    temp_dict = {}
    sorted_dict = {}
    valid_records = _find_valid_documents(search_query, database)
    for key, record in valid_records:
        #for key in record:
        #    print(key)
        record = record.encode("UTF-8")
        record = literal_eval(record)
        #for docID, tfidf in record:
        #    print(docID)
        for x, y in record.items():
            if x not in docID_dict:
                temp_dict = dict([(key, y)])
                docID_dict[x] = temp_dict
            else:
                temp_dict = dict([(key, y)])
                docID_dict[x].update(temp_dict)
    for key, value in docID_dict.items():
        score = 0
        for i in value:
            score = score + value[i]
        score_dict[key] = score
        sorted_dict = sorted(score_dict, key=score_dict.get, reverse=True)[:10]
    url_list = get_links(sorted_dict, url_dict)
    return url_list

def get_links(sorted_dict, url_dict):
    url_list = []
    for link in sorted_dict:
        url_list.append(url_dict[link].encode("UTF-8"))
    return url_list

'''
Basically now we need to sum the tf-idf scores for each term in the search query for each document
according to https://piazza.com/class/jfk8ckl0nbujw?cid=517 "The "default" method would just be summing tf-idf scores 
for each term in the search query for each document."

 These are my thoughts so far: 

steps: 
1) find the documents which contain most of the terms
2) look at each term in the search query
3) sum the tf-idf scores for each term contained in the document
4) rank the documents by the total tf-idf and then create the return set

search query: people get info

results: 
(u'get', u"{'13/481': 10.0, '13/480': 2.5}")
(u'information', u"{'4/214': 5.0}")
(u'forget', u"{'13/481': 5.0}")
(u'people', u"{'4/214': 1.6666666666666667, '13/481': 5.0, '13/480': 1.6666666666666667}")
(u'bioinformatics', u"{'13/480': 10.0}")

doc 13/481 - get(10.0), forget(5.0), people(5.0) - Sum(20)
doc 13/480 - get(2.5), people(1.667), bioinformatics(10) - Sum(14.17)
doc  4/214 - information(5.0), people(1.667) - Sum(6.667)

{"13/481" : 20, "13/480" : 14.17, "4/214" : 6.667} - sorted

Search for "people get info" returned 3 results: 
link for 13/481 from bookkeeping.json
link for 13/480 from bookkeeping.json
link for 4/214 from bookkeeping.json
'''
