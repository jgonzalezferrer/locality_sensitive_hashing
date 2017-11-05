from nose.tools import assert_equal

from locality_sensitive_hashing.shingling import Shingling
from locality_sensitive_hashing.minhashing import MinHashing
from locality_sensitive_hashing.utility import compare_sets, compare_signatures


def test_strings_shingling_similarity():
    editorial = "editorial"
    factorial = "factorial"
    expected_values = [(1, 0.6), (5, 0.25), (9, 0.0)]

    for k, expected in expected_values:
        editorial_shingle = Shingling(editorial, k)
        factorial_shingle = Shingling(factorial, k)
        jaccard_similarity = compare_sets(editorial_shingle.shingles, factorial_shingle.shingles)

        assert_equal(jaccard_similarity, expected, "Jaccard similarity of '{}' and '{}' failed. "
                                                   "Expected: {}, got: {}. "
                     .format(editorial, factorial, expected, jaccard_similarity))


def test_minhash_similarity():
    editorial = "editorial"
    factorial = "factorial"

    editorial_shingle = Shingling(editorial, 5)
    factorial_shingle = Shingling(factorial, 5)

    editorial_minhashing = MinHashing(editorial_shingle.shingles, 100)
    factorial_minhashing = MinHashing(factorial_shingle.shingles, 100)

    print(compare_signatures(editorial_minhashing.signature, factorial_minhashing.signature))


if __name__ == "__main__":
    test_minhash_similarity()