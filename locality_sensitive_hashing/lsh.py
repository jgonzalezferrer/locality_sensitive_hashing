from collections import defaultdict

from locality_sensitive_hashing.utility import compress_hash


class LSH:

    def __init__(self, signatures, t):
        self.signatures = signatures
        self.t = t

        candidate_pairs = self._create_candidate_pairs()

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

        for doc_id, signature in self.signatures:
            for b in range(buckets):
                bucket = compress_hash(tuple(signature[b*r:(b+1)*r]))  # Python can calculate hash for multiple numbers from tuples.
                bucket_array[b][bucket].append(doc_id)

        """
        We then consider any pair that hashed to the same bucket for any
        of the hashings to be a candidate pair. We check only the candidate pairs for
        similarity
        """

        # TODO: create candidate pairs.


    def _calculate_bands_and_rows(self):
        b = 4  # TODO
        r = 3  # TODO
        return b, r
