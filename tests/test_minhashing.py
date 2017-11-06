from nose.tools import assert_almost_equal

from locality_sensitive_hashing.shingling import Shingling
from locality_sensitive_hashing.minhashing import MinHashing

from locality_sensitive_hashing.utility import compare_signatures


def test_minhash_similarity():
    str1 = "editorial"
    str2 = "factorial"

    k = 5
    str1_shingle = Shingling(str1, k)
    str2_shingle = Shingling(str2, k)

    n = 10000
    str1_minhashing = MinHashing(str1_shingle.shingles, n)
    str2_minhashing = MinHashing(str2_shingle.shingles, n)

    assert_almost_equal(compare_signatures(str1_minhashing.signature, str2_minhashing.signature), 0.25, 1)