from locality_sensitive_hashing.shingling import Shingling
from locality_sensitive_hashing.minhashing import MinHashing
from locality_sensitive_hashing.lsh import LSH

from locality_sensitive_hashing.utility import compare_signatures

def test_lsh_similarity():
    str1 = "editorial"
    str2 = "factorial"
    str3 = "phone number"

    k = 1
    str1_shingle = Shingling(str1, k)
    str2_shingle = Shingling(str2, k)
    str3_shingle = Shingling(str3, k)

    n = 12
    str1_minhashing = MinHashing(str1_shingle.shingles, n)
    str2_minhashing = MinHashing(str2_shingle.shingles, n)
    str3_minhashing = MinHashing(str3_shingle.shingles, n)

    signatures_collection = {"doc1": str1_minhashing.signature,
                             "doc2": str2_minhashing.signature,
                             "doc3": str3_minhashing.signature}

    lsh = LSH(signatures_collection, 0.5)

    print(lsh.candidate_pairs)
    print(lsh.similar_pairs)



if __name__== '__main__':
    test_lsh_similarity()
