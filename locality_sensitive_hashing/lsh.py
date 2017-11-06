from collections import defaultdict
from itertools import combinations
from sympy import nsolve, Symbol

from locality_sensitive_hashing.utility import compress_hash, compare_signatures
from locality_sensitive_hashing.shingling import SHINGLE_BITS_REPRESENTATION


class LSH:

    def __init__(self, signatures, t):
        self.signatures = signatures
        self.t = t

        self.candidate_pairs = self._create_candidate_pairs()
        self.similar_pairs = self._check_threshold()

    def _create_candidate_pairs(self):

        buckets, r = self._calculate_bands_and_rows()

        """
        Algorithm:

        If we have minhash signatures for the items, an effective way to choose the
        hashings is to divide the signature matrix into b bands consisting of r rows
        each.

        For each band, there is a hash function that takes vectors of r integers
        (the portion of one column within that band) and hashes them to some large
        number of buckets. We can use the same hash function for all the bands, but
        we use a separate bucket array for each band, so columns with the same vector
        in different bands will not hash to the same bucket
        :return:
        """

        bucket_array = [defaultdict(list)]*buckets

        for doc_id, signature in self.signatures.items():
            for b in range(buckets):
                bucket = compress_hash(tuple(signature[b*r:(b+1)*r]), SHINGLE_BITS_REPRESENTATION)  # Python can calculate hash for multiple numbers from tuples.
                bucket_array[b][bucket].append(doc_id)


        """
        We then consider any pair that hashed to the same bucket for any
        of the hashings to be a candidate pair. We check only the candidate pairs for
        similarity
        """

        candidate_pairs = set()

        for band in bucket_array:
            for pairs in band.values():
                if len(pairs) > 1:  # more than one element in bucket
                    for candidate_pair in combinations(pairs, 2):
                        candidate_pairs.add(candidate_pair)

        return candidate_pairs

    def _calculate_bands_and_rows(self):
        if __name__ == '__main__':
            if False:
                x = Symbol('x')
                y = Symbol('y')
                n = len(self.signatures)
                sol = nsolve([x * y / n - 1, (1 / x) ** (1 / y) / self.t - 1], [x, y], [1, 1])

                # these two values are close to the real solution
                b = sol[0]
                r = sol[1]

                # TODO: find the closest integer such as: b*r = n and (1 / x) ** (1 / y) < t.
                # Last equation because:  "If avoidance of false negatives is important,
                # you may wish to select b and r to produce a threshold lower than t"
                # QUESTION: which value should be optimize first? b or r?

        b = 4  # TODO
        r = 3  # TODO
        return b, r

    def _check_threshold(self):
        similar_pairs = []
        for can1, can2 in self.candidate_pairs:
            if compare_signatures(self.signatures[can1], self.signatures[can2]) >= self.t:
                similar_pairs.append((can1, can2))

        return similar_pairs
