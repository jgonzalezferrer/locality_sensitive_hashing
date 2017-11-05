from nose.tools import assert_equal

from locality_sensitive_hashing.shingling import Shingling
from locality_sensitive_hashing.compare import Compare


def test_strings_similarity():
    editorial = "editorial"
    factorial = "factorial"
    expected_values = [(1, 0.6), (5, 0.25), (9, 0.0)]

    for k, expected in expected_values:
        editorial_shingle = Shingling(editorial, k)
        factorial_shingle = Shingling(factorial, k)
        jaccard_similarity = Compare.compare_sets(editorial_shingle.shingles, factorial_shingle.shingles)

        assert_equal(jaccard_similarity, expected, "Jaccard similarity of '{}' and '{}' failed. Expected: {}, actual: "
                                                   "{} "
                     .format(editorial, factorial, expected, jaccard_similarity))