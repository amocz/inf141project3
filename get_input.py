from nltk.corpus import stopwords

STOPWORDS = set(stopwords.words('english'))


class query:

    def __init__(self):
        self.input = ""
        self.trimmed_list = []

    def get_query(self):
        self.input = raw_input("Search here: ")    
        return self.input

    def trim_query(self):
        user_input = self.get_query().lower().split()
        self.trimmed_list = [i for i in user_input if i not in STOPWORDS]
        return self.trimmed_list
   
##if __name__ == "__main__":
##    q = query()
