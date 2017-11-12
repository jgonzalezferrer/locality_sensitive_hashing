import random


def compare_sets(set1, set2):
    """
    Compute real Jaccard similarity of 2 sets. Not applicable for large sets, just for benchmarking
    the implementation on smaller sets to verify the correctness of implementation.
    :param set1:
    :param set2:
    :return:
    """
    set_intersection = set1.intersection(set2)
    set_union = set1.union(set2)

    jaccard_similarity = len(set_intersection) / len(set_union)
    return jaccard_similarity


def compare_signatures(sig1, sig2):
    assert len(sig1) == len(sig2)
    return len([i for i, j in zip(sig1, sig2) if i == j]) / len(sig1)


def compress_hash(string, n_bits):
    # In addition to this, you can use `hashed_value & 0xffffffff` for converting to 8-bits
    return hash(string) % (2**n_bits-1)


def generate_hash_functions(n, seed=777, max_value=2**32-1, prime_number=2**61-1):
    """
    Algorithm extracted from: ttps://en.wikipedia.org/wiki/Universal_hashing#Hashing_integers

    :param n:
    :param seed:
    :param max_value:
    :param prime_number:
    :return:
    """
    assert max_value < prime_number
    random.seed(seed)  # Set random seed in order to create the same hash functions.
    for i in range(n):
        _a = random.randint(1, max_value-1)
        _b = random.randint(1, max_value-1)
        _c = prime_number
        yield lambda x, a=_a, b=_b, c=_c: ((a * x + b) % c) % max_value
