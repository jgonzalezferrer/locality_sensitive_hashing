import random


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

    def _generate_hash_functions(self):
        random.seed(999)  # Set random seed in order to have the same hash functions for different documents,
        for i in range(self.n):
            m = random.randint(1, 100)
            c = random.randint(1, 100)
            yield lambda x, a=m, b=c: (a * x + b) % len(self.hashed_singles)  # TODO: not sure whether n or hash buckets.

    def _create_signature(self):
        signature = [None] * self.n
        for i, hash_function in enumerate(self._generate_hash_functions()):
            signature[i] = min([hash_function(x) for x in self.hashed_singles])

        return signature
