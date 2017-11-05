class Shingling:

    def __init__(self, doc, k):
        # TODO: preprocessing of documents
        # Questions:
        # 1) What to do with \t and \n characters? (I suggest to convert them to whitespace).
        # 2) Multiple consecutive white-spaces -> single whitespace
        self.doc = doc
        self.k = k
        self.shingles = set()

        self._create_shingles()

    def _create_shingles(self):
        characters = list(self.doc)  # split document into single characters
        str_shingles = ["".join(characters[i:i+self.k]) for i in range(len(characters)-self.k+1)]
        hash_shingles = [hash(shingle) for shingle in str_shingles]
        self.shingles = set(hash_shingles)  # unique hash singles