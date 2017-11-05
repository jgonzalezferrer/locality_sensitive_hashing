from nose.tools import assert_equal, assert_almost_equal

from locality_sensitive_hashing.shingling import Shingling
from locality_sensitive_hashing.minhashing import MinHashing
from locality_sensitive_hashing.utility import compare_sets, compare_signatures


def test_strings_shingling_similarity():
    editorial = "The dog is running"
    factorial = "The cat is running"
    expected_values = [(1, 0.6), (5, 0.25), (9, 0.0)]

    for k, expected in expected_values:
        editorial_shingle = Shingling(editorial, k)
        factorial_shingle = Shingling(factorial, k)
        jaccard_similarity = compare_sets(editorial_shingle.shingles, factorial_shingle.shingles)

        assert_equal(jaccard_similarity, expected, "Jaccard similarity of '{}' and '{}' failed. "
                                                   "Expected: {}, got: {}. "
                     .format(editorial, factorial, expected, jaccard_similarity))


def test_minhash_similarity():
    str1 = "editorial"
    str2 = "factorial"

    str1_shingle = Shingling(str1, 5)
    str2_shingle = Shingling(str2, 5)

    str1_minhashing = MinHashing(str1_shingle.shingles, 10000)
    str2_minhashing = MinHashing(str2_shingle.shingles, 10000)

    assert_almost_equal(compare_signatures(str1_minhashing.signature, str2_minhashing.signature), 0.25, 1)


if __name__ == "__main__":
    test_minhash_similarity()