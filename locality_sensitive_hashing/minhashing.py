from locality_sensitive_hashing.utility import generate_hash_functions


class MinHashing:
    """
        Class for calculating minhash of given shingles
    """
    def __init__(self, hashed_singles, n):
        """

        :param hashed_singles:
        :param n:
        """
        self.hashed_singles = hashed_singles
        self.n = n

        self.signature = self._create_signature()

    def _create_signature(self):
        signature = [None] * self.n
        for i, hash_function in enumerate(generate_hash_functions(self.n)):
            signature[i] = min([hash_function(x) for x in self.hashed_singles])

        return signature
