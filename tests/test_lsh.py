from locality_sensitive_hashing.shingling import Shingling
from locality_sensitive_hashing.minhashing import MinHashing
from locality_sensitive_hashing.lsh import LSH

from locality_sensitive_hashing.utility import compare_signatures

def test_lsh_similarity():
    str1 = "editorial"
    str2 = "factorial"
    str3 = "sensacional"

    str1_shingle = Shingling(str1, 1)
    str2_shingle = Shingling(str2, 1)
    str3_shingle = Shingling(str3, 1)

    str1_minhashing = MinHashing(str1_shingle.shingles, 10000)
    str2_minhashing = MinHashing(str2_shingle.shingles, 10000)
    str3_minhashing = MinHashing(str3_shingle.shingles, 10000)

    signatures_collection = {"doc1": str1_minhashing.signature,
                             "doc2": str2_minhashing.signature,
                             "doc3": str3_minhashing.signature}

    lsh = LSH(signatures_collection, 0.5)

    print(lsh.candidate_pairs)
    print(lsh.similar_pairs)


if __name__== '__main__':
    test_lsh_similarity()
