from locality_sensitive_hashing.utility import compress_hash

SHINGLE_BITS_REPRESENTATION = 32


class Shingling:
    """

    """
    def __init__(self, doc, k):
        """

        :param doc:
        :param k:
        """
        # TODO: preprocessing of documents
        '''
        Questions:
        1) What to do with \t and \n characters? (I suggest to convert them to whitespace).
        2) Multiple consecutive white-spaces -> single whitespace
        '''
        self.doc = doc
        self.k = k
        self.shingles = set()

        self._create_shingles()

    def _create_shingles(self):
        """

        :return:
        """
        characters = list(self.doc)  # split document into single characters
        str_shingles = ["".join(characters[i:i+self.k]) for i in range(len(characters)-self.k+1)]
        hash_shingles = [compress_hash(shingle, SHINGLE_BITS_REPRESENTATION) for shingle in str_shingles]
        self.shingles = set(hash_shingles)  # unique hash singles
