from __future__ import division

from collections import defaultdict
from itertools import combinations

from locality_sensitive_hashing.utility import compress_hash, compare_signatures
from locality_sensitive_hashing.shingling import SHINGLE_BITS_REPRESENTATION


def _calculate_factors(n):
    factors = []

    for i in range(1, n + 1):
        if n % 1 == 0:
            factors.append(i)
    return factors


class LSH:
    def __init__(self, signatures, threshold):
        self.signatures = signatures
        self.threshold = threshold

        self.candidate_pairs = self._create_candidate_pairs()
        self.similar_pairs = self._check_threshold()

    def _create_candidate_pairs(self):

        band, r = self._calculate_bands_and_rows()

        print(band, r)

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

        bucket_array = [defaultdict(list)] * band

        for doc_id, signature in self.signatures.items():

            for b in range(band):
                # Python can calculate hash for multiple numbers from tuples.
                bucket = compress_hash(tuple(signature[b * r:(b + 1) * r]), SHINGLE_BITS_REPRESENTATION)
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

        n = len(self.signatures)
        factors_b = _calculate_factors(n)  # take each factor as b and calculate r and t

        minimum_threshold = 1  # Initialize distance to a large value
        current_b = factors_b[0]

        for b in factors_b:
            r = n / b

            t = (1.0 / b) ** (1.0 / r)

            if abs(t - self.threshold) < minimum_threshold:
                minimum_threshold = abs(t - self.threshold)
                current_b = b

        b = current_b
        r = int(n / b)

        print("The values for b is {} and r is {}. The best approximation for threshold {} is t = {}"
              .format(b, r, self.threshold, (1.0 / b) ** (1.0 / r)))

        return b, r

    def _check_threshold(self):
        similar_pairs = {}
        for can1, can2 in self.candidate_pairs:
            if compare_signatures(self.signatures[can1], self.signatures[can2]) >= self.threshold:
                similar_pairs[can1] = can2
                similar_pairs[can2] = can1

        return similar_pairs
