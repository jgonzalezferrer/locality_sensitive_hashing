import random
from locality_sensitive_hashing.shingling import Shingling
class MinHashing:

    def __init__(self, hashed_singles, n):
        self.hashed_singles = hashed_singles
        self.n = n

        self.signature = self._create_signature()

    def _generate_hash_functions(self):
        random.seed(999)  # Set random seed in order to have the same hash functions for different documents,
        for i in range(self.n):
            m = random.randint(1, 100)
            c = random.randint(1, 100)
            yield lambda x, a=m, b=c: (a * x + b) % self.n  # TODO: not sure whether n or hash buckets.

    def _create_signature(self):
        signature = [None]*self.n
        for i, hash_function in enumerate(self._generate_hash_functions()):
            signature[i] = min([hash_function(x) for x in self.hashed_singles])

        return signature


if __name__ == "__main__":

    text = "The hash, then, is only stable if you don't restart the Python process or set PYTHONHASHSEED to a fixed decimal number"

    editorial = "editorial"
    factorial = "factorial"

    editorial_shingle = Shingling(editorial, 5)
    factorial_shingle = Shingling(factorial, 5)

    min1 = MinHashing(editorial_shingle.shingles, 100)
    min2 = MinHashing(factorial_shingle.shingles, 100)

    print(min1.signature)
    print(min2.signature)
    print(len([i for i, j in zip(min1.signature, min2.signature) if i == j])/len(a.signature))

